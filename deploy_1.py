# -*- coding: utf-8 -*-
"""DEPLOY_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RNg99QNG22nJ8VHG2953EMqw2MBRW8iL

#DEPLOYMENT

##CREAT_LOAD_PKL_FILE
"""

# !pip install -U  --upgrade pip
import streamlit as st
# !pip install matplotlib
import pickle
import pandas as pd
import numpy as np
import matplotlib as plt 
echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc
st.write("DISTRIBUTION_PLOTTING FOR DATA_FRAME")
url = 'https://raw.githubusercontent.com/merrooo/ML_DATA/main/concrete_data.csv'
df=pd.read_csv(url)
x=df.loc[:,df.columns != 'Strength']
y=df['Strength']
   #------------------------------------------------------------------
st.title("""### VISUALIZATION """)
   #------------------------------------------------------------------
st.write("DISTRIBUTION_PLOTTING FOR DATA_FRAME")
button_VISU_1=st.button("DATA_FRAME",type="primary")
if button_VISU_1:
     fig, ax = plt.subplots()
     ax.hist(df, bins=20)
     st.pyplot(fig)
