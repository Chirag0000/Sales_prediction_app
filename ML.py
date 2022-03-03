import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
RF_model = pickle.load(open('model.pkl', 'rb'))
Xg_model=pickle.load(open('Xg_model.pkl','rb'))
LR_model=pickle.load(open('LR_model.pkl','rb'))

# # FUNCTION

def run_ml():  
  submenu=st.sidebar.selectbox("Select the Model",["Random Forest","XgBoost"])

  if submenu=="Random Forest":
    st.subheader("Random Forest")
    shop_id = st.slider('shop_id', 0,59, 1 )
    item_id = st.slider('item_id', 0,22167, 1 )
    date_block_num=st.slider('date_block_num',0,34,1)
    Sales_per_item = st.slider('Sales_per_item', -995,2400, 1 )

  
    data = {
      'Shop ID':shop_id,
      'Item ID':item_id,
      'Date number':date_block_num,
      'Sales for item($)':Sales_per_item,
    }
    report_data = pd.DataFrame(data, index=[0])

    if st.button("Predict"):

      quantity = RF_model.predict(report_data)
      st.subheader('Monthly Sales forecast')
      st.subheader(quantity)
  
  elif submenu=="XgBoost":
    st.subheader("Xg Boost")
    shop_id = st.slider('shop_id', 0,59, 1 )
    item_id = st.slider('item_id', 0,22167, 1 )
    date_block_num=st.slider('date_block_num',0,34,1)
    Sales_per_item = st.slider('Sales_per_item', -995,2400, 1 )

    data = {
      'Shop ID':shop_id,
      'Item ID':item_id,
      'Date number':date_block_num,
      'Sales for item($)':Sales_per_item,
    }
    report_data = pd.DataFrame(data, index=[0])

    if st.button("Predict"):

      quantity = Xg_model.predict(report_data)
      st.subheader('Monthly Sales forecast')
      st.subheader(quantity)
