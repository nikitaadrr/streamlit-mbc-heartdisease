import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# Load model
penyakitjantung = pickle.load(open('penyakit-jantung.sav', 'rb'))


st.title('Heart Diesease Prediction')
st.markdown(
"""
Welcome to the **Heart Disease Prediction** web app. This tool utilizes a **Classification** model to predict the age of fossils based on various geological and chemical parameters. Simply input the required data, and let the model do the rest!
"""
)

# Pengaturan Input
st.markdown("## Input Heart Disease Parameters")

Age = st.slider('Age', min_value=1, max_value=100, step=1)
RestingBP = st.slider('Resting BP', min_value=50, max_value=250, step=1)
Cholesterol = st.slider('Cholesterol', min_value=50, max_value=500, step=1)
FastingBS = st.slider('FastingBS', min_value=0	, max_value=5, step=1)
MaxHR = st.slider('Max HR', min_value=0	, max_value=5, step=1)
Oldpeak = st.slider('Oldpeak', min_value=0.0	, max_value=5, step=0.01)

# Kolom 2 untuk input tambahan
col3, col4 = st.columns(2)
with col3:
    Sex = st.selectbox('Sex', ['F', 'M'])
    ChestPainType = st.selectbox('Tipe Penyakit Dada', ['ASP', 'NAY', 'ATA', 'TA'])

with col4:
    RestingECG = st.selectbox('Resting ECG', ['Normal', 'ST', 'LVH'])
    ExerciseAngina = st.selectbox('Exercise Angina', ['Y', 'N'])
    ST_Slope = st.selectbox('ST_Slope', ['Up', 'Flat'])

# Memisahkan prediksi dengan section yang menarik
st.markdown("---")
st.markdown("<style>div.row-widget.stSlider { margin-bottom: -15px; }</style>", unsafe_allow_html=True)
st.markdown("## Predict Heart Disease")

# code untuk prediksi
heart_diagnosis = ''

#buat tombol
if st.button('Predict') :
    heart_predict = penyakitjantung.predict([[Age, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak, Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope]])
if(heart_predict[0]==1):
    heart_diagnosis = 'Pasien terkena penyakit jantung'
else :
    heart_diagnosis = 'Pasien tidak terkena penyakit jantung'

st.success(heart_diagnosis)
