import datetime
from database import inicializar_banco, Candidato, engine
from ml_engine import MLEngine
from dashboard import DashboardEngine
from sqlmodel import Session

def main():
    # Inicializa o ambiente
    inicializar_banco()
    
    # Mock de Usuário para Demonstração Executiva
    print("\n[👤 INICIANDO CONSULTORIA]: Candidato Alpha")
    
    dados_user = {
        "nome": "Candidato Alpha",
        "idade": 20,
        "performance": {"corrida": 2200, "barra": 2, "nota_simulado": 8.5},
        "saude": {"miopia": 1.0, "altura": 178},
        "preferencias": {"comando": 9, "tecnologia": 3}
    }

    # Meta de Dados para EsPCEx
    meta_espcex = {
        "sigla": "EsPCEx",
        "corrida": 2450,
        "barra": 3,
        "miopia_max": 3.0,
        "altura_min": 160,
        "soldo_aluno": 1334.0,
        "soldo_formado": 7500.0
    }

    # Execução da IA
    score = MLEngine.calcular_readiness_score(dados_user['performance'], meta_espcex)
    cluster = MLEngine.definir_cluster_afinidade(dados_user['preferencias'])
    saude = MLEngine.verificar_showstoppers(dados_user['saude'], meta_espcex)

    # Persistência
    with Session(engine) as session:
        cand = Candidato(
            nome=dados_user['nome'], 
            idade=dados_user['idade'], 
            data_nascimento=datetime.date(2006, 1, 1),
            altura_cm=dados_user['saude']['altura'],
            escolaridade="Médio"
        )
        session.add(cand)
        session.commit()

    # Relatório Final
    print(f"\n[🏆 RESULTADO IA]: Probabilidade de Sucesso: {score}%")
    print(f"[🔍 CLUSTER]: {cluster}")
    
    if not saude['apto']:
        print(f"[⚠️ ALERTAS]: {saude['detalhes']}")
    
    DashboardEngine.imprimir_roi_financeiro(meta_espcex['sigla'], meta_espcex['soldo_aluno'], meta_espcex['soldo_formado'])
    
    # Gerando Visualização
    labels = ['Corrida', 'Barra', 'Estudo', 'Altura', 'Comando']
    user_radar = [6.5, 5.0, 8.5, 9.5, 9.0]
    meta_radar = [9.0, 8.0, 9.0, 8.0, 10.0]
    DashboardEngine.gerar_radar_chart(user_radar, meta_radar, labels)

if __name__ == "__main__":
    main()
