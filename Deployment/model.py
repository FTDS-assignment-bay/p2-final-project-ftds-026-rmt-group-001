import streamlit as st
import pandas as pd
import numpy as np
import xgboost
from PIL import Image
from joblib import load

# load all files
model = load('xgb_tuned_model.joblib')
transformer = load('transformer.joblib')

def run():
    with st.form('from_website_data'):
        # write short description about the model
        st.write('''
        # **IKN Property Prediction**
        - The model used for this Regression is `XGBRegressor` Model which Hyperparameter have been tuned.
        - This model achieved `88%` R² Train Score and `83%` R² Test Score.
        ''')
        
        #Tambahkan gambar
        image = Image.open('IKN_LOGO2.png')
        st.image(image) 
                
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
            
            # first get the key of the lokasi
            for key, value in lokasi_choice.items():
                if value == lokasi:
                    lokasi = key
                    break
            
            # filter by same lokasi based on the key
            clean_data_fix = clean_data_fix[clean_data_fix['Lokasi'] == lokasi]
                        
            # if 10 random listing is not enough from the same lokasi, then add the rest from random other lokasi
            if clean_data_fix.shape[0] < 10:
                # filter first by price range
                clean_data_fix_additional = pd.read_csv('clean_data_fix.csv')
                clean_data_fix_additional = clean_data_fix_additional[clean_data_fix_additional['Harga'] > y_pred_inf[0] * 1000]
                clean_data_fix_additional = clean_data_fix_additional[(clean_data_fix_additional['Harga'] > y_pred_inf[0] * 1000 * 0.8) & (clean_data_fix_additional['Harga'] < y_pred_inf[0] * 1000 * 1.2)]
                # filter by different lokasi
                clean_data_fix_additional = clean_data_fix_additional[clean_data_fix_additional['Lokasi'] != lokasi]
                # get the rest of the 10 random listing
                if clean_data_fix_additional.shape[0] > 10 - clean_data_fix.shape[0]:
                    clean_data_fix_additional = clean_data_fix_additional.sample(10 - clean_data_fix.shape[0])
                # combine the 10 random listing from the same lokasi and the rest from different lokasi
                clean_data_fix = pd.concat([clean_data_fix, clean_data_fix_additional])
            else:
                clean_data_fix = clean_data_fix.sample(10)
                
            # if there is no listing, show warning to user that cant find example in the price range
            if clean_data_fix.shape[0] == 0:   
                st.warning('Tidak ada listing yang mirip dengan range harga')
                st.stop()
                
            # Create a list of tabs
            tabs = st.tabs([f'Listing {i+1}' for i in range(10)])

            for i in range(10):
                # Define the content for each tab
                with tabs[i]:
                    st.image(clean_data_fix.iloc[i]["Img_Hyperlink"], width=None)
                    st.write(f'**Price:** {clean_data_fix.iloc[i]["Harga"]/1000} Milyar')
                    st.write(f'**Location:** {clean_data_fix.iloc[i]["Lokasi"]}')
                    st.markdown(f'**Link:** [Click here]({clean_data_fix.iloc[i]["Hyperlink"]})')
        else:
            final = round(y_pred_inf[0], 3)
            st.markdown(f'<p style="color: green; text-align: center; font-size: 50px;">Predicted Price: {final:.4f} Juta</p>', unsafe_allow_html=True)
            
            # Get random 10 listings from clean_data_fix.csv based on the price and show them to the user, including image, hyperlink, and price
            st.write('**10 Random Listing**')
            clean_data_fix = pd.read_csv('clean_data_fix.csv')
            clean_data_fix = clean_data_fix[clean_data_fix['Harga'] > y_pred_inf[0]]
            
            # Filter 10 random listings with a price around 10% of the predicted price both lower and upper
            clean_data_fix = clean_data_fix[(clean_data_fix['Harga'] > y_pred_inf[0] * 0.8) & (clean_data_fix['Harga'] < y_pred_inf[0] * 1.2)]
            
            # If there are no listings, show a warning to the user that there are no listings in the price range
            if clean_data_fix.shape[0] == 0:
                st.warning('Tidak ada listing yang mirip dengan range harga')
                st.stop()
            
            # first get the key of the lokasi
            for key, value in lokasi_choice.items():
                if value == lokasi:
                    lokasi = key
                    break
            
            # Filter by the same location
            clean_data_fix_same_loc = clean_data_fix[clean_data_fix['Lokasi'] == lokasi]
            
            # If there are not enough listings with the same location, get additional listings from different locations
            if clean_data_fix_same_loc.shape[0] < 10:
                # Filter first by price range
                clean_data_fix_additional = pd.read_csv('clean_data_fix.csv')
                clean_data_fix_additional = clean_data_fix_additional[clean_data_fix_additional['Harga'] > y_pred_inf[0]]
                clean_data_fix_additional = clean_data_fix_additional[(clean_data_fix_additional['Harga'] > y_pred_inf[0] * 0.8) & (clean_data_fix_additional['Harga'] < y_pred_inf[0] * 1.2)]
                
                # Filter by different location
                clean_data_fix_additional = clean_data_fix_additional[clean_data_fix_additional['Lokasi'] != lokasi]
                
                # Get the rest of the 10 random listings
                if clean_data_fix_additional.shape[0] > 10 - clean_data_fix_same_loc.shape[0]:
                    clean_data_fix_additional = clean_data_fix_additional.sample(10 - clean_data_fix_same_loc.shape[0])
                
                # Combine the 10 random listings from the same location and the rest from different locations
                clean_data_fix = pd.concat([clean_data_fix_same_loc, clean_data_fix_additional])
            else:
                clean_data_fix = clean_data_fix_same_loc.sample(10)

            # Display the listings using a tab structure
            tabs = st.tabs([f'Listing {i+1}' for i in range(10)])

            for i in range(10):
                # Define the content for each tab
                with tabs[i]:
                    st.image(clean_data_fix.iloc[i]["Img_Hyperlink"], use_column_width=True)
                    st.write(f'**Price:** {clean_data_fix.iloc[i]["Harga"]} Juta')
                    st.markdown(f'**Location:** {clean_data_fix.iloc[i]["Lokasi"]}')
                    st.markdown(f'**Link:** [Click here]({clean_data_fix.iloc[i]["Hyperlink"]})')
        
if __name__ == '__main__':
    app()