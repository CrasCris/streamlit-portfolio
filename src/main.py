import streamlit as st
import models.project1 as project1
import models.project2 as project2
import models.project3 as project3
import models.project4 as project4

# Título del portafolio
st.title("Cristian Díaz")
st.write("""
Portafolio de proyectos | Cientifico de Datos | Analista de Datos
""")

# Inicializar el estado de session
if 'selected_project' not in st.session_state:
    st.session_state.selected_project = "project1"  # Mostrar por defecto Visión por computadora

# Sección de la barra lateral
st.sidebar.title("Proyectos")

if st.sidebar.button("Visión por computadora 👁️"):
    st.session_state.selected_project = "project1"
    
if st.sidebar.button("RAG 🤖 Constitución de Colombia"):
    st.session_state.selected_project = "project2"

if st.sidebar.button("Analisis y Predección 📊"):
    st.session_state.selected_project = "project3"

# Mostrar el proyecto seleccionado
if st.session_state.selected_project == "project1":
    st.header("Visión por computadora 👁️")
    project1.run()

elif st.session_state.selected_project == "project2":
    st.header("RAG 🤖 Constitución de Colombia")
    project2.run()

elif st.session_state.selected_project == "project3":
    st.header("Analisis y Predección 📊")
    project3.run()
