import streamlit as st
import asyncio

st.title("Broken Spinner Example")

with st.spinner():
    await asyncio.sleep(5)
    st.write("done")
