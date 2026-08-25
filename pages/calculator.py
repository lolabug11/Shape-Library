import streamlit as st
import json
st.header("Calculator")

with open("defaultShapes.json","r") as file:
    default_shapes = json.load(file)

if "last_page" not in st.session_state:
    st.session_state["last_page"] = 'calc'
else:
    st.session_state['last_page'] = 'calc'


if st.button("Home"):
    st.switch_page('pages/home.py')

shape = st.selectbox(
    "Choose a shape",
    [shape for shape in default_shapes]
)

x = None
y = None
z = None
if default_shapes[shape]["number of inputs"] == 1:
    x = st.number_input(f'{default_shapes[shape]["name for the inputs"][0]}',value= 0,help= "Enter the input to you equation")
    result = eval(default_shapes[shape]["formula"],{"x":x})
    st.write(f"The {default_shapes[shape]["formula type"]} of your {shape} is {result} units")
elif default_shapes[shape]["number of inputs"] == 2:
    x = st.number_input(f'{default_shapes[shape]["name for the inputs"][0]}',value= 0,help= "Enter the first input to you equation")
    y = st.number_input(f'{default_shapes[shape]["name for the inputs"][1]}',value= 0,help= "Enter the second input to you equation")
    result = eval(default_shapes[shape]["formula"],{"x":x,"y":y})
    st.write(f"The {default_shapes[shape]["formula type"]} of your {shape} is {result} units")
elif default_shapes[shape]["number of inputs"] == 3:
    x = st.number_input(f'{default_shapes[shape]["name for the inputs"][0]}',value= 0,help= "Enter the first input to you equation")
    y = st.number_input(f'{default_shapes[shape]["name for the inputs"][1]}',value= 0,help= "Enter the second input to you equation")
    z = st.number_input(f'{default_shapes[shape]["name for the inputs"][2]}',value= 0,help= "Enter the second input to you equation")
    result = eval(default_shapes[shape]["formula"],{"x":x,"y":y,"z":z})
    st.write(f"The {default_shapes[shape]["formula type"]} of your {shape} is {result} units")