import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuração de Página "Dark Mode" de Engenharia
st.set_page_config(page_title="MilMatch AI v7.0 - Elite", layout="wide", initial_sidebar_state="expanded")

# --- ESTILIZAÇÃO CUSTOMIZADA (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_name_with_html=True)

# --- ENGINE DE DADOS ---
CONCURSOS = {
    "EsPCEx": {"idade_min": 17, "idade_max": 22, "soldo": 7500, "custo_saude": 1200, "taf_barra": 3, "taf_corrida": 2450},
    "AFA": {"idade_min": 17, "idade_max": 22, "soldo": 9500, "custo_saude": 2500, "taf_barra": 2, "taf_corrida": 2400},
    "ITA": {"idade_min": 16, "idade_max": 24, "soldo": 10500, "custo_saude": 3500, "taf_barra": 0, "taf_corrida": 2100},
    "ESA": {"idade_min": 17, "idade_max": 24, "soldo": 5500, "custo_saude": 800, "taf_barra": 3, "taf_corrida": 2450}
}

# --- SIDEBAR INTERATIVA ---
st.sidebar.title("🎖️ QG DE COMANDO")
nome = st.sidebar.text_input("Nome de Guerra", "Candidato Alpha")
sexo = st.sidebar.select_slider("Sexo Biológico", options=["Feminino", "Masculino"])
idade = st.sidebar.number_input("Sua Idade", 14, 30, 19)
objetivo = st.sidebar.selectbox("Alvo Estratégico", list(CONCURSOS.keys()))

st.sidebar.divider()
st.sidebar.subheader("🏥 Perfil Clínico")
anamnese = {
    "Visão (Miopia/Astig)": st.sidebar.toggle("Alteração Visual?"),
    "Cirurgia/Placa": st.sidebar.toggle("Histórico Cirúrgico?"),
    "Cicatriz Aparente": st.sidebar.toggle("Tatuagem/Cicatriz Pescoço?")
}

st.sidebar.divider()
st.sidebar.subheader("🏋️ Performance Física")
corrida = st.sidebar.slider("Corrida (metros)", 1000, 3500, 2100)
barra = st.sidebar.slider("Barras Fixas", 0, 20, 2)
nota_simulado = st.sidebar.slider("Média Teórica (0-10)", 0.0, 10.0, 6.5)

# --- PROCESSAMENTO ---
regras = CONCURSOS[objetivo]
score_taf = (corrida / regras['taf_corrida'] * 50) + (min(barra/regras['taf_barra'], 1.0) * 50)
score_final = (score_taf * 0.4) + (nota_simulado * 10 * 0.6)

# --- CABEÇALHO DINÂMICO ---
st.title(f"Plano de Invasão: {objetivo}")
if score_final < 50:
    st.warning(f"⚠️ **PATENTE: RECRUTA** - Você precisa de mais intensidade, {nome}!")
elif score_final < 80:
    st.info(f"⚡ **PATENTE: CADETE** - No caminho certo. Ajuste a pontaria.")
else:
    st.success(f"🔥 **PATENTE: OFICIAL** - Perfil de aprovação imediata detectado!")

# --- LAYOUT PRINCIPAL (TABS) ---
tab1, tab2, tab3, tab4 = st.tabs(["🎯 MISSÃO", "🩺 SAÚDE & CUSTOS", "💰 PLANO FINANCEIRO", "📑 BUROCRACIA"])

with tab1:
    c1, c2, c3 = st.columns(3)
    c1.metric("Readiness Index", f"{score_final:.1f}%", delta=f"{score_final-50:.1f}")
    
    gap_corrida = max(regras['taf_corrida'] - corrida, 0)
    c2.metric("Gap de Corrida", f"{gap_corrida}m", delta="Faltam" if gap_corrida > 0 else "Meta batida", delta_color="inverse")
    
    gap_barra = max(regras['taf_barra'] - barra, 0)
    c3.metric("Gap de Barras", f"{gap_barra} rep", delta="Treinar" if gap_barra > 0 else "Apto", delta_color="inverse")

    st.divider()
    # Radar Chart
    labels = ['Corrida', 'Barra', 'Teoria', 'Idade', 'Saúde']
    user = [corrida/regras['taf_corrida']*10, barra/regras['taf_barra']*10, nota_simulado, 8, 5 if anamnese['Visão (Miopia/Astig)'] else 10]
    target = [10, 10, 9, 10, 10]
    
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    user += user[:1]; target += target[:1]; angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
    ax.fill(angles, target, color='red', alpha=0.1)
    ax.fill(angles, user, color='#1f77b4', alpha=0.6)
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    st.pyplot(fig)

with tab2:
    st.subheader("Análise de Risco Médico")
    custo_total = regras['custo_saude']
    if anamnese['Visão (Miopia/Astig)']: custo_total += 450
    if anamnese['Cirurgia/Placa']: custo_total += 900
    
    st.write(f"📊 **Investimento Estimado em Exames:** R$ {custo_total},00")
    
    # Checklist de Saúde Interativo
    st.write("**O que checar agora?**")
    st.checkbox("Eletrocardiograma (Esforço)")
    st.checkbox("Audiometria (Essencial para AFA)")
    st.checkbox("Exame de Sangue Completo (Perfil Hormonal)")

with tab3:
    st.subheader("Simulador de Vida: Civil vs Militar")
    soldo = regras['soldo']
    invest = st.slider("Quanto do soldo você vai investir? (%)", 5, 50, 15)
    
    meses = np.arange(1, 13)
    poupanca = [ (soldo * (invest/100)) * i for i in meses]
    
    st.write(f"Em **1 ano** como formado na {objetivo}, você terá guardado **R$ {poupanca[-1]:,.2f}**.")
    st.line_chart(poupanca)
    
    st.info("💡 Lembre-se: Como militar você tem auxílio moradia e saúde gratuita, o que aumenta seu poder de investimento em relação a um civil.")

with tab4:
    st.subheader("Checklist de Documentação (Não seja eliminado por papel!)")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("**Documentos Básicos:**")
        st.checkbox("Identidade Original (Nada de cópia)")
        st.checkbox("Título de Eleitor + Certidão Quitação")
        st.checkbox("Certificado de Alistamento (Homens)")
    with col_b:
        st.write("**Escolaridade:**")
        st.checkbox("Histórico Escolar Original")
        st.checkbox("Certificado de Conclusão")
        st.checkbox("Fotos 3x4 (Leve 10 por segurança)")

st.divider()
st.caption(f"MilMatch AI Elite v7.0 | Gerado em {pd.Timestamp.now().strftime('%d/%m/%Y %H:%M')}")
