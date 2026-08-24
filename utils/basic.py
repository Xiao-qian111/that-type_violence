import streamlit as st
import time
def ct(text):
    st.title(text, text_alignment = "center")

def ch(text):
    st.header(text, text_alignment = "center")

def cs(text):
    st.subheader(text, text_alignment = "center")

def tt(text, time):
    ct(text)
    time.sleap(time)

def th(text, time):
    ch(text)
    time.sleap(time)

def ts(text, time):
    cs(text)
    time.sleap(time)
