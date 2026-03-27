import matplotlib.pyplot as plt
import numpy as np

class DashboardEngine:
    """Gera dashboards visuais de alta fidelidade."""

    @staticmethod
    def gerar_radar_chart(usuario_dados, meta_dados, labels, filename="radar_perfil.png"):
        """Gera um gráfico de radar comparativo."""
        num_vars = len(labels)
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        
        # Fechamento do gráfico
        usuario_dados += usuario_dados[:1]
        meta_dados += meta_dados[:1]
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
        
        # Plot Meta (Aprovados)
        ax.fill(angles, meta_dados, color='red', alpha=0.1, label='Perfil Ideal')
        ax.plot(angles, meta_dados, color='red', linewidth=1, linestyle='--')
        
        # Plot Usuário
        ax.fill(angles, usuario_dados, color='#1f77b4', alpha=0.5, label='Seu Perfil')
        ax.plot(angles, usuario_dados, color='#1f77b4', linewidth=2)

        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)
        ax.set_thetagrids(np.degrees(angles[:-1]), labels)
        
        plt.title("MAPA DE COMPETÊNCIAS MILITARES", size=16, y=1.1)
        plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
        
        # Salva o gráfico para o repositório
        plt.savefig(filename)
        print(f"[📊 DASHBOARD]: Gráfico salvo como {filename}")
        plt.show()

    @staticmethod
    def imprimir_roi_financeiro(nome_prova, soldo_aluno, soldo_formado):
        """Exibe o Business Case de carreira."""
        investimento = 3500.00 # Custo médio estudo/enxoval
        receita_10_anos = (soldo_aluno * 13 * 2) + (soldo_formado * 13 * 8)
        
        print("\n" + "-"*50)
        print(f"💰 ANÁLISE DE ROI: {nome_prova}")
        print("-"*50)
        print(f"Investimento Inicial Estimado: R$ {investimento:,.2f}")
        print(f"Retorno Bruto (10 anos): R$ {receita_10_anos:,.2f}")
        print(f"Payback: O investimento se paga no 3º mês de formação.")
        print("-" * 50)
