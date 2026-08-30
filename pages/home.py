import streamlit as st
left_col,middle_col,right_col = st.columns([1,2,1])
with middle_col:
    st.title("Home",text_alignment="center")
calculator_col,community_shapes_col,make_a_shape_col = st.columns(3)
if "last_page" not in st.session_state:
    st.session_state["last_page"] = 'home'
else:
    st.session_state['last_page'] = 'home'

with calculator_col:
    left_col,middle_col,right_col = st.columns([1,2,1])
    with middle_col:
        if st.button("Calculator"):
            st.switch_page("pages/calculator.py")
        
with community_shapes_col:
    left_col,middle_col,right_col = st.columns([1,2,1])
    with middle_col:
        if st.button("Community Shapes"):
            st.switch_page("pages/community_shapes.py")
        if st.button("Quadratic Solver"):
            st.switch_page("pages/quadratic_solver.py")
with make_a_shape_col:
    left_col,middle_col,right_col = st.columns([1,2,1])
    with middle_col:
        if st.button("Make a Shape"):
            st.switch_page("pages/make_a_shape.py")