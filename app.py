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


elif opcion == "Carga del dataset":

    st.title("Carga del dataset")

    st.write(
        "Carga el archivo BankMarketing.csv para comenzar "
        "el análisis exploratorio de datos."
    )

    archivo = st.file_uploader(
        "Selecciona el archivo CSV",
        type=["csv"]
    )

    if archivo is None:

        st.warning(
            "Por favor, carga el archivo BankMarketing.csv "
            "para continuar."
        )

    else:

        try:

            df = pd.read_csv(archivo)

            st.success("Dataset cargado correctamente.")

            # Dimensiones
            filas, columnas = df.shape

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Número de filas", filas)

            with col2:
                st.metric("Número de columnas", columnas)

            # Vista previa
            st.subheader("Vista previa del dataset")

            st.dataframe(df.head())

        except Exception as e:

            st.error(
                f"No fue posible cargar el archivo: {e}"
            )

