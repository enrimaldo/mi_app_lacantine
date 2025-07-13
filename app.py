import streamlit as st

st.title("🍽️ Menú del Comedor Escolar")
st.write("Reserva tu almuerzo del día")

menu = {
    "Lunes": "Milanesa con arroz",
    "Martes": "Ensalada de quinoa",
    "Miércoles": "Pollo al horno con papas",
    "Jueves": "Pasta con pollo .--- prueba de cambio",
    "Viernes": "Hamburguesa vegetal"
}

dia = st.selectbox("Selecciona el día:", list(menu.keys()))
st.write(f"Plato del día: **{menu[dia]}**")

if st.button("Reservar"):
    st.success(f"✅ Reserva realizada para el {dia}: {menu[dia]}")
