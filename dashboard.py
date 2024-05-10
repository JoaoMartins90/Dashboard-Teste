import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title(' DASHBOARD DE VENDA :shopping_trolley:')

url = 'https://labdados.com/produtos'
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())

st.metric('Receitas', dados['Preço'].sum())
st.metric('Quantidade de Vendas', dados.shape[0])


st.dataframe(dados)