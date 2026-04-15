import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# conexão com banco
engine = create_engine('postgresql://admin:admin@localhost:5432/iot')

# função pra carregar dados
def load_data(view):
    return pd.read_sql(f"SELECT * FROM {view}", engine)

# título
st.title('📡 Dashboard IoT - Temperaturas')

# gráfico 1
st.header('Média de Temperatura por Dispositivo')
df1 = load_data('avg_temp_por_dispositivo')
fig1 = px.bar(df1, x='device_id', y='avg_temp')
st.plotly_chart(fig1)

# gráfico 2
st.header('Leituras por Hora')
df2 = load_data('leituras_por_hora')
fig2 = px.line(df2, x='hora', y='contagem')
st.plotly_chart(fig2)

# gráfico 3
st.header('Temperatura Máx e Mín por Dia')
df3 = load_data('temp_max_min_por_dia')
fig3 = px.line(df3, x='data', y=['temp_max', 'temp_min'])
st.plotly_chart(fig3)