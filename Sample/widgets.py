import streamlit as st
import numpy as np
import pandas as pd

# slider
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# text input
st.text_input("Your name", key="name")

# You can access the value at any point with:
name = st.session_state.name
st.write(f"Hello, {name}!")

# checkbox
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    #st.line_chart(chart_data)
    chart_data

# selectbox
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
     df['first column']
)
st.write('You selected:', option)