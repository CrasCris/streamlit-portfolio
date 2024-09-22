import streamlit as st
import plotly.express as px

def run():
    st.subheader("[Link al Repositorio](https://github.com/CrasCris/TechnicalTest/blob/master/Part1/MachineLearningSkills.ipynb)")
    st.write("""
    Las habilidades para poder entender la información y sus diferentes patrones es muy valiosa en esta era del big data.
    Realizar un analisis exploratorio de manera efectivo es necesario para poder plantear cual sería la mejor forma de solucionar
    las pregunta que srugen alrededor de los mismos en este caso cual es el mejor algoritmo para predecir o clasificar.
             
    \n
    Para esto se utilizan herramientas como PowerBI pensando en la inteligencia de negocion y librerias de Manchine Learning
    como Sklearn y xgboost entre otras, en el proyecto tenemos información de los clientes de una empresa, donde queremos clasificarlos
    que en este caso es la variable churn.
    """)

    st.image("src/img/img3.png", caption="Detalle de la información")


    st.write("""
    Realizamos un analizis exploratorio previo a la definicion y entrenamiento de nuestro modelo para poder clasificar a los clientes \n
    La forma en la que podemos poner en producción nuestro modelo es variada, podemos usar una api con fastapi o podemos crear un
    demonio(bot/automata), que utilice nuestro modelo, guarde los valores de la predicción en base de datos o para automatizar informes
    para la genrencia, equipo de marketing o cualquier area que la necesite.
    """)



if __name__ == "__main__":
    run()