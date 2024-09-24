import streamlit as st
import pandas as pd 
from datetime import date

def gravar_dados(nome,dt_nasc,tipo):
    if nome and dt_nasc <= date.today() and tipo:
        with open("clientes.csv","a",encoding="utf-8") as file:
            file.write(f"{nome}, {dt_nasc}, {tipo}\n")
        st.session_state["Sucesso"] = True
    else:
        st.session_state["Sucesso"]= False
    

st.set_page_config("Cadastro de Clientes", page_icon=("ico LOGO.32x32.Imatik.png"))

st.title("Cadastro de clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente",
                     placeholder="Digite o nome.....",
                     key="nome_cliente"
                     )

dt_nasc = st.date_input("data de nascimento",
                        format= "DD/MM/YYYY",
                        min_value= date(1950,1,1),
                        key="data_nasc"
                        )

tipo = st.selectbox("Escolha o tipo de cliente",
                    ["Pessoa Juridica", "Pessoa física"],
                    index=None,
                    placeholder="Escolha a Tipologia.....",
                    key="tipologia"
                    )

btn_cadastro = st.button("Cadastrar", 
                         on_click= gravar_dados,
                         args=[nome,dt_nasc,tipo])

if btn_cadastro:
    if st.session_state["Sucesso"]:
        st.success("Dados cadastrados com sucesso", icon="🆗")
    else:
        st.error("Houve algum erro no cadastro",
                 icon="❌")