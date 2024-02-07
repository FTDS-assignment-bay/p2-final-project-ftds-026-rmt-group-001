import streamlit as st
import pandas as pd
import numpy as np
import xgboost
from joblib import load

# load all files
model = load('xgb_tuned_model.joblib')
transformer = load('transformer.joblib')

def app():
    
    with st.form('from_website_data'):
        # write short description about the model
        st.write('''
        # **IKN Property Model**
        - The model used for this detection is `...` Regression which Hyperparameter have been tuned.
        - This model achieved `...` score ....
        ''')
        
        
                
        sertifikat_choice = {'SHM': 'SHM - Sertifikat Hak Milik', 'HGB': 'HGB - Hak Guna Bangunan', 'Lainnya': 'Lainnya (PPJB, Girik, Adat, dll)'}

        lokasi_choice = {
            'Balikpapan Selatan': 'Balikpapan Selatan, Balikpapan',
            'Balikpapan Utara': 'Balikpapan Utara, Balikpapan',
            'Balikpapan Tengah': 'Balikpapan Tengah, Balikpapan',
            'Balikpapan Baru': 'Balikpapan Baru, Balikpapan',
            'Balikpapan Timur': 'Balikpapan Timur, Balikpapan',
            'Damai': 'Damai, Balikpapan',
            'Gn. Samarinda': 'Gn. Samarinda, Balikpapan',
            'Sepinggan': 'Sepinggan, Balikpapan',
            'Sumber Rejo': 'Sumber Rejo, Balikpapan',
            'Balikpapan Kota': 'Balikpapan Kota, Balikpapan',
            'Marga Sari': 'Marga Sari, Balikpapan',
            'Gn. Sari Ilir': 'Gn. Sari Ilir, Balikpapan',
            'Manggar': 'Manggar, Balikpapan',
            'Batakan': 'Batakan, Balikpapan',
            'Gunung Bahagia': 'Gunung Bahagia, Balikpapan',
            'Balikpapan Barat': 'Balikpapan Barat, Balikpapan',
            'Karang Joang': 'Karang Joang, Balikpapan',
            'Manggar Baru': 'Manggar Baru, Balikpapan',
            'Karang Rejo': 'Karang Rejo, Balikpapan',
            'Batu Ampar': 'Batu Ampar, Balikpapan',
            'Telaga Sari': 'Telaga Sari, Balikpapan',
            'Klandasan Ulu': 'Klandasan Ulu, Balikpapan',
            'Klandasan Ilir': 'Klandasan Ilir, Balikpapan',
            'Muara Rapak': 'Muara Rapak, Balikpapan',
            'Kariangau': 'Kariangau, Balikpapan',
            'Baru Tengah': 'Baru Tengah, Balikpapan',
            'Lamaru': 'Lamaru, Balikpapan',
            'Prapatan': 'Prapatan, Balikpapan',
            'Teritip': 'Teritip, Balikpapan',
            'Karang Jati': 'Karang Jati, Balikpapan'
        }


        sertifikat = st.selectbox("Pilih Sertifikat", options=list(sertifikat_choice.values()), help='The type of certificate of the house')

        lokasi = st.selectbox("Piluh Loasi", options=list(lokasi_choice.values()), help='The location of the house')
 
        kamar_tidur = st.number_input('Kamar Tidur', min_value=0, max_value=30, value=2, help='The number of bedrooms')
        
        kamar_mandi = st.number_input('Kamar Mandi', min_value=0, max_value=120, value=2, help='The number of bathrooms')
        
        luas_tanah = st.number_input('Luas Tanah', min_value=0, max_value=100000, value=300, help='The land area in square meters')
        
        luas_bangunan = st.number_input('Luas Bangunan', min_value=0, max_value=100000, value=270, help='The building area in square meters')
        
        daya = st.number_input('Daya Listrik', min_value=0, max_value=22000, value=1300, help='The power capacity of the house in watt')

        #submit buttion
        submitted = st.form_submit_button('Predict')
        
    
    data_inf = {
        'Sertifikat': sertifikat,
        'Lokasi': lokasi,
        'Kamar Tidur': kamar_tidur,
        'Kamar Mandi': kamar_mandi,
        'Luas Tanah': luas_tanah,
        'Luas Bangunan': luas_bangunan,
        'Daya Listrik': daya   
    }

    data_inf = pd.DataFrame([data_inf])

    # logic ketika user submit
    if submitted:
        
        # check for luas bangunan must be smaller than luas tanah
        if luas_bangunan > luas_tanah:
            st.warning('Luas Bangunan tidak boleh lebih besar dari Luas Tanah')
            st.stop()
        
        # show data_inf
        st.dataframe(data_inf)

        # scaling and encoding with transformer
        data_inf_final = transformer.transform(data_inf)
        
        # predict using model
        y_pred_inf = model.predict(data_inf_final)
        
        if y_pred_inf[0] > 1000:
            y_pred_inf[0] = y_pred_inf[0] / 1000
            final = round(y_pred_inf[0], 2)
            st.markdown(f'<p style="color: green; text-align: center; font-size: 50px;">Predicted Price: {final:.2f} Milyar</p>', unsafe_allow_html=True)
            
            # get random 10 listing form clean_data_fix.csv based on the price and show it to user both the image, hyperlink, and the price
            st.write('**10 Random Listing**')
            clean_data_fix = pd.read_csv('clean_data_fix.csv')
            clean_data_fix = clean_data_fix[clean_data_fix['Harga'] > y_pred_inf[0] * 1000]
            
            # filter 10 random listing with price around 10% of the predicted price both lower and upper
            clean_data_fix = clean_data_fix[(clean_data_fix['Harga'] > y_pred_inf[0] * 1000 * 0.8) & (clean_data_fix['Harga'] < y_pred_inf[0] * 1000 * 1.2)]
            
            # if there is no listing, show warning to user that cant find example in the price range
            if clean_data_fix.shape[0] == 0:
                st.warning('Tidak ada listing yang mirip dengan range harga')
                st.stop()      
            
            # get 10 random listing
            clean_data_fix = clean_data_fix.sample(10)
            
            for i in range(10):
                # the image in hyperlink, so load the image and show it to user
                st.write(f'**Listing {i+1}**')
                st.image(clean_data_fix.iloc[i]['Img_Hyperlink'], use_column_width=True)
                # divide {clean_data_fix.iloc[i]["Harga"]} by 1000 to convert from Juta to Milyar
                Harga_list = clean_data_fix.iloc[i]["Harga"]/1000
                st.write(f'**Price: {Harga_list} Milyar**')
                st.write(f'**Link: {clean_data_fix.iloc[i]["Hyperlink"]}**')
                            
        else:
            final = round(y_pred_inf[0], 3)
            st.markdown(f'<p style="color: green; text-align: center; font-size: 50px;">Predicted Price: {final:.4f} Juta</p>', unsafe_allow_html=True)
            
            # get random 10 listing form clean_data_fix.csv based on the price and show it to user both the image, hyperlink, and the price
            st.write('**10 Random Listing**')
            clean_data_fix = pd.read_csv('clean_data_fix.csv')
            clean_data_fix = clean_data_fix[clean_data_fix['Harga'] > y_pred_inf[0]]
            
            # filter 10 random listing with price around 10% of the predicted price both lower and upper
            clean_data_fix = clean_data_fix[(clean_data_fix['Harga'] > y_pred_inf[0] * 0.8) & (clean_data_fix['Harga'] < y_pred_inf[0] * 1.2)]
            
            # if there is no listing, show warning to user that cant find example in the price range
            if clean_data_fix.shape[0] == 0:
                st.warning('Tidak ada listing yang mirip dengan range harga')
                st.stop()      
            
            # get 10 random listing
            clean_data_fix = clean_data_fix.sample(10)
            
            for i in range(10):
                # the image in hyperlink, so load the image and show it to user
                st.write(f'**Listing {i+1}**')
                st.image(clean_data_fix.iloc[i]['Img_Hyperlink'], use_column_width=True)
                st.write(f'**Price: {clean_data_fix.iloc[i]["Harga"]} Juta**')
                st.write(f'**Link: {clean_data_fix.iloc[i]["Hyperlink"]}**')
        
if __name__ == '__main__':
    app()