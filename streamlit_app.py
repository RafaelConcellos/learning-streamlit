import streamlit as st

st.title("Hell yaa World!")
st.header("Let's start it", divider="green")

with st.sidebar:
    st.header("About")
    st.markdown('first time doing it')

col1, col2 = st.columns(2)
with col1:
    x = st.slider("Choose your destiny", 1, 10)
with col2:
    st.write("flawless victory: ", x)


import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df