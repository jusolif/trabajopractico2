import streamlit as st
import pandas as pd
modulo = st.sidebar.selectbox("Seleccione una sección:",["Home","Carga del dataset","EDA"])

if modulo == "Home":
  st.title("Primer Proyecto de Portafolio Profesional")
  st.image("DMC.png",width=150)
  st.image("Python_logo.png",width=300)
  st.subheader("Julio Humberto Solis Flores")
  st.markdown("Especialización en Python for Analytics")
  st.write("2026")
  st.write("Este proyecto está basado en el archivo BankMarketing.csv, correspondiente a una institución financiera que buscan entender los factores que influyen en la aceptación de sus campañas de marketing.")
  st.write("Para este trabajo se usaron tecnologías como Python, Pandas y Streamlit")

elif modulo == "Carga del dataset":

    st.header("Carga del dataset")

    st.markdown("""En este módulo se realiza la carga del archivo BankMarketing.csv
    para posteriormente efectuar el Análisis Exploratorio de Datos (EDA).""")

    archivo = st.file_uploader("Seleccione el archivo BankMarketing.csv",type=["csv"])

    if archivo is not None:

        df = pd.read_csv(archivo)

        st.success("Archivo cargado correctamente.")

        st.subheader("Vista previa del dataset")

        st.dataframe(df.head())

        filas, columnas = df.shape

        st.subheader("Dimensiones del dataset")

        st.write(f"Filas: {filas}")
        st.write(f"Columnas: {columnas}")

    else:

        st.warning("Debe cargar el archivo BankMarketing.csv para continuar.")
