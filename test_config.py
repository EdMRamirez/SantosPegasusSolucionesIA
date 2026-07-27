from src.config.configuracion import Configuracion

print("API encontrada:")
print(Configuracion.COHERE_API_KEY)

print()

print("Documentos:")
print(Configuracion.CARPETA_DOCUMENTOS)

print()

print("VectorStore:")
print(Configuracion.CARPETA_VECTORSTORE)