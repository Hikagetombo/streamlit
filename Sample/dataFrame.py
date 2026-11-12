import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit DataFrame Example')
st.write("Here's our first attempt example using the Pandas Styler object to highlight some elements:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

st.write("Streamlit also has a method for static table generation: st.table()")
dataframe2 = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe2)
