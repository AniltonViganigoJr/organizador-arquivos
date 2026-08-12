from pathlib import Path
from utils.arquivos import listar_arquivos, mover_arquivo, validar_diretorio
from utils.logger import configurar_logger

def main() -> None:
    """Ponto de entrada da automação."""
    
    logger = configurar_logger()
    logger.info("Automação iniciada com sucesso!")

    #Localizar pasta de entrada de arquivos
    pasta_entrada = Path(__file__).parent.parent.parent / "data" / "input"
    logger.info(f"Pasta de entrada: %s", pasta_entrada.resolve)
    
    #Validar se a pasta de entrada existe
    try:
        validar_diretorio(pasta=pasta_entrada)
        logger.info("Pasta de entrada validada.")
    except FileNotFoundError as erro:
        logger.error("Pasta de entrada não encontrada: %s", erro)
        return
    
    #Listar arquivos
    extensao = ".pdf"
    arquivos = listar_arquivos(pasta=pasta_entrada, extensao=extensao)

    if not arquivos:
        logger.info("Não há arquivos para processar.")
        return

    logger.info("Arquivos encontrados: %s", len(arquivos))
    try:
        pasta_saida = Path(__file__).parent.parent.parent / "data" / "processed"
        for arquivo in arquivos:
            logger.info("Movendo arquivo: %s", arquivo.name)
            mover_arquivo(origem=arquivo, destino=pasta_saida)
            logger.info("Arquivo movido com sucesso: %s", arquivo.name)
    except Exception as erro:
        logger.error("Erro ao mover o arquivo")
        raise

if __name__ == "__main__":
    main()