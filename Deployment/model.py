import streamlit as st
import pandas as pd
import numpy as np
import pickle

# load all files

with open("model.pkl", "rb") as f: # load the model
    model = pickle.load(f)
    
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("encoder.pkl", "rb") as f: # load the scaler
    encoder = pickle.load(f)

# with open('column_names.pkl', 'rb') as f:
#     column_names = pickle.load(f)

# Kamar Tidur', 'Kamar Mandi', 'Luas Tanah', 'Luas Bangunan', 'Daya Listrik']
# 'Lokasi', 
# 'Sertifikat' = 'SHM - Sertifikat Hak Milik', 'HGB - Hak Guna Bangunan', 'Lainnya (PPJB,Girik,Adat,dll)', nan

def app():
    
    with st.form('from_website_data'):
        # write short description about the model
        st.write('''
        # **IKN Property Model**
        - The model used for this detection is `...` Regression which Hyperparameter have been tuned.
        - This model achieved `...` score ....
        ''')
        
        url = st.text_input('URL', 'https://www.google.com', help='The URL that will be analyzed')

        daya = {1: "ISO-8859-1", 2: "UTF-8", 3: "utf-8", 4: "us-ascii", 5: "iso-8859-1", 6: "unknown", 7: "windows-1252", 8: "windows-1251"}
                
        server_choice = {1: 'Apache', 2: 'cloudflare-nginx', 3: 'other', 4: 'Server', 5: 'GSE', 6: 'nginx', 7: 'unknown', 8: 'Microsoft-HTTPAPI/2.0', 9: 'nginx/1.8.0', 10: 'nginx/1.10.1', 11: 'Microsoft-IIS/7.5', 12: 'YouTubeFrontEnd', 13: 'Apache/2.2.22 (Debian)', 14: 'nginx/1.12.0', 15: 'Microsoft-IIS/6.0', 16: 'Apache/2.4.23 (Unix) OpenSSL/1.0.1e-fips mod_bwlimited/1.4', 17: 'Apache/2.2.14 (FreeBSD) mod_ssl/2.2.14 OpenSSL/0.9.8y DAV/2 PHP/5.2.12 with Suhosin-Patch'}
        
        whois_country_choice = {1: "AU", 2: "CA", 3: "ES", 4: "US", 5: "other", 6: "unknown", 7: "PA", 8: "FR", 9: "KR", 10: "CZ", 11: "JP", 12: "ru", 13: "UK", 14: "CN", 15: "GB", 16: "UY"}
                
        CHARSET = st.selectbox("Select Charset", options=list(charset_choice.values()), help='The character encoding standard (also called character set)')

        SERVER = st.selectbox("Select Server", options=list(server_choice.values()), help='The operative system of the server got from the packet response')

        CONTENT_LENGTH = st.number_input('CONTENT_LENGTH', min_value=0, max_value=9806, value=50, help='The content size of the HTTP header')

        WHOIS_COUNTRY = st.selectbox("Select Country", options=list(whois_country_choice.values()), help='The countries we got from the server response (specifically, our script used the API of Whois)')

        WHOIS_STATEPRO = st.selectbox("Select States", options=list(WHOIS_STATEPRO_choice.values()), help='The states we got from the server response (specifically, our script used the API of Whois)')
    
        kamar_tidur = st.number_input('Kamar Tidur', min_value=0, max_value=20, value=0, help='The number of bedrooms')
        
        kamar_mandi = st.number_input('Kamar Mandi', min_value=0, max_value=20, value=0, help='The number of bathrooms')
        
        luas_tanah = st.number_input('Luas Tanah', min_value=0, max_value=100000, value=0, help='The land area in square meters')
        
        luas_bangunan = st.number_input('Luas Bangunan', min_value=0, max_value=100000, value=0, help='The building area in square meters')
        
 
        #submit buttion
        submitted = st.form_submit_button('Predict')
    
    data_inf = {
        'CONTENT_LENGTH': CONTENT_LENGTH,
        'CHARSET': CHARSET,
        'SERVER': SERVER,
        'WHOIS_COUNTRY': WHOIS_COUNTRY,
        'WHOIS_STATEPRO': WHOIS_STATEPRO
    }

    
    data_inf = pd.DataFrame([data_inf])

    # logic ketika user submit
    if submitted:
        #split between numerical and categorical columns
        data_inf_num = data_inf[['URL_LENGTH', 'NUMBER_SPECIAL_CHARACTERS', 'CONTENT_LENGTH', 
                                 'WHOIS_REGDATE', 'WHOIS_UPDATED_DATE', 'TCP_CONVERSATION_EXCHANGE', 
                                 'DIST_REMOTE_TCP_PORT', 'REMOTE_IPS', 'APP_BYTES', 'SOURCE_APP_PACKETS', 
                                 'REMOTE_APP_PACKETS', 'SOURCE_APP_BYTES', 'REMOTE_APP_BYTES', 'APP_PACKETS', 
                                 'DNS_QUERY_TIMES']]
        
        data_inf_cat = data_inf[['CHARSET', 'SERVER', 'WHOIS_COUNTRY', 'WHOIS_STATEPRO']]
        
        # scaling and encoding
        data_inf_num_scaled = scaler.transform(data_inf_num)
        
        # encode categorical data
        data_inf_cat_encoded = encoder.transform(data_inf_cat)
        
        # transform to dataframe
        # data_inf_num_scaled = pd.DataFrame(data_inf_num_scaled, columns=data_inf_num.columns)

        # concat all data 
        data_inf_final = pd.concat([data_inf_num_scaled, data_inf_cat_encoded], axis=1)
        
        # if len(column_names) != len(set(column_names)):
        #     st.write("column_names contains duplicates")
            
        # if len(data_inf_final.columns) != len(set(data_inf_final.columns)):
        #     st.write("data_inf_final has duplicate column names")

        # Check Missing Values
        data_inf_final.isnull().sum()

        # fill null value with zeros
        data_inf_final = data_inf_final.fillna(0)
        
        #predict using model
        y_pred_inf = model.predict(data_inf_final)
        
        st.dataframe(data_inf)
        
        if y_pred_inf == 0:
            # write with green color the predicted price
            st.markdown(f'<p style="color: green;">Predicted Price: {y_pred_inf[0]}</p>', unsafe_allow_html=True)
        
if __name__ == '__main__':
    app()