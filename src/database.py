from sqlmodel import Field, SQLModel, create_engine, Session, select
from typing import Optional, List
import datetime

# --- DEFINIÇÃO DAS TABELAS (MODELOS) ---

class Candidato(SQLModel, table=True):
    """Representa o perfil biométrico e social do usuário."""
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    idade: int
    data_nascimento: datetime.date
    casado: bool = False
    dependentes: bool = False
    escolaridade: str # "Médio", "Superior"
    
    # Biometria
    miopia_grau: float = 0.0
    altura_cm: int
    possui_daltonismo: bool = False
    
    data_registro: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class PerformanceTAF(SQLModel, table=True):
    """Histórico de evolução física para Gap Analysis."""
    id: Optional[int] = Field(default=None, primary_key=True)
    candidato_id: int = Field(foreign_key="candidato.id")
    data_teste: datetime.date = Field(default_factory=datetime.date.today)
    
    corrida_12min_m: int
    barra_fixa: int
    flexao_braco: int
    abdominal_1min: int

class InstituicaoMilitar(SQLModel, table=True):
    """Base de dados estática com requisitos das Forças."""
    id: Optional[int] = Field(default=None, primary_key=True)
    sigla: str # Ex: AMAN, ITA, AFA, ESA
    forca: str # Exército, Marinha, Aeronáutica
    idade_min: int
    idade_max: int
    permite_casado: bool
    soldo_aluno: float
    soldo_formado: float
    meta_corrida: int
    meta_barra: int

# --- CONFIGURAÇÃO DO BANCO ---

sqlite_file_name = "data/milmatch_ai_v2.db" # Salva dentro da pasta data
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=False)

def inicializar_banco():
    """Cria o banco de dados e as tabelas se não existirem."""
    import os
    # Garante que a pasta 'data' existe
    if not os.path.exists('data'):
        os.makedirs('data')
        
    SQLModel.metadata.create_all(engine)
    print(f"[⚙️ DATABASE]: Sistema de arquivos de dados inicializado em {sqlite_file_name}")

if __name__ == "__main__":
    inicializar_banco()
