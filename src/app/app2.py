import streamlit as st
import pandas as pd
import numpy as np
import csv

st.title("Alkoholkonsum")


df = pd.read_csv("src/app/data_alcohol.csv")
auwahl = st.selectbox('Wähle die Region aus', df)









#%%

#%%
