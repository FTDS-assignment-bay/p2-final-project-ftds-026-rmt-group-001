import streamlit as st
from PIL import Image
import eda 
import model

page = st.sidebar.selectbox(label='Page:', options=['Homepage', 'Exploration Data Analysis', 'Prediction'])