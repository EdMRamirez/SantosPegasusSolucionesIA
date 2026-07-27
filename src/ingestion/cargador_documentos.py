from langchain_community.document_loaders import PyPDFDirectoryLoader
from src.config.configuracion import Configuracion
from src.utils.logger import logger

class CargadorDocumentos:
    def cargar(self):
        loader = PyPDFDirectoryLoader(
            Configuracion.CARPETA_DOCUMENTOS
        )
        documentos = loader.load()
        logger.info(f"Documentos cargados: {len(documentos)}")
        return documentos