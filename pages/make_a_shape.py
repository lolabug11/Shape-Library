import streamlit as st
st.header("Make a Shape")
if "last_page" not in st.session_state:
    st.session_state["last_page"] = 'make'
else:
    st.session_state['last_page'] = 'make'


if st.button("Home"):
    st.switch_page('pages/home.py')
st.write("Work in progress")