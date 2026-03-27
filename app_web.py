import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. Configuração de Alta Fidelidade
st.set_page_config(page_title="MILMATCH AI | FULL MANUAL", layout="wide", page_icon="🛡️")

# --- BANCO DE DADOS DE EXAMES (DETALHADO) ---
EXAMES_LISTA = {
    "Laboratoriais": ["Hemograma Completo", "Glicemia de Jejum", "Ureia e Creatinina", "VDRL (Sífilis)", "Beta-HCG (Feminino)", "Exame de Urina (EAS)", "Exame de Fezes (Parasitológico)"],
    "Radiológicos": ["Raio-X do Tórax (PA e Perfil)", "Raio-X de Coluna Cervical/Torácica/Lombar", "Raio-X de Seios da Face"],
    "Cardiológicos/Outros": ["Eletrocardiograma (ECG)", "Teste Ergométrico", "Eletroencefalograma (EEG)", "Audiometria", "Exame Oftalmológico Completo", "Exame Odontológico"],
    "Especiais": ["Exame Toxicológico (Larga Janela)", "Exame Psicotécnico"]
}

# --- BANCO DE DADOS DE DOCUMENTOS ---
DOCUMENTOS_LISTA = {
    "Pessoais": ["Identidade (RG) Original", "CPF", "Título de Eleitor", "Certidão de Nascimento/Casamento", "Certificado de Alistamento Militar/Reservista"],
    "Escolares": ["Diploma de Conclusão", "Histórico Escolar Original (Autenticado)", "Certificado de Proficiência (se houver)"],
    "Certidões": ["Certidão Negativa da Justiça Federal", "Certidão Negativa da Justiça Estadual", "Certidão de Antecedentes Criminais (Polícia Federal)", "Certidão de Quitação Eleitoral"]
}

# --- ÍNDICES TAF (EXEMPLO ESPCEX) ---
TAF_ESPEC = {
    "Masculino": {"Corrida (12min)": "2.450m", "Flexão de Braço": "21 reps", "Abdominal": "30 reps", "Barra": "3 reps"},
    "Feminino": {"Corrida (12min)": "2.100m", "Flexão de Braço": "12 reps", "Abdominal": "25 reps", "Barra": "1 rep (estático 5s)"}
}

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ CONFIGURAÇÃO")
    nome = st.text_input("NOME COMPLETO", "RECRUTA")
    objetivo = st.selectbox("ALVO", ["EsPCEx", "AFA", "ITA", "ESA"])
    sexo = st.radio("SEXO BIOLÓGICO", ["Masculino", "Feminino"], horizontal=True)
    st.divider()
    nota = st.slider("NOTA SIMULADO", 0.0, 10.0, 7.5)
    corrida = st.number_input("CORRIDA ATUAL (METROS)", 0, 4000, 2200)

# --- TÍTULO ---
st.title(f"🎖️ MILMATCH AI v9.0: DOSSIÊ COMPLETO - {objetivo}")

# --- TABS ESTRATÉGICAS ---
t1, t2, t3, t4 = st.tabs(["📊 ANÁLISE DE PRONTIDÃO", "🩺 INSPEÇÃO DE SAÚDE", "🏃 TAF (FISICO)", "📑 CHECKLIST DOCUMENTAL"])

with t1:
    # Mostra o Readiness Score
    readiness = (nota * 10) * 0.7 + (min(corrida/2450, 1.0) * 30)
    st.metric("ÍNDICE DE PRONTIDÃO ESTRATÉGICA", f"{readiness:.1f}%")
    st.progress(readiness/100)
    st.write("---")
    st.subheader("Radar de Competências")
    # Gráfico Radar (Simplificado para o exemplo)
    fig = go.Figure(go.Scatterpolar(r=[nota, corrida/300, 8, 9, 7], theta=['Teoria', 'Corrida', 'Saúde', 'Foco', 'Disciplina'], fill='toself'))
    st.plotly_chart(fig)

with t2:
    st.header("🔬 Relação Completa de Exames")
    st.warning("Nota: A validade dos exames geralmente é de 90 dias antes da data da inspeção.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🧪 Laboratório e Sangue")
        for item in EXAMES_LISTA["Laboratoriais"]:
            st.checkbox(item, key=f"lab_{item}")
            
    with col2:
        st.subheader("📸 Imagem e Coração")
        for item in EXAMES_LISTA["Radiológicos"] + EXAMES_LISTA["Cardiológicos/Outros"]:
            st.checkbox(item, key=f"img_{item}")
            
    st.subheader("⚠️ Exames de 'Janela Larga'")
    st.info(f"O **Exame Toxicológico** para o {objetivo} deve detectar substâncias em um período mínimo de 90 dias. Evite qualquer medicamento sem prescrição.")

with t3:
    st.header("🏋️ Treinamento Físico de Edital")
    st.write(f"Índices mínimos para o perfil **{sexo}**:")
    
    df_taf = pd.DataFrame.from_dict(TAF_ESPEC[sexo], orient='index', columns=['Índice Mínimo'])
    st.table(df_taf)
    
    st.subheader("Plano de Treino Sugerido")
    st.code("""
    - Segunda: Corrida Intervalada (Tiros de 400m)
    - Terça: Fortalecimento de Core (Abdominais e Lombar)
    - Quarta: Volume de Corrida (5km a 7km ritmo leve)
    - Quinta: Técnica de Barra Fixa e Flexão
    - Sexta: Simulado TAF (Cronometrado)
    """, language="markdown")

with t4:
    st.header("📂 Mobilização de Documentos")
    st.error("Documentos rasurados ou vencidos causam eliminação imediata na etapa de Heteroidentificação/Validação.")
    
    for categoria, docs in DOCUMENTOS_LISTA.items():
        with st.expander(f"📌 {categoria}"):
            for d in docs:
                st.write(f"• {d}")
                
    st.subheader("💡 Dica de Engenharia")
    st.write("Digitalize todos estes documentos em PDF e salve na nuvem (Google Drive/iCloud). No dia da apresentação, leve tudo em uma pasta sanfonada organizada por ordem de edital.")

st.divider()
st.caption("MILMATCH AI v9.0 | ENGINE DE DADOS INTEGRADA")
