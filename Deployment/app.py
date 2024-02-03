import streamlit as st
from PIL import Image
import eda 
import model
import homepage

page = st.sidebar.selectbox(label='Page:', options=['Homepage', 'Exploration Data Analysis', 'Prediction'])

if page == 'Homepage' : 
    homepage.run()
elif page == 'Exploration Data Analysis' :
    eda.run()
else:
    model.run()