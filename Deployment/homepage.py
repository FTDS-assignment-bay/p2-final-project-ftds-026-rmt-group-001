import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def make_clickable(link):
    return f'<a target="_blank" href="{link}">{link}</a>'

def run():
    #Membuat title
    st.title('IKN Property')

    #Tambahkan gambar
    image = Image.open('IKN LOGO.JPG')
    st.image(image, caption = '')

    #Menambahkan deskripsi
    st.write('')

    #Membuat garis
    st.markdown('----')

    #Masukkan pandas dataframe

    #Show dataframe
    df = pd.read_csv('rumah123_fix_data.csv')
    st.subheader('List')
    st.dataframe(df)

    st.markdown('----')

    st.subheader('Gambar Properti')

    links = [
        "https://picture.rumah123.com/r123/720x420-crop/house/ho15/15945789/original/hos15945789-rumah-di-jual-di-balikpapan-selatan-balikpapan-1704340035.jpg",
        "https://picture.rumah123.com/r123-images/720x420-crop/customer/1964420/2024-02-01-02-35-27-030b4254-675e-46cc-b965-e52a0bb80d6d.jpg",
        "https://picture.rumah123.com/r123-images/720x420-crop/customer/1926217/2023-12-01-06-10-42-94a69e3c-8b2e-4af7-9489-e15c0da42060.jpg",
        "https://picture.rumah123.com/r123/720x420-crop/house/ho14/14193967/original/hos14193967-rumah-di-jual-di-balikpapan-tengah-balikpapan-1689042171.jpg",
        "https://picture.rumah123.com/r123-images/720x420-crop/customer/1355633/2024-01-23-07-46-31-33b01afa-3599-49a3-8e3f-2eca551661c0.png"
    ]
    property_urls = [
    "https://www.rumah123.com//properti/balikpapan/hos15945789/",
    "https://www.rumah123.com//properti/balikpapan/hos16239750/",
    "https://www.rumah123.com//properti/balikpapan/hos15643485/",
    "https://www.rumah123.com//properti/balikpapan/hos14193967/",
    "https://www.rumah123.com//properti/balikpapan/hos15998364/"
    ]
    
    # Ambil informasi harga dan lokasi dari lima properti teratas
    top_5_harga_lokasi = df[['Harga', 'Lokasi']].head()
    # Membuat kolom untuk menampilkan gambar
    col1, col2, col3, col4, col5 = st.columns(5)

    # Menampilkan gambar dalam kolom masing-masing
    with col1:
        st.markdown(f'<a href="{property_urls[0]}" target="_blank"><img src="{links[0]}" style="width:100%;height:auto;"></a>', unsafe_allow_html=True)
        st.write(f'Harga: {top_5_harga_lokasi.iloc[0]["Harga"]}')
        st.write(f'Lokasi: {top_5_harga_lokasi.iloc[0]["Lokasi"]}')
    with col2:
        st.markdown(f'<a href="{property_urls[1]}" target="_blank"><img src="{links[1]}" style="width:100%;height:auto;"></a>', unsafe_allow_html=True)
        st.write(f'Harga: {top_5_harga_lokasi.iloc[1]["Harga"]}')
        st.write(f'Lokasi: {top_5_harga_lokasi.iloc[1]["Lokasi"]}')
    with col3:
        st.markdown(f'<a href="{property_urls[2]}" target="_blank"><img src="{links[2]}" style="width:100%;height:auto;"></a>', unsafe_allow_html=True)
        st.write(f'Harga: {top_5_harga_lokasi.iloc[2]["Harga"]}')
        st.write(f'Lokasi: {top_5_harga_lokasi.iloc[2]["Lokasi"]}')
    with col4:
        st.markdown(f'<a href="{property_urls[3]}" target="_blank"><img src="{links[3]}" style="width:100%;height:auto;"></a>', unsafe_allow_html=True)
        st.write(f'Harga: {top_5_harga_lokasi.iloc[3]["Harga"]}')
        st.write(f'Lokasi: {top_5_harga_lokasi.iloc[3]["Lokasi"]}')
    with col5:
        st.markdown(f'<a href="{property_urls[4]}" target="_blank"><img src="{links[4]}" style="width:100%;height:auto;"></a>', unsafe_allow_html=True)
        st.write(f'Harga: {top_5_harga_lokasi.iloc[4]["Harga"]}')
        st.write(f'Lokasi: {top_5_harga_lokasi.iloc[4]["Lokasi"]}')

    #Membuat bar plot
    # st.write('#### Plot AttackingWorkRate')
    # fig = plt.figure(figsize=(15,5))
    # sns.countplot(x='AttackingWorkRate', data = df)
    # st.pyplot(fig)

    # #Membuat histogram
    # st.write('#### Histogram of Age')
    # fig = plt.figure(figsize=(15,5))
    # sns.histplot(df['Overall'], bins = 30, kde = True)
    # st.pyplot(fig)

    # #membuat histogram berdasarkan inputan user
    # st.write('#### Histogram berdasarkan input user')
    # #kalo mau pake radio button, ganti selectbox jadi radio
    # option = st.selectbox('Pilih Column : ', ('Age', 'Weight', 'Height', 'ShootingTotal'))
    # fig = plt.figure(figsize= (15,5))
    # sns.histplot(df[option], bins = 30, kde = True)
    # st.pyplot(fig)

    # #Membuat Plotly plot

    # st.write('#### Plotly Plot - ValueEUR vs Overall')
    # fig = px.scatter(df, x = 'ValueEUR', y = 'Overall', hover_data = ['Name', 'Age'])
    # st.plotly_chart(fig)

if __name__ == '__main__':
    run()
