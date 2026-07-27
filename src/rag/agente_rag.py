from src.embeddings.vectorstore import VectorStore
from src.llm.cliente_cohere import ClienteCohere

class AgenteRAG:
    def __init__(self):
        self.modelo = ClienteCohere().obtener_modelo()
        self.vectorstore = VectorStore().cargar()

    def responder(self, pregunta: str):
        documentos = self.vectorstore.similarity_search(
            pregunta,
            k=4
        )
        contexto = "\n\n".join(
            documento.page_content
            for documento in documentos
        )

        prompt = f"""
                    Eres un asistente de inteligencia artificial de Santos Pegasus Soluciones.

                    Responde únicamente utilizando la información del contexto.

                    Si la respuesta no está en el contexto responde exactamente:

                    No encontré información sobre esa pregunta en la documentación de Santos Pegasus Soluciones.

                    Contexto:  
                    {contexto}

                    Pregunta:
                    {pregunta}

                    Respuesta:
                """

        respuesta = self.modelo.invoke(prompt)
        return respuesta.content