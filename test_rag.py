from src.rag.agente_rag import AgenteRAG

agente = AgenteRAG()
while True:
    pregunta = input("\nPregunta: ")
    if pregunta.lower() == "salir":
        break
    respuesta = agente.responder(pregunta)
    print("\nRespuesta:\n")
    print(respuesta)