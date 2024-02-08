import streamlit as st
from PIL import Image
import eda 
import model

page = st.sidebar.selectbox(label='Page:', options=['Homepage', 'Exploration Data Analysis', 'Prediction'])

if page == 'Homepage':
    st.markdown("<h1 style='text-align: center;'>WELCOME TO IKN PROPERTY</h1>", unsafe_allow_html=True)
    st.header('')

    #Tambahkan gambar
    image = Image.open('IKN_LOGO2.png')
    st.image(image) 
    st.caption('Please check our github repository [here!](https://github.com/FTDS-assignment-bay/p2-final-project-ftds-026-rmt-group-001)')
    st.markdown('----')
    
    with st.expander("Project's Background"):
        st.write('''The Indonesian government's decision to relocate the national capital to the Kalimantan area, with the new capital named IKN (Ibu Kota Negara), will likely lead to significant changes in the region's real estate market. 
                 The goal is to develop a prediction model application sthat can accurately estimate house prices in the IKN area. ''')

    with st.expander("What is IKN Property ?"):
        st.write('''Leveraging the most recent price data, this application serves as a price estimation tool designed to assist developers and homeowners in estimating and determining the value of their residential properties in IKN (Ibu Kota Nusantara).
                 This application will be valuable for both prospective homebuyers and real estate investors seeking insights into property values in the emerging capital city.''')
        
    with st.expander("Dataset"):
        st.write('''The dataset used to build the house price prediction model for the IKN area is obtained through web scraping from rumah123.com. This dataset aims to capture a comprehensive view of the real estate market in Balikpapan. ''')
        
    with st.expander("Conclusion"):
        st.write(
            ''' 
            1. EDA Conclusion :
                 
                The analysis of the dataset reveals several key trends in the Balikpapan real estate market. Most houses feature land and building areas below 500 square meters, and larger areas correlate with higher prices. Balikpapan city commands the highest average house prices (IDR 2.4 billion) due to its central location, while the East Balikpapan area, farther from the city center, shows the lowest prices (IDR 1.3 billion). Ownership Certificate is the most common certificate type in home sales, constituting 86% of transactions. 
                The majority of houses for sale are situated in the South Balikpapan area. Furniture condition data is often missing, and a strong correlation exists between Building Area, Land Area, Bedrooms, and house prices, indicating their impact on property values. 
            2. Model Conclusion :
                 
                The model used for this detection is XGBRegressor Regression Model which Hyperparameter have been tuned. And the model achieved 88% R² Train Score and 83% R² Test Score.
            ''')
        
    with st.expander("Recommendation"):
        st.write(
            ''' 
            1. Given the strong correlation between house features (Luas Bangunan, Luas Tanah, Kamar Tidur) and prices, real estate developers or sellers may consider focusing on properties with larger and well-designed living spaces. 
            Emphasizing these features in marketing materials could attract potential buyers seeking spacious and comfortable homes.
                
            2. For properties in the East Balikpapan area, where prices are comparatively lower, there may be an opportunity for real estate investors to explore strategic development projects or renovations to enhance the appeal of the area. 
            Highlighting any upcoming infrastructure developments or amenities could also contribute to increased property values over time.
                 
            3.  Additionally, since Sertifikat Hak Milik is the most common certificate type, real estate professionals should streamline processes related to this type of certificate to facilitate smoother transactions. 
            Providing clear information and guidance on certificate-related matters can build trust and simplify the buying process for potential customers.
            ''')

    with st.expander("Meet our team"):
        st.write("- Masayu Anandita Prameswari | [LinkedIn](https://www.linkedin.com/in/masayuanandita-/) | [Github](https://github.com/masayuanandita)")
        st.write("- Gilbert Kurniawan Hariyanto | [LinkedIn](https://www.linkedin.com/in/gilbert-kurniawan-h/) | [Github](https://github.com/gilbertk27)")
        st.write("- Ade William Tabrani | [LinkedIn] () | [Github] () ")
        st.write("- Mardhya Malik Nurbani | [LinkedIn](https://www.linkedin.com/in/mnurbani/) | [Github](https://github.com/mnurbani97)")

elif page == 'Exploration Data Analysis':
    eda.run()
else:
    model.run()