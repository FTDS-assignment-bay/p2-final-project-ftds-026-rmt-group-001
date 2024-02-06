import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import scipy.stats as stats
import statistics
import numpy as np

def run():
    # Membuat title
    st.markdown("<h1 style='text-align: center;'>Exploration Data Analysis</h1>", unsafe_allow_html=True)
    #Menambahkan deskripsi
    st.markdown('----')

    #Tambahkan gambar
    image = Image.open('IKN_LOGO2.png')
    st.image(image) 
    st.write('by FTDS-RMT026-GROUP01')
    st.markdown('----')

    st.header('Comparision House Price Based On Area')
    image = Image.open('EDA01.png')
    st.image(image)
    with st.expander("**Insight** :"):
        st.caption(
            '''
            Majority of the houses feature a land area less than 500 square meters. Similarly, the building area data reveals a predominant trend, with a significant portion also falling below 500 square meters. 
            Additionally, it is observed that houses with larger land or building areas tend to command higher prices.
            ''')

    st.header('Averages House Price Based On Location')
    image = Image.open('EDA9.png')
    st.image(image)
    with st.expander("**Insight** :"):
        st.caption(
            '''
            The Balikpapan city area stands out with the highest average house price. This trend can be attributed to the advantageous locations of properties in urban areas, 
            which typically command higher selling values and present greater profit potential.
            ''')
        
    st.header('Type of Certificate')
    image = Image.open('EDA7.png')
    st.image(image)
    with st.expander("**Insight** :"):
        st.caption(
            '''
            From 3 type of sertifikat, the Sertifikat Hak Milik is have 86% distibution thus making it the most common type of certificate in home sales.
            ''')

    st.header('Comparasion House Price Based On Room')
    image = Image.open('EDA02.png')
    st.image(image)
    with st.expander("**Insight** :"):
        st.caption(
            '''
            An increase in the count of bedrooms or bathrooms is associated with a higher expected house price.
            ''')

    st.header('Correlation Feature')
    image = Image.open('EDA10.png')
    st.image(image)
    with st.expander("**Insight** :"):
        st.caption(
            '''
            The correlation map indicates a strong relationship between the Luas Bangunan, Luas Tanah, and Kamar Tidur columns with the Price column. 
            This suggests that changes or variations in these features are closely associated with corresponding changes in the house prices.
            ''')
        
    st.header('Histogram of Some Column')
    with st.expander("Harga"):
        image = Image.open('EDA1.png')
        st.image(image)
        st.write(''' ''')

    with st.expander("Kamar Tidur"):
        image = Image.open('EDA2.png')
        st.image(image)
        st.write(''' ''')

    with st.expander("Kamar Mandi"):
        image = Image.open('EDA3.png')
        st.image(image)
        st.write(''' ''')

    with st.expander("Luas Tanah"):
        image = Image.open('EDA4.png')
        st.image(image)
        st.write(''' ''')
        
    with st.expander("Luas Bangunan"):
        image = Image.open('EDA5.png')
        st.image(image)
        st.write(''' ''')    



if __name__ == '__main__':
    run()
