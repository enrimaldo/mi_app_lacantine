# import streamlit as st

# st.title("🍽️ Menú del Comedor Escolar")
# st.write("Reserva tu almuerzo del día")

# menu = {
#     "Lunes": "Voy a cambiar algo",
#     "Martes": "Ensalada de quinoa",
#     "Miércoles": "Pollo al horno con papas",
#     "Jueves": "Pasta con pollo .--- prueba de",
#     "Viernes": "Hamburguesa vegetal"
# }

# dia = st.selectbox("Selecciona el día:", list(menu.keys()))
# st.write(f"Plato del día: **{menu[dia]}**")

# if st.button("Reservar"):
#     st.success(f"✅ Reserva realizada para el {dia}: {menu[dia]}")

import streamlit as st

st.title("This is the app title")
st.header("This is the header")
st.markdown("This is the markdown")
st.subheader("This is the subheader")
st.caption("This is the caption")
st.code("x = 2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# st.image("kid.jpg", caption="A kid playing")
# st.audio("audio.mp3")
# st.video("video.mp4")

st.checkbox('Yes')
st.button('Click Me')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)

st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

st.balloons()  # Celebration balloonsst.progress(10)  # Progress barwith st.spinner('Wait for it...'):    time.sleep(10)  # Simulating a process delay
