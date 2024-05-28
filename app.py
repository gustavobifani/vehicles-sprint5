import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

# cabeçalho do nosso site
st.header('Bem vindo! Aqui neste site você terá acesso as informações de distribuição da quantidade de carros disponíveis no nosso conjunto com base em sua distância percorrida. Além disso, poderá observar de maneira gráfica como isso influencia no preço de cada um deles.')

# DataViewer
st.write('Este é o cabeçalho do conjunto de dados com os veículos que compõem as análises do nosso site')
st.dataframe(car_data.head(10))

# Criando nossa caixa de seleção
build_histogram = st.checkbox('Criar um histograma')
build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_histogram:
    # identificando e detalhando a escolha do usuário na caixa de seleção - histograma
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros, mostrando a distribuição da quantidade de carros de acordo com as informações do odômetro')
         
    # criando um histograma com base nas informações de distância total percorrida pelos veículos
    fig_hist = px.histogram(car_data, x="odometer")
     
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:
    # identificando e detalhando a escolha do usuário na caixa de seleção - gráfico de dispersão
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros, mostrando a correlação entre os preços dos veículos e a distância informada no odômetro')
         
    # criando um gráfico de dispersão que correlaciona o preço dos veículos com a distância informada no odômetro
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
     
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)    
