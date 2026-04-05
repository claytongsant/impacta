import os
from pathlib import Path
from pydantic import BaseModel
from strictyaml import load

# --- CONFIGURAÇÃO DE CAMINHOS ---
current_file_path = Path(__file__).resolve()
PACKAGE_ROOT = current_file_path.parent.parent

ASSETS_PATH = PACKAGE_ROOT / "assets"
CONFIG_FILE_PATH = ASSETS_PATH / "config.yml"

# --- CONTRATOS DE DADOS (SCHEMAS) ---
class ModelConfig(BaseModel):
    trained_model_file: str
    preprocess_model_file: str

class DataSchema(BaseModel):
    quanti_variables: list[str]
    quali_variables: list[str]
    model_variables: list[str]

class Config(BaseModel):
    """Classe mestra que agrupa todas as configurações"""
    data_config: DataSchema
    ml_config: ModelConfig

def create_and_validate_config(cfg_path=CONFIG_FILE_PATH) -> Config:
    if not cfg_path.exists():
        raise OSError(f"Arquivo não encontrado em: {cfg_path}")

    with open(cfg_path, "r") as conf_file:
        # Carrega o YAML completo
        parsed_config = load(conf_file.read()).data
    
    # EXTRAÇÃO DA CHAVE 'data' (Onde estão os campos que o Pydantic espera)
    # Isso resolve o ValidationError de 'Field required'
    data_values = parsed_config['data']
    
    return Config(
        data_config=DataSchema(**data_values),
        ml_config=ModelConfig(**data_values),
    )

# Aqui ESTA INSTÂNCIA É A QUE OS OUTROS ARQUIVOS IMPORTAM
config = create_and_validate_config()

if __name__ == "__main__":
    print("--- Core carregado com sucesso! ---")
    print(config)