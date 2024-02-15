import streamlit as st
import pandas as pd 
#import streamlit_pandas as sp  
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth


#cred = credentials.Certificate('ash-ppm-tracking-app-1668deebeb15.json')
#firebase_admin.initialize_app(cred)

st.sidebar.header("Option")
text = st.sidebar.text_area('inter data Here')
button1 = st.sidebar.button("Clean text")
if button1:
          st.write(text)
def home(uploaded_file):
    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please uplod a file')

def Data_Entrey():
    st.title("streamlit for & Task statuss")
    menu =['Home, Data_Summary']
    choise = st.sidebar.slecctbox("menu, menu")
       


def app():  
    st.title('✅Welcome to PPM Tracking app')
    st.header('PPM Dataset')
    data = pd.read_csv('data.csv') 
    st.write(data.head())

    st.subheader('pick-up the Tsak stats valu on the PPM Dataset')
    Task_status_dist = pd.DataFrame (data['Task status'].value_counts())
    st.bar_chart(Task_status_dist)

    st.markdown('* **firest featur:** please chack the box if the task is get done.. I calculatted it using compalation % ')

    disp_col = st.bar_chart()
    max_depth = disp_col.slider("Task status", min_value =1, max_value=26, step = 3)
    st.title("streamlit for & Task statuss")
    menu =['Home, Data_Summary']