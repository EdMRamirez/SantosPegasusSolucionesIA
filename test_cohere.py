from src.llm.cliente_cohere import ClienteCohere

modelo = ClienteCohere().obtener_modelo()

respuesta = modelo.invoke(
    "Responde únicamente con la palabra: FUNCIONA"
)

print(respuesta.content)