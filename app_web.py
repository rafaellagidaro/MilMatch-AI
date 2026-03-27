import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importamos a lógica que já criamos (ajuste os caminhos se necessário)
# Para o teste rápido, vou incluir a lógica essencial aqui
st.set_page_config(page_title="MilMatch AI - Consultoria Estratégica", layout="wide")

# --- ESTILIZAÇÃO ---
st.title("🎖️ MilMatch AI v5.0")
st.markdown("### Plataforma de Inteligência Preditiva para Carreiras Militares")
st.sidebar.header("Painel do Candidato")

# --- ENTRADA DE DADOS INTERATIVA ---
nome = st.sidebar.text_input("Nome do Candidato", "Candidato Alpha")
idade = st.sidebar.slider("Idade", 14, 26, 19)
objetivo = st.sidebar.selectbox("Instituição Alvo", ["EsPCEx", "AFA", "ITA", "ESA"])

st.sidebar.subheader("Performance Física (TAF)")
corrida = st.sidebar.number_input("Corrida 12min (metros)", 1000, 3200, 2200)
barra = st.sidebar.number_input("Barras Fixas", 0, 20, 2)

st.sidebar.subheader("Performance Intelectual")
nota_simulado = st.sidebar.slider("Nota Média Simulados", 0.0, 10.0, 7.5)

# --- LÓGICA DE CÁLCULO (O Cérebro da IA) ---
meta_corrida = 2450 if objetivo != "ITA" else 2100
readiness = ( (nota_simulado/10 * 0.6) + (min(corrida/meta_corrida, 1.0) * 0.4) ) * 100

# --- EXIBIÇÃO DE RESULTADOS (O DASHBOARD) ---
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Índice de Prontidão (Readiness)", value=f"{readiness:.2f}%")
    st.write(f"**Análise:** O candidato {nome} está a caminho da aprovação para {objetivo}.")
    
    # Gráfico de Radar em Tempo Real
    labels = ['Corrida', 'Barra', 'Teoria', 'Idade', 'Foco']
    user_stats = [corrida/meta_corrida*10, barra/3*10, nota_simulado, 8, 9]
    target_stats = [10, 10, 9, 7, 10]
    
    # Lógica do Gráfico
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    user_stats += user_stats[:1]
    target_stats += target_stats[:1]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
    ax.fill(angles, target_stats, color='red', alpha=0.1, label='Perfil Ideal')
    ax.fill(angles, user_stats, color='blue', alpha=0.4, label='Seu Perfil')
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    st.pyplot(fig)

with col2:
    st.subheader("💰 Projeção de Carreira (ROI)")
    soldo = 7500.0 if objetivo == "EsPCEx" else 9000.0
    patrimonio = [soldo * 12 * i * 0.15 for i in range(1, 36)] # Simulação simples
    
    st.line_chart(patrimonio)
    st.write("Evolução patrimonial estimada ao longo de 35 anos de serviço.")

st.success("Dados processados com sucesso. Relatório pronto para exportação.")
