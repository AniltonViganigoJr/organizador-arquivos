import shutil
from pathlib import Path

def validar_diretorio(pasta: Path) -> None:
    """Valida se a pasta de entrada existe e é um diretório."""
    if not pasta.exists() or not pasta.is_dir():
        raise FileNotFoundError(f"Pasta de entrada não encontrada: {pasta.resolve()}") 

def listar_arquivos(pasta: Path, extensao: str) -> list[Path]:
    """Lista os arquivos contidos em um diretório."""
    extensao = extensao.lower()
    arquivos = [
        str(arquivo) for arquivo in pasta.iterdir() 
        if arquivo.is_file() and arquivo.suffix.lower() == extensao
        ]
    return arquivos

def mover_arquivo(origem: Path, destino: Path) -> None:
    """Move os arquivos para o diretório especificado"""
    destino.mkdir(parents=True, exist_ok=True)
    shutil.move(str(origem), str(destino))
