# 🎖️ MilMatch AI v2.0 - Strategic Military Intelligence
> **Transformando dados brutos em decisões estratégicas de carreira militar.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Database: SQLModel](https://img.shields.io/badge/Database-SQLModel-green.svg)](https://sqlmodel.tiangolo.com/)

O **MilMatch AI** é um ecossistema de inteligência preditiva desenhado para candidatos, escolas militares e consultorias de carreira. O sistema utiliza **Data Science** e **Lógica Multivariada** para cruzar perfis biométricos, sociais e físicos com os rigorosos editais das Forças Armadas (Exército, Marinha e Aeronáutica).

---

## 💼 Visão de Negócio (Value Proposition)

Em um cenário onde a evasão em escolas militares (churn) custa milhões ao Estado, o MilMatch AI atua na **Prevenção e Direcionamento**:
- **Redução de Inscrições Inviáveis:** Filtra candidatos com restrições de saúde (miopia, altura, estado civil) antes do investimento financeiro.
- **Gap Analysis em Tempo Real:** Identifica exatamente quantos metros faltam na corrida ou quantas barras faltam para atingir o índice de aprovação.
- **Projeção de ROI:** Calcula o retorno financeiro vitalício, transformando a "vontade de servir" em um plano de carreira estruturado.

---

## 🧠 Arquitetura do Sistema

O projeto segue os princípios de **Clean Code** e **Modularização Sênior**:

1.  **`database.py`**: Camada de persistência usando **SQLModel**. Gerencia o ciclo de vida dos dados e histórico de performance.
2.  **`ml_engine.py`**: O "Cérebro" do sistema. Implementa lógica de scoring preditivo e clustering de afinidade operacional/técnica.
3.  **`dashboard.py`**: Engine de BI que gera **Gráficos de Radar** comparativos para visualização imediata de competências.
4.  **`milmatch_app.py`**: Orquestrador que integra as camadas em um fluxo contínuo de consultoria.

---

## 🚀 Como Executar o Projeto

### 1. Requisitos Prévios
Certifique-se de ter o Python 3.10 ou superior instalado.

### 2. Instalação
Clone o repositório e instale as dependências:
```bash
git clone [https://github.com/SEU_USUARIO/milmatch-ai.git](https://github.com/SEU_USUARIO/milmatch-ai.git)
cd milmatch-ai
pip install -r requirements.txt
