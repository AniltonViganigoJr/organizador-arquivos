import os
from pathlib import Path
from utils.arquivos import listar_arquivos, mover_arquivo, validar_diretorio

def main() -> None:
    """Ponto de entrada da automação."""
    print("Automação iniciada com sucesso!")

    #Localizar pasta de entrada de arquivos
    pasta_entrada = Path(__file__).parent.parent.parent / "data" / "input"
    print(f"Pasta de entrada: {pasta_entrada.resolve()}")
    
    #Validar se a pasta de entrada existe
    try:
        validar_diretorio(pasta=pasta_entrada)
        print("Pasta validada. Continuando automação...")
    except FileNotFoundError as erro:
        print(f"Erro: {erro}")
        return
    
    #Listar arquivos
    extensao = ".pdf"
    arquivos = listar_arquivos(pasta=pasta_entrada, extensao=extensao)

    if not arquivos:
        print("Não há arquivos para processar.")
        return

    try:
        pasta_saida = Path(__file__).parent.parent.parent / "data" / "processed"
        for arquivo in arquivos:
            print(f"Movendo arquivo: {os.path.basename(arquivo)}")
            mover_arquivo(origem=arquivo, destino=pasta_saida)
    except Exception as erro:
        print(f"Erro: {erro}")
        raise

if __name__ == "__main__":
    main()