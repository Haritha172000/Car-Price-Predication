import pandas as pd
import numpy as numpy
import pickle as pk
import streamlit as st

model = pk.load(open('model.pkl','rb'))

st.header('Car price Prediction ML model')
cars_data = pd.read_cvs('Cardetails.csv')

def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip()
cars_data['name'] = cars_data['name'].apply(get_brand_name)
  
st.selectbox('Select Car Brand',cars_data['name'].unique())
st.slider('Car Manufactured Year', 1994,2024)
st.slider('No of kms Driven',11,200000)
st.selectbox('Fuel type', cars_data['fuel'].unique())
st.selectbox('Seller type',cars_data['seller_type'].unique())
st.selectbox('Transmissions type', cars_data['transmission'].unique())
st.slider('Car Milege',10,40)
st.slider('Engine cc',700,5000)
st.slider('Max Power',0,200)
st.slider('No of Seats',5,10)

if(st.button("Predict"):
  input_data_model = pd.DataFrame([[5,2022,12000,1,1,1,1,12.99,2494.0,100.6,5.0]],
                                  columns =[



  
