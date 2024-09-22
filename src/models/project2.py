import streamlit as st

def run():
    st.subheader("[Link al Repositorio](https://github.com/CrasCris/ColombianConstitution-RAG-API/tree/master)")
    st.write("""
    Los grandes modelos de lenguaje(LLM) han abrierto las puertas al analisis y procesamiento del lenguaje natural, por esta razón
    la necesidad de entender documentos largos como la constitución de un pais es fundamental.\n
    
    Para este proyecto se uso una arquitectura RAG donde previamente con un endpoint dedicado a vectorizar nuestros documentos y 
    almacenarlos en una base de datos vectorial, hacemos una busqueda vectorial con cada pregunta que pueda surgir devolviendo los documentos
    posibles con la información, y despues llamando a nuestro LLM en este caso de OpenAI, cabe resaltar el trabajo de definir un buen Prompt
    y el meto de extracción de texto de cada documento, para evitar la alucinacion de nuestro modelo.
    """)

    # Incluir una imagen
    st.image("src/img/img2.png", caption="Ejemplo de la interacción")

    st.write("""
    Para su puesta en producción podemos tanto usar una interfaz como la proporcionada por streamlit o usar una API Rest y crear nuestra propia UX.

    """)


if __name__ == "__main__":
    run()