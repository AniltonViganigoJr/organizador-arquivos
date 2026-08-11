import shutil
from pathlib import Path

def validar_diretorio(pasta: Path) -> None:
    """Valida se a pasta de entrada existe e é um diretório."""
    if not pasta.exists() or not pasta.is_dir():
        raise FileNotFoundError(f"Pasta de entrada não encontrada: {pasta.resolve()}") 

def listar_arquivos(pasta: Path) -> list:
    """Lista os arquivos contidos em um diretório."""
    arquivos = [str(arquivo) for arquivo in pasta.iterdir() if arquivo.is_file()]
    return arquivos

def mover_arquivo(origem: Path, destino: Path) -> None:
    """Move os arquivos para o diretório especificado"""
    destino.mkdir(parents=True, exist_ok=True)
    shutil.move(str(origem), str(destino))

def main() -> None:
    """Ponto de entrada da automação."""
    print("Automação iniciada com sucesso!")

    #Localizar pasta de entrada de arquivos
    pasta_entrada = Path(__file__).parent / "data" / "input"
    print(f"Pasta de entrada: {pasta_entrada.resolve()}")
    
    #Validar se a pasta de entrada existe
    try:
        validar_diretorio(pasta=pasta_entrada)
        print("Pasta validada. Continuando automação...")
    except FileNotFoundError as erro:
        print(f"Erro: {erro}")
        raise
    #Listar arquivos
    arquivos = listar_arquivos(pasta=pasta_entrada)

    if not arquivos:
        print("Não há arquivos para processar.")
        return

    try:
        pasta_saida = Path(__file__).parent / "data" / "processed"
        for arquivo in arquivos:
            mover_arquivo(origem=arquivo, destino=pasta_saida)
    except Exception as erro:
        print(f"Erro: {erro}")

    for arquivo in arquivos:
        print(arquivo)

if __name__ == "__main__":
    main()