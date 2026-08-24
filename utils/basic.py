import streamlit as st
import time
def ct(text):
    st.title(text, text_alignment = "center")

def ch(text):
    st.header(text, text_alignment = "center")

def cs(text):
    st.subheader(text, text_alignment = "center")

# Get out!!!
# phs = []

# def set_ph(num):
#     for i in range(num):
#         phs.append(st.empty())

# def tt(text, time, id):
#     phs[id].empty()
#     with phs[id]:
#         ct(text)
#     time.sleep(time)

# def th(text, time, id):
#     phs[id].empty()
#     with phs[id]:
#         ch(text)
#     time.sleep(time)

# def ts(text, time, id):
#     phs[id].empty()
#     with phs[id]:
#         cs(text)
#     time.sleep(time)
