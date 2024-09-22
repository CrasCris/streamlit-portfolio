import streamlit as st
import pandas as pd

def run():
    st.subheader("[Link al Repositorio](https://github.com/CrasCris/Yolo-Nas-FineTuning)")
    st.write("""
    Este proyecto se centra en la detección de imágenes utilizando técnicas avanzadas de modelos SOTA (Modelos
             más actuales y optimizados), para la detección de los elementos de protección personal de los empleados,
             está idea se puede extrapolar tanto para la detección como la clasificación de imagenes estaticas 
             como video en tiempo real.
    """)

    # Incluir una imagen
    st.image("src/img/img1.png", caption="Detección de EPP's de un albañil")

    st.write("""
    Se entrenada un modelo con las imagenes previamente etiquetadas (caso contrarío debes etiquetarlas con heramientas como
             LabelStudio entre otras), para su puesta en producción se despliega como un micro servicio en contenedores docker o podman.
    """)

if __name__ == "__main__":
    run()
