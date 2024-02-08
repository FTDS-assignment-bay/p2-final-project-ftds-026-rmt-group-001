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
    image = Image.open('EDA11.png')
    st.image(image)
    with st.expander("**Insight** :"):
        st.caption(
            '''
            Majority of the houses feature a land area less than 500 square meters. Similarly, the building area data reveals a predominant trend, with a significant portion also falling below 500 square meters. 
            Additionally, it is observed that houses with larger land or building areas tend to command higher prices.
            ''')

    st.header('Averages House Price Based On Location')
    image = Image.open('EDA1.png')
    st.image(image)
    with st.expander("**Insight** :"):
        st.caption(
            '''
            1. The Balikpapan city area exhibits the highest house prices compared to other regions, boasting an estimated average house price of IDR 2.4 billion. This can be attributed to its central location, 
            making it unsurprising that the housing prices in this area rank among the most expensive.

            2. Conversely, the East Balikpapan area displays the lowest house prices based on the provided data, with an estimated average price of IDR 1.3 billion. 
            This disparity may be linked to the East Balikpapan area's distance from the city center.
            ''')
        
    st.header('Type of Certificate')
    image = Image.open('EDA9.png')
    st.image(image)
    with st.expander("**Insight** :"):
        st.caption(
            '''
            From 3 type of sertifikat, the Sertifikat Hak Milik is have 86% distibution thus making it the most common type of certificate in home sales.
            ''')

    st.header('Most locations selling houses')
    image = Image.open('EDA8.png')
    st.image(image)
    with st.expander("**Insight** :"):
        st.caption(
            '''
            From the bar chart, most of sell house locations are in the South Balikpapan area.
            ''')

    st.header('Comparasion House Price Based On Furniture Condition')
    image = Image.open('EDA10.png')
    st.image(image)
    with st.expander("**Insight** :"):
        st.caption(
            '''
            Most furniture condition is unknown, it is because most of the seller did not fill the data.
            ''')
        
    st.header('Correlation Feature')
    image = Image.open('EDA12.png')
    st.image(image)
    with st.expander("**Insight** :"):
        st.caption(
            '''
            The correlation map indicates a strong relationship between the Luas Bangunan, Luas Tanah, and Kamar Tidur columns with the Price column. 
            This suggests that changes or variations in these features are closely associated with corresponding changes in the house prices.
            ''')
        

if __name__ == '__main__':
    run()
