import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Configuração Inicial (DEVE ser a primeira linha de comando Streamlit)
st.set_page_config(page_title="MilMatch AI v7.0 - Elite", layout="wide")

# 2. Base de Dados de Regras (Dicionário de Engenharia)
CONCURSOS = {
    "EsPCEx": {"idade_min": 17, "idade_max": 22, "soldo": 7500, "custo_saude": 1200, "taf_barra": 3, "taf_corrida": 2450},
    "AFA": {"idade_min": 17, "idade_max": 22, "soldo": 9500, "custo_saude": 2500, "taf_barra": 2, "taf_corrida": 2400},
    "ITA": {"idade_min": 16, "idade_max": 24, "soldo": 10500, "custo_saude": 3500, "taf_barra": 0, "taf_corrida": 2100},
    "ESA": {"idade_min": 17, "idade_max": 24, "soldo": 5500, "custo_saude": 800, "taf_barra": 3, "taf_corrida": 2450}
}

# 3. Sidebar - Entrada de Dados (O QG de Comando)
st.sidebar.title("🎖️ QG DE COMANDO")
nome = st.sidebar.text_input("Nome de Guerra", "Candidato Alpha")
sexo = st.sidebar.radio("Sexo Biológico", ["Masculino", "Feminino"])
idade = st.sidebar.number_input("Sua Idade", 14, 30, 19)
objetivo = st.sidebar.selectbox("Alvo Estratégico", list(CONCURSOS.keys()))

st.sidebar.divider()
st.sidebar.subheader("🏥 Perfil Clínico")
visao = st.sidebar.checkbox("Alteração Visual (Miopia)?")
cirurgia = st.sidebar.checkbox("Histórico Cirúrgico?")
tattoo = st.sidebar.checkbox("Tatuagem Visível (Pescoço/Rosto)?")

st.sidebar.divider()
st.sidebar.subheader("🏋️ Performance")
corrida = st.sidebar.slider("Corrida (metros)", 1000, 3500, 2100)
barra = st.sidebar.slider("Barras Fixas", 0, 20, 2)
nota_simulado = st.sidebar.slider("Média Teórica (0-10)", 0.0, 10.0, 6.5)

# 4. Lógica de Processamento
regras = CONCURSOS[objetivo]
score_taf = (corrida / regras['taf_corrida'] * 50) + (min(barra/regras['taf_barra'] if regras['taf_barra'] > 0 else 1, 1.0) * 50)
score_final = (score_taf * 0.4) + (nota_simulado * 10 * 0.6)

# 5. Dashboard Principal
st.title(f"🚀 Plano de Invasão: {objetivo}")

if score_final < 50:
    st.warning(f"⚠️ **PATENTE: RECRUTA** - {nome}, intensifique os estudos e o TAF!")
elif score_final < 80:
    st.info(f"⚡ **PATENTE: CADETE** - Você está no caminho certo. Ajuste os detalhes.")
else:
    st.success(f"🔥 **PATENTE: OFICIAL** - Perfil de aprovação detectado!")

tab1, tab2, tab3, tab4 = st.tabs(["🎯 MISSÃO", "🩺 SAÚDE & CUSTOS", "💰 FINANCEIRO", "📑 BUROCRACIA"])

with tab1:
    c1, c2, c3 = st.columns(3)
    c1.metric("Readiness Index", f"{score_final:.1f}%")
    
    gap_corrida = max(regras['taf_corrida'] - corrida, 0)
    c2.metric("Gap Corrida", f"{gap_corrida}m", delta="Faltam" if gap_corrida > 0 else "OK")
    
    gap_barra = max(regras['taf_barra'] - barra, 0)
    c3.metric("Gap Barra", f"{gap_barra} rep", delta="Treinar" if gap_barra > 0 else "OK")

    # Radar Chart
    labels = ['Corrida', 'Barra', 'Teoria', 'Saúde', 'Foco']
    user = [corrida/regras['taf_corrida']*10, (barra/regras['taf_barra']*10 if regras['taf_barra']>0 else 10), nota_simulado, 5 if visao else 10, 9]
    target = [10, 10, 9, 10, 10]
    
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    user += user[:1]; target += target[:1]; angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
    ax.fill(angles, target, color='red', alpha=0.1)
    ax.fill(angles, user, color='blue', alpha=0.5)
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    st.pyplot(fig)

with tab2:
    st.subheader("Análise Médica & Investimento")
    custo = regras['custo_saude']
    if visao: custo += 400
    if cirurgia: custo += 800
    st.write(f"💸 **Estimativa de Gasto com Exames:** R$ {custo},00")
    st.info("Checklist Médico: 🟢 Hemograma | 🟢 ECG | 🟢 Raio-X Torax")

with tab3:
    st.subheader("Projeção de Patrimônio Formado")
    invest = st.slider("Quanto investir do soldo (%)", 5, 50, 15)
    anos = np.arange(1, 13)
    poupanca = [(regras['soldo'] * (invest/100)) * i for i in anos]
    st.line_chart(poupanca)
    st.write(f"Patrimônio ao final de 12 meses como formado: **R$ {poupanca[-1]:,.2f}**")

with tab4:
    st.subheader("Papelada do Candidato")
    st.checkbox("Identidade Original (RG)")
    st.checkbox("Certidão de Nascimento")
    st.checkbox("Histórico Escolar")
    st.checkbox("Título de Eleitor")

st.divider()
st.caption("MilMatch AI v7.0 - Enterprise Edition")
