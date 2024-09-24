import streamlit as st
import pandas as pd

st.set_page_config("Consulta de Clientes", page_icon=("ico LOGO.32x32.Imatik.png"))

dados = pd.read_csv('clientes.csv')

st.title('Consulta de clientes')

busca = st.text_input('Pesquisar')

if busca:
    # filtra os dados pela coluna "nome"
    resultados = dados[dados['nome'].str.contains(busca, case=False, na=False)]

    # exibe os resultados em uma tabela
    if not resultados.empty:
        st.write('Resultados encontrados:')
        st.dataframe(resultados)
    else:
        st.write('Nenhum resultado encontrado.')
st.divider()





# toggle da tabela

tabela_clientes = st.toggle('Tabela de clientes')

if tabela_clientes:
    st.dataframe(dados)
