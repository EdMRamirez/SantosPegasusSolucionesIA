from pathlib import Path

from dotenv import load_dotenv
import os


# Ruta de la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parents[2]

# Cargar variables de entorno
load_dotenv(BASE_DIR / ".env")


class Configuracion:
    """
    Centraliza la configuración del proyecto.
    """

    COHERE_API_KEY = os.getenv("COHERE_API_KEY")

    CARPETA_DOCUMENTOS = BASE_DIR / "documentos"

    CARPETA_VECTORSTORE = BASE_DIR / "vectorstore"