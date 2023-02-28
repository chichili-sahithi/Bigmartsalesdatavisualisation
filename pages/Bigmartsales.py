import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Bigmartsales.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "bigmartsales.csv")

st.title(":orange[Dashboard - Bigmart Sales]:sunglasses:")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

Item_Type = st.selectbox("Select the Item Type:", df['Item_Type'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Item_Type'] == Item_Type], x="Item_MRP")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Item_Type'] == Item_Type], y="Item_MRP")
col2.plotly_chart(fig_2, use_container_width=True)