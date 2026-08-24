import streamlit as st

def ct(text):
    st.title(text, text_alignment = "center")

def ch(text):
    st.header(text, text_alignment = "center")

def cs(text):
    st.subheader(text, text_alignment = "center")

ct("test")
