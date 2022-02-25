
import streamlit as st 
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
from ML import run_ml

st.title('Sales Prediction App')
st.sidebar.title('Sales Prediction App')

image = Image.open('sales(profile).png')
st.image(image, '')

st.subheader('This is an interactive dashboard, created on the dataset given by 1C Company(largest Russian Software firm) with a challenging time-series dataset consisting of daily sales data. The result for prediction is based on input parameter entered.')

def main():
	menu = ["Home","ML"]
	choice = st.sidebar.selectbox("Menu",menu)


	if choice == "ML":
		run_ml()
	else:
		pass

if __name__ == '__main__':
	main()