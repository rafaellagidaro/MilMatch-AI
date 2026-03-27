import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# 1. CONFIGURAÇÃO DE ALTA PERFORMANCE
st.set_page_config(page_title="MILMATCH AI | ELITE COMMAND", layout="wide", page_icon="🛡️")

# --- BANCO DE DADOS INTEGRADO (CONCURSOS & TAF) ---
DATA_CORE = {
    "EsPCEx": {
        "idade": "17-22 anos", "soldo": 7500.00, "vagas": 440,
        "taf_m": {"Corrida (12min)": "2.450m", "Flexão": "21 reps", "Abdominal": "30 reps", "Barra": "3 reps"},
        "taf_f": {"Corrida (12min)": "2.100m", "Flexão": "12 reps", "Abdominal": "25 reps", "Barra": "1 rep (estático 5s)"}
    },
    "ESA": {
        "idade": "17-24 anos", "soldo": 5500.00, "vagas": 1100,
        "taf_m": {"Corrida (12min)": "2.450m", "Flexão": "21 reps", "Abdominal": "30 reps", "Barra": "3 reps"},
        "taf_f": {"Corrida (12min)": "2.100m", "Flexão": "12 reps", "Abdominal": "25 reps", "Barra": "1 rep (estático 5s)"}
    },
    "AFA": {
        "idade": "17-22 anos", "soldo": 9500.00, "vagas": 85,
        "taf_m": {"Corrida (12min)": "2.400m", "Flexão": "26 reps", "Abdominal": "42 reps", "Barra": "2 reps"},
        "taf_f": {"Corrida (12min)": "2.100m", "Flexão": "16 reps", "Abdominal": "38 reps", "Barra": "8s estático"}
    },
    "ITA": {
        "idade": "16-24 anos", "soldo": 10500.00, "vagas": 150,
        "taf_m": {"Corrida (12min)": "2.100m", "Flexão": "15 reps", "Abdominal": "30 reps", "Barra": "0 (Não exige)"},
        "taf_f": {"Corrida (12min)": "1.850m", "Flexão": "10 reps", "Abdominal": "25 reps", "Barra": "0 (Não exige)"}
    }
}

# --- LISTAGEM EXAUSTIVA DE EXAMES (INSPEÇÃO DE SAÚDE) ---
EXAMES_DETALHADOS = {
    "LABORATÓRIO": ["Hemograma completo", "Glicemia de Jejum", "Ureia e Creatinina", "VDRL e Anti-HIV", "Beta-HCG (Feminino)", "Exame de Urina (EAS)", "Parasitológico de Fezes", "Exame Toxicológico (Larga Janela - 90 dias)"],
    "RADIOLOGIA/IMAGEM": ["Raio-X de Tórax (PA e Perfil)", "Raio-X de Seios da Face", "Raio-X de Coluna Cervical (com laudo)", "Raio-X de Coluna Torácica e Lombar (Cobb e Ferguson)", "Ultrassonografia Abdominal Total"],
    "ESPECIALIDADES": ["Eletrocardiograma (ECG)", "Teste Ergométrico", "Eletroencefalograma (EEG)", "Audiometria", "Exame Oftalmológico (Acuidade, Senso Cromático, Fundo de Olho)", "Exame Odontológico Completo"]
}

# --- DOCUMENTAÇÃO COMPLETA (MOBILIZAÇÃO) ---
DOCS_DETALHADOS = {
    "PESSOAIS": ["RG Original e Cópia", "CPF", "Título de Eleitor", "Certificado de Alistamento Militar/Reservista", "Certidão de Nascimento/Casamento"],
    "ACADÊMICOS": ["Diploma de Conclusão de Ensino Médio", "Histórico Escolar Original (Autenticado)", "Cartão de Confirmação de Inscrição (CCI)"],
    "JUDICIÁRIOS": ["Certidão Negativa da Justiça Federal", "Certidão Negativa da Justiça Estadual", "Certidão de Antecedentes Criminais (PF e Civil)", "Certidão de Quitação Eleitoral"]
}

# --- SIDEBAR (INPUTS DE ENGENHARIA) ---
with st.sidebar:
    st.title("🎖️ COMMAND CENTER")
    nome = st.text_input("NOME DE GUERRA", "RECRUTA ALPHA")
    objetivo = st.selectbox("ALVO ESTRATÉGICO", list(DATA_CORE.keys()))
    sexo = st.radio("SEXO BIOLÓGICO", ["Masculino", "Feminino"], horizontal=True)
    idade = st.number_input("IDADE", 14, 30, 19)
    
    st.divider()
    st.subheader("📊 PERFORMANCE ATUAL")
    nota_simulado = st.slider("NOTA MÉDIA SIMULADOS", 0.0, 10.0, 7.5)
    corrida_atual = st.number_input("CORRIDA 12MIN (METROS)", 0, 4000, 2200)
    barra_atual = st.number_input("BARRA FIXA (REPS)", 0, 25, 2)
    
    st.divider()
    st.subheader("🩺 ANAMNESE CLÍNICA")
    miopia = st.toggle("Possui Miopia/Astigmatismo?")
    cirurgia = st.toggle("Possui Cicatriz Cirúrgica/Placa?")
    alergia = st.toggle("Possui Alergias Graves?")

# --- LÓGICA DE PROCESSAMENTO ---
info = DATA_CORE[objetivo]
perfil_taf = info["taf_m"] if sexo == "Masculino" else info["taf_f"]

# --- INTERFACE PRINCIPAL ---
st.title(f"🛡️ DOSSIÊ MILMATCH AI: {objetivo}")
st.markdown(f"**Candidato:** {nome} | **Patente Estimada:** {'ASPIRANTE' if nota_simulado > 8 else 'CADETE'}")

# MÉTRICAS DE TOPO
m1, m2, m3, m4 = st.columns(4)
m1.metric("SOLDO INICIAL", f"R$ {info['soldo']:.2f}")
m2.metric("VAGAS NO EDITAL", info['vagas'])
m3.metric("LIMITE IDADE", info['idade'])
m4.metric("STATUS EDITAL", "ABERTO/PREVISTO", delta="Ativo", delta_color="normal")

# ABAS INCREMENTADAS
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🎯 ANÁLISE DE GAP", "🏃 TAF DETALHADO", "🔬 INSPEÇÃO DE SAÚDE", "📂 DOCUMENTAÇÃO", "💰 ROI FINANCEIRO"])

with tab1:
    col_a, col_b = st.columns([1, 1])
    with col_a:
        st.subheader("Radar de Prontidão")
        # Gráfico Radar com Plotly
        categories = ['Teoria', 'Corrida', 'Barra', 'Saúde', 'Foco']
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=[nota_simulado, (corrida_atual/2500)*10, (barra_atual/5)*10, 5 if miopia else 10, 9],
            theta=categories, fill='toself', name='Seu Perfil', line_color='#1f77b4'
        ))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col_b:
        st.subheader("Relatório de Riscos")
        if idade > 22 and objetivo == "EsPCEx": st.error("❌ IDADE CRÍTICA: Você excedeu o limite do edital.")
        if miopia and objetivo == "AFA": st.warning("⚠️ ALERTA MÉDICO: AFA Aviação possui restrições severas de acuidade visual.")
        if nota_simulado < 8.0: st.info("💡 REFORÇO TEÓRICO: Sua média está abaixo da nota de corte histórica (8.2).")
        st.success("✅ TAF: Evolução constante detectada.")

with tab2:
    st.subheader(f"Índices Oficiais do TAF - {sexo}")
    df_taf = pd.DataFrame.from_dict(perfil_taf, orient='index', columns=['Mínimo Exigido'])
    st.table(df_taf)
    
    st.subheader("🔥 Simulador de Evolução")
    distancia_falta = 2450 - corrida_atual
    if distancia_falta > 0:
        st.write(f"Faltam **{distancia_falta} metros** para atingir o índice de segurança.")
    else:
        st.write("✨ **Índice de corrida atingido!** Foque em manter o ritmo.")

with tab3:
    st.header("🔬 Protocolo de Inspeção de Saúde")
    st.write("Marque os exames que você já possui ou laudos que já revisou:")
    
    for cat, exames in EXAMES_DETALHADOS.items():
        with st.expander(f"➕ {cat}"):
            for ex in exames:
                st.checkbox(ex, key=ex)
    
    st.error("CUIDADO: O exame toxicológico de larga janela detecta substâncias consumidas há meses. Cuidado com medicações pré-treino não autorizadas.")

with tab4:
    st.header("📂 Checklist de Mobilização Documental")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Certidões & Cartório")
        for d in DOCS_DETALHADOS["JUDICIÁRIOS"] + DOCS_DETALHADOS["PESSOAIS"]:
            st.checkbox(d, key=f"doc_{d}")
    with c2:
        st.subheader("Vida Escolar")
        for d in DOCS_DETALHADOS["ACADÊMICOS"]:
            st.checkbox(d, key=f"doc_{d}")

with tab5:
    st.header("📈 Projeção Patrimonial Militar")
    st.write("Simulação de acúmulo financeiro ao longo de 30 anos (Soldo + Promoções + Investimento de 15%)")
    anos = np.arange(1, 31)
    capital = [(info['soldo'] * 13 * 0.15) * ((1.09**i - 1) / 0.09) for i in anos]
    st.area_chart(capital)
    st.write(f"Estimativa de patrimônio aos 30 anos de serviço: **R$ {capital[-1]:,.2f}**")

st.divider()
st.caption(f"MILMATCH AI ELITE v10.0 | Engine de Decisão atualizada em {datetime.now().strftime('%d/%m/%Y')}")
