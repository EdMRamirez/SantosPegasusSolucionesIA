from langchain_community.vectorstores import FAISS
from src.config.configuracion import Configuracion
from src.embeddings.gestor_embeddings import GestorEmbeddings
from src.utils.logger import logger


class VectorStore:
    def crear(self, chunks):
        embeddings = GestorEmbeddings().obtener_embeddings()
        bd = FAISS.from_documents(
            chunks,
            embeddings
        )
        bd.save_local(
            Configuracion.CARPETA_VECTORSTORE
        )
        logger.info("VectorStore creado correctamente")

    def cargar(self):

        embeddings = GestorEmbeddings().obtener_embeddings()
        return FAISS.load_local(
            Configuracion.CARPETA_VECTORSTORE,
            embeddings,
            allow_dangerous_deserialization=True

        )