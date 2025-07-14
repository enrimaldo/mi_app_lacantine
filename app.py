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

st.success("You did it!")
st.error("Error occurred")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("Sidebar Title")
st.sidebar.markdown("This is the sidebar content")

with st.container():
    st.write("This is inside the container")

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)

import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.bar_chart(df)


import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.area_chart(df)

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
df = pd.DataFrame(np.random.randn(500, 3), columns=['x', 'y', 'z'])
chart = alt.Chart(df).mark_circle().encode(    x='x', y='y', size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(chart, use_container_width=True)

import streamlit as st
import graphvizst.graphviz_
chart('''
      digraph {
      Big_shark -> Tuna
      Tuna -> Mackerel
      Mackerel -> Small_fishes
      Small_fishes -> Shrimp
      }
    ''')
