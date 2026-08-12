import logging
from pathlib import Path
from datetime import datetime

def configurar_logger() -> logging.Logger:
    """Configura o logger da aplicação"""

    pasta_logs = Path(__file__).parent.parent.parent / "logs"
    pasta_logs.mkdir(parents=True, exist_ok=True)

    data_atual = datetime.now().strftime("%Y-%m-%d")
    arquivo_log = pasta_logs / f"automacao_{data_atual}.log"
    logger = logging.getLogger("automacao")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(
            arquivo_log,
            encoding="utf-8"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger