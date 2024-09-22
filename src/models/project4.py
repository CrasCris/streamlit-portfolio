import streamlit as st
import plotly.express as px

def run():
    '''
    Sobre Mi
    '''
    st.subheader("Visualización Interactiva")

    # Ejemplo: Gráfico interactivo con Plotly
    df = px.data.iris()  # Dataset iris
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="Gráfico interactivo de Iris")

    # Mostrar gráfico interactivo
    st.plotly_chart(fig)