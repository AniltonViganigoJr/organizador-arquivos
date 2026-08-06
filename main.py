from pathlib import Path

def validar_diretorio(pasta: Path) -> None:
    """Valida se a pasta de entrada existe e é um diretório."""
    if not pasta.exists() or not pasta.is_dir():
        raise FileNotFoundError(f"Pasta de entrada não encontrada: {pasta.resolve()}") 
    
def main() -> None:
    """Ponto de entrada da automação."""
    print("Automação iniciada com sucesso!")

    #Localizar pasta de entrada de arquivos
    pasta_entrada = Path(__file__).parent / "data" / "input"
    print(f"Pasta de entrada: {pasta_entrada.resolve()}")
    
    #Validar se a pasta de entrada existe
    try:
        validar_diretorio(pasta_entrada)
        print("Pasta validada. Continuando automação...")
    except FileNotFoundError as erro:
        print(f"Erro: {erro}")
        raise

if __name__ == "__main__":
    main()