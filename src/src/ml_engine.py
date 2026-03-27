import numpy as np

class MLEngine:
    """Motor de análise preditiva e classificação de perfil."""

    @staticmethod
    def calcular_readiness_score(user_perf, meta_prova):
        """Calcula a probabilidade de aprovação (0-100%)."""
        # Normalização dos dados físicos (Cap em 1.0)
        score_corrida = min(user_perf['corrida'] / meta_prova['corrida'], 1.0)
        score_barra = min((user_perf['barra'] + 1) / (meta_prova['barra'] + 1), 1.0)
        
        fisico_ponderado = (score_corrida * 0.7) + (score_barra * 0.3)
        intelectual_ponderado = user_perf['nota_simulado'] / 10
        
        # O Intelectual tem peso 60% na classificação final das armas
        final_score = (intelectual_ponderado * 0.6) + (fisico_ponderado * 0.4)
        return round(final_score * 100, 2)

    @staticmethod
    def definir_cluster_afinidade(preferencias):
        """Classifica o perfil do candidato em clusters militares."""
        p = preferencias
        if p['comando'] >= 7 and p['tecnologia'] <= 5:
            return "COMBATENTE / OPERACIONAL"
        elif p['tecnologia'] >= 8:
            return "TÉCNICO / ENGENHARIA"
        else:
            return "LOGÍSTICO / ADMINISTRATIVO"

    @staticmethod
    def verificar_showstoppers(user_saude, checks_prova):
        """Verifica condições que causam eliminação imediata."""
        alertas = []
        if user_saude['miopia'] > checks_prova['miopia_max']:
            alertas.append(f"Miopia ({user_saude['miopia']}) excede o limite ({checks_prova['miopia_max']})")
        if user_saude['altura'] < checks_prova['altura_min']:
            alertas.append(f"Altura ({user_saude['altura']}cm) abaixo do mínimo ({checks_prova['altura_min']}cm)")
            
        return {"apto": len(alertas) == 0, "detalhes": alertas}
