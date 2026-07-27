import streamlit as st

from src.rag.agente_rag import AgenteRAG


st.set_page_config(

    page_title="Santos Pegasus Soluciones",

    page_icon="🤖",

    layout="wide"

)

# ------------------------
# CSS
# ------------------------

with open("assets/style.css", encoding="utf8") as css:

    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

# ------------------------
# SIDEBAR
# ------------------------

with st.sidebar:

    st.title("Acerca del asistente")

    st.write(
        """
Este asistente responde únicamente utilizando la documentación oficial de **Santos Pegasus Soluciones**.
"""
    )

    st.markdown(
        """
<div class="info">

Este asistente puede responder preguntas relacionadas con:

- Onboarding

- Ingeniería Back-end

- Ingeniería Front-end

- Arquitectura

- Incidentes y Post-Mortems

</div>
""",
        unsafe_allow_html=True,
    )

    if st.button("🗑 Nueva conversación"):

        st.session_state.chat = []

        st.rerun()

    st.divider()

    st.caption("Santos Pegasus IA v1.0")

# ------------------------
# TITULO
# ------------------------

st.markdown(
    '<p class="titulo">🤖 Santos Pegasus Soluciones</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitulo">Asistente inteligente basado en RAG</p>',
    unsafe_allow_html=True
)

# ------------------------
# AGENTE
# ------------------------

if "agente" not in st.session_state:

    st.session_state.agente = AgenteRAG()

if "chat" not in st.session_state:

    st.session_state.chat = []

# ------------------------
# Mostrar conversación
# ------------------------

for mensaje in st.session_state.chat:

    with st.chat_message(mensaje["role"]):

        st.markdown(mensaje["content"])

# ------------------------
# Entrada
# ------------------------

pregunta = st.chat_input(
    "Escribe tu pregunta..."
)

if pregunta:

    st.session_state.chat.append(

        {
            "role": "user",
            "content": pregunta
        }

    )

    with st.chat_message("user"):

        st.markdown(pregunta)

    with st.chat_message("assistant"):

        with st.spinner("Pensando..."):

            respuesta = st.session_state.agente.responder(
                pregunta
            )

            st.markdown(respuesta)

    st.session_state.chat.append(

        {
            "role": "assistant",
            "content": respuesta
        }

    )