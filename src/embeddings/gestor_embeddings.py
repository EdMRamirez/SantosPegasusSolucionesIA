from langchain_cohere import CohereEmbeddings
from src.config.configuracion import Configuracion


class GestorEmbeddings:
    def obtener_embeddings(self):
        return CohereEmbeddings(
            cohere_api_key=Configuracion.COHERE_API_KEY,
            model="embed-multilingual-v3.0"

        )