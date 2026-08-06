from pathlib import Path  

def main() -> None:
    """Ponto de entrada da automação."""
    print("Automação iniciada com sucesso!")
    
    #Localizar pasta de entrada de arquivos
    pasta_entrada = Path(__file__).parent / "data" / "input"
    print(f"Pasta de entrada: {pasta_entrada.resolve()}")
    
if __name__ == "__main__":
    main()