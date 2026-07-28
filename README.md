# 🤖 Agente Inteligente RAG - Santos Pegasus Soluciones

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un Agente Inteligente basado en la técnica **Retrieval-Augmented Generation (RAG)**, capaz de responder preguntas utilizando exclusivamente la documentación interna de la empresa **Santos Pegasus Soluciones**.

El sistema procesa documentos PDF oficiales de la empresa, genera embeddings mediante Cohere, almacena la información en un índice vectorial FAISS y utiliza un modelo de lenguaje para generar respuestas fundamentadas en el contenido recuperado.

El proyecto fue desarrollado en Python utilizando LangChain y cuenta con una interfaz web creada con Streamlit.

---

# Objetivo

Desarrollar un asistente inteligente que permita consultar información interna de Santos Pegasus Soluciones de forma rápida y precisa, evitando respuestas inventadas y utilizando únicamente la documentación proporcionada.

---

# Documentación utilizada

El agente obtiene sus respuestas a partir de los siguientes documentos:

- Manual de Onboarding para Nuevos Desarrolladores
- Guía Oficial de Ingeniería Back-end
- Guía Oficial de Ingeniería Front-end
- Arquitectura de Microservicios y Mapa de Dominios
- Protocolo de Respuesta a Incidentes y Post-Mortems

---

# Arquitectura de la Solución

```text
                     Usuario
                        │
                        ▼
              Interfaz Streamlit
                        │
                        ▼
                 Agente Inteligente
                        │
                        ▼
                Recuperación (RAG)
                        │
                        ▼                               
                    Modelo Cohere   
                        |
                        ▼               
                    Base Vectorial FAISS
                        │
                        ▼
                    Embeddings Cohere
                        │
                        ▼
                    Documentos PDF
```

---

# Tecnologías utilizadas

- Python 3
- Cohere
- LangChain
- FAISS
- Streamlit
- Git
- GitHub
- Oracle Cloud Infrastructure (OCI)

---

# Estructura del Proyecto

```text
SantosPegasusSoluciones/
│
├── app.py
├── main_ingestion.py
├── README.md
├── requirements.txt
├── .env.example
├── documentos/
├── vectorstore/
├── assets/
│
└── src/
    ├── config/
    ├── embeddings/
    ├── ingestion/
    ├── llm/
    ├── prompts/
    ├── rag/
    └── utils/
```

---

# Instalación

## Clonar el repositorio

```bash
git clone git@github.com:EdMRamirez/SantosPegasusSolucionesIA.git
```

## Crear entorno virtual

```bash
python -m venv .venv
```

## Activar entorno

Windows

```bash
.venv\Scripts\activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Crear archivo .env

```env
COHERE_API_KEY=TU_API_KEY
```

## Procesar los documentos

```bash
python main_ingestion.py
```

## Ejecutar la aplicación

```bash
streamlit run app.py
```

---

# Ejemplos de preguntas

- ¿Cómo es el proceso de onboarding para nuevos desarrolladores?
- ¿Qué tecnologías utiliza el equipo Back-end?
- ¿Cómo se gestionan los incidentes?
- ¿Cuál es la arquitectura de microservicios?
- ¿Qué responsabilidades tiene un desarrollador Front-end?

---

# Ejemplo de respuesta

**Pregunta**

> ¿Cómo es el proceso de onboarding?

**Respuesta**

> El proceso de onboarding incluye la configuración del entorno de desarrollo, acceso a los repositorios, revisión de la arquitectura del proyecto, asignación de un mentor y familiarización con las buenas prácticas de desarrollo establecidas por Santos Pegasus Soluciones.

---

# Características

- Respuestas basadas únicamente en la documentación.
- Procesamiento de documentos PDF.
- Búsqueda semántica mediante FAISS.
- Embeddings con Cohere.
- Interfaz web intuitiva con Streamlit.
- Arquitectura modular.
- Fácil de desplegar en Oracle Cloud.

---
# Anexo
<img width="1271" height="600" alt="image" src="https://github.com/user-attachments/assets/52f6a7f9-4707-4ac6-93da-01afd0730dc1" />
<img width="1250" height="620" alt="image" src="https://github.com/user-attachments/assets/abccf37d-32bc-4bf3-8b92-fcba3ad82196" />



# Autor

**Eddy Daniel Mujica Ramirez**

Alura Latam

Challenge Alura Agente
