import streamlit as st
st.header("Community Shape")
if "last_page" not in st.session_state:
    st.session_state["last_page"] = 'community'
else:
    st.session_state['last_page'] = 'community'


if st.button("Home"):
    st.switch_page('pages/home.py')
st.write("Work in progress")