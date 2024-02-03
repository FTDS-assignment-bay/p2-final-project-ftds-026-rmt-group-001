import streamlit as st
from PIL import Image
import eda 
import model

page = st.sidebar.selectbox(label='Page:', options=['Homepage', 'Exploration Data Analysis', 'Prediction'])

if page == 'Homepage':
    st.markdown("<h1 style='text-align: center;'>WELCOME TO IKN PROPERTY</h1>", unsafe_allow_html=True)
    st.header('')

    #Tambahkan gambar
    image = Image.open('IKN_LOGO.jpg')
    st.image(image) 
    st.caption('Please check our github repository [here!](https://github.com/FTDS-assignment-bay/p2-final-project-ftds-026-rmt-group-001)')
    st.markdown('----')
    
    with st.expander("Project's Background"):
        st.write('''The Indonesian government's decision to relocate the national capital to the Kalimantan area, with the new capital named IKN (Ibu Kota Negara), will likely lead to significant changes in the region's real estate market. 
                 The goal is to develop a prediction model application sthat can accurately estimate house prices in the IKN area. ''')

    with st.expander("What is IKN Property ?"):
        st.write('''Leveraging the most recent price data, this application serves as a price estimation tool designed to assist developers and homeowners in estimating and determining the value of their residential properties in IKN (Ibu Kota Nusantara).
                 This application will be valuable for both prospective homebuyers and real estate investors seeking insights into property values in the emerging capital city.''')
        
    with st.expander("Workflow"):
        st.write(''' ''')
        
    with st.expander("Conclusion"):
        st.write(''' ''')
        
    with st.expander("Meet our team"):
        st.write("- Masayu Anandita Prameswari | [LinkedIn] () | [Github] ()")
        st.write("- Gilbert Kurniawan Hariyanto | [LinkedIn] () | [Github] ()")
        st.write("- Ade William Tabrani | [LinkedIn] () | [Github] () ")
        st.write("- Mardhya Malik Nurbani | [LinkedIn] () | [Github] ()")

elif page == 'Exploration Data Analysis':
    eda.run()
else:
    model.run()