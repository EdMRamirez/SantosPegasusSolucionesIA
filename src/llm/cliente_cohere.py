from langchain_cohere import ChatCohere

from src.config.configuracion import Configuracion


class ClienteCohere:
    def __init__(self):

        self.modelo = ChatCohere(
            cohere_api_key=Configuracion.COHERE_API_KEY,
            model="command-a-03-2025"
        )

    def obtener_modelo(self):
        return self.modelo