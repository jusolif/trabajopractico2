import streamlit as st

modulo = st.sidebar.selectbox("Seleccione una sección:",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulo == "Home":
  st.title("Primer Proyecto de Portafolio Profesional")
  st.image("DMC.png",width=150)
  st.image("Python_logo.png",width=300)
  st.subheader("Julio Humberto Solis Flores")
  st.markdown("Especialización en Python for Analytics")
  st.write("2026")
  st.write("Este proyecto está baasado en el archivo BankMarketing.csv,")
  st.write("Para este trabajo se usaron tecnologías como Python, Pandas y Streamlit")
