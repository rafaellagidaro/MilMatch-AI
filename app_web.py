import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="MilMatch AI v6.0 - Enterprise Suite", layout="wide")

# --- DATABASE DE REGRAS DE NEGÓCIO (EDITAIS) ---
CONCURSOS = {
    "EsPCEx": {"idade_min": 17, "idade_max": 22, "soldo": 7500, "custo_saude": 1200, "rm": "Todas"},
    "AFA": {"idade_min": 17, "idade_max": 22, "soldo": 9500, "custo_saude": 2500, "rm": "Especificas"},
    "ITA": {"idade_min": 16, "idade_max": 24, "soldo": 10500, "custo_saude": 3500, "rm": "Sede SP"},
    "ESA": {"idade_min": 17, "idade_max": 24, "soldo": 5500, "custo_saude": 800, "rm": "Todas"}
}

# --- ESTILIZAÇÃO E CABEÇALHO ---
st.title("🎖️ MilMatch AI v6.0 - Engenharia de Carreira Militar")
st.markdown("### Sistema de Análise de Viabilidade e Prontidão Estratégica")

# --- SIDEBAR: ANAMNESE E DADOS BRUTOS ---
st.sidebar.header("📋 Anamnese & Perfil")
nome = st.sidebar.text_input("Nome Completo", "Recruta Alpha")
sexo = st.sidebar.radio("Sexo Biológico", ["Masculino", "Feminino"])
idade = st.sidebar.number_input("Idade Atual", 14, 30, 19)
objetivo = st.sidebar.selectbox("Instituição Alvo", list(CONCURSOS.keys()))

st.sidebar.divider()
st.sidebar.subheader("🩺 Check-up Clínico Rápido")
miopia = st.sidebar.checkbox("Possui Miopia/Astigmatismo?")
cirurgia = st.sidebar.checkbox("Cirurgias Prévia (Óssea/Cardíaca)?")
alergia = st.sidebar.checkbox("Alergias Restritivas (Medicamentos/Alimentos)?")

st.sidebar.divider()
st.sidebar.subheader("⚡ Performance")
nota_simulado = st.sidebar.slider("Média Geral Simulados", 0.0, 10.0, 7.5)
corrida = st.sidebar.number_input("Corrida 12min (m)", 1000, 3500, 2200)
barra = st.sidebar.number_input("Barras (Repetições)", 0, 30, 4)

# --- LÓGICA DE ENGENHARIA: VALIDAÇÃO DE REQUISITOS ---
regras = CONCURSOS[objetivo]
inaptidão = []
if idade < regras['idade_min'] or idade > regras['idade_max']:
    inaptidão.append(f"Idade fora do limite ({regras['idade_min']}-{regras['idade_max']} anos)")
if miopia and objetivo == "AFA":
    inaptidão.append("Restrição visual severa para Quadros de Voo (CMA)")

# --- DASHBOARD PRINCIPAL ---
tabs = st.tabs(["📊 Prontidão & Radar", "💰 Financeiro & Saúde", "🌍 Geopolítica & RM", "📝 Relatório de Anamnese"])

with tabs[0]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Score de Prontidão")
        readiness = ((nota_simulado/10 * 0.7) + (min(corrida/2450, 1.0) * 0.3)) * 100
        st.metric("Readiness Index", f"{readiness:.2f}%")
        
        if inaptidão:
            for erro in inaptidão:
                st.error(f"⚠ INAPTO: {erro}")
        else:
            st.success("✅ Candidato Elegível ao Edital")

    with col2:
        labels = ['Corrida', 'Barra', 'Teoria', 'Saúde', 'Idade']
        val_user = [corrida/245, barra/2, nota_simulado, 4 if miopia else 10, 10 if not inaptidão else 2]
        val_meta = [10, 10, 9, 10, 10]
        
        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
        val_user += val_user[:1]; val_meta += val_meta[:1]; angles += angles[:1]
        
        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
        ax.fill(angles, val_meta, color='red', alpha=0.1, label='Requisito Edital')
        ax.fill(angles, val_user, color='#1f77b4', alpha=0.5, label='Perfil Candidato')
        ax.set_thetagrids(np.degrees(angles[:-1]), labels)
        st.pyplot(fig)

with tabs[1]:
    st.subheader("💸 Investimento e Retorno (ROI)")
    c1, c2, c3 = st.columns(3)
    
    # Cálculo de custo de saúde estimado
    custo_base = regras['custo_saude']
    if miopia: custo_base += 500  # Adicional de exames oftalmológicos
    if cirurgia: custo_base += 800 # Laudos ortopédicos extras
    
    c1.metric("Custo Inspeção (Est.)", f"R$ {custo_base}")
    c2.metric("Soldo Formado", f"R$ {regras['soldo']}")
    c3.metric("Payback (Meses)", f"{round(custo_base/(regras['soldo']*0.2), 1)}")

    st.write("**Projeção Patrimonial de Longo Prazo (35 anos):**")
    patrimonio = [ (regras['soldo'] * 13 * 0.15) * ((1.10**i - 1) / 0.10) for i in range(1, 36)]
    st.area_chart(patrimonio)

with tabs[2]:
    st.subheader("🗺️ Distribuição de Regiões Militares (RM)")
    rm_selecionada = st.selectbox("Selecione sua Região de Domicílio", [f"{i}ª RM" for i in range(1, 13)])
    
    rm_data = {
        "1ª RM": "RJ/ES - Alta densidade de organizações militares.",
        "2ª RM": "SP - Foco tecnológico e sede do ITA.",
        "3ª RM": "RS - Forte tradição de Cavalaria e Blindados.",
        "11ª RM": "DF/GO - Centro administrativo e comandos especiais."
    }
    st.info(f"**Análise da {rm_selecionada}:** {rm_data.get(rm_selecionada, 'Área de cobertura padrão com juntas de seleção locais.')}")
    
    st.warning("Nota: O deslocamento para as etapas de Inspeção de Saúde e TAF são por conta do candidato.")

with tabs[3]:
    st.subheader("📋 Relatório Consolidado de Anamnese")
    report_data = {
        "Critério": ["Altura/Peso", "Visão", "Histórico Cirúrgico", "Alergias", "Idade"],
        "Status": ["Apto", "Observação" if miopia else "Apto", "Revisão" if cirurgia else "Apto", "Monitorar" if alergia else "Livre", "Dentro do Limite" if not inaptidão else "Crítico"]
    }
    st.table(pd.DataFrame(report_data))
    st.write(f"**Parecer Técnico:** O candidato {nome} apresenta um perfil com foco em {objetivo}. Recomenda-se iniciar o fundo de reserva para exames (R$ {custo_base}) imediatamente.")

st.markdown("---")
st.caption("MilMatch AI v6.0 | Módulo de Engenharia e Consultoria de Carreira")
