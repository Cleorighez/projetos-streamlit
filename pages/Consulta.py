import streamlit as st
import pandas as pd

st.set_page_config("Consulta de Clientes", page_icon=("ico LOGO.32x32.Imatik.png"))

dados = pd.read_csv("clientes.csv")

st.title("Clientes cadastrados")
st.divider()

st.dataframe(dados)