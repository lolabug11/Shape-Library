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
    x = st.number_input(f'{default_shapes[shape]["name for the inputs"][0]}',value= 0.0,step= 0.001, format="%.3f",help= "Enter the input to you equation")
    if x >= 2**64-1:
        st.write("Your number is to large enter a new number")
    else:
        result = round(eval(default_shapes[shape]["formula"],{"x":x}),3)
        st.write(f"The {default_shapes[shape]["formula type"]} of your {shape} is {result} units")
elif default_shapes[shape]["number of inputs"] == 2:
    x = st.number_input(f'{default_shapes[shape]["name for the inputs"][0]}',value= 0.0,step= 0.001, format="%.3f",help= "Enter the first input to you equation")
    y = st.number_input(f'{default_shapes[shape]["name for the inputs"][1]}',value= 0.0,step= 0.001, format="%.3f",help= "Enter the second input to you equation",)
    if x >= 2**64-1 or y>= 2**64-1:
        st.write("One of your inputs is to large enter smaller inputs")
    else:
        result = round(eval(default_shapes[shape]["formula"],{"x":x,"y":y}),3)
        st.write(f"The {default_shapes[shape]["formula type"]} of your {shape} is {result} units")
elif default_shapes[shape]["number of inputs"] == 3:
    x = st.number_input(f'{default_shapes[shape]["name for the inputs"][0]}',value= 0.0,step= 0.001, format="%.3f",help= "Enter the first input to you equation")
    y = st.number_input(f'{default_shapes[shape]["name for the inputs"][1]}',value= 0.0,step= 0.001, format="%.3f",help= "Enter the second input to you equation")
    z = st.number_input(f'{default_shapes[shape]["name for the inputs"][2]}',value= 0.0,step= 0.001, format="%.3f",help= "Enter the second input to you equation")
    if x >= 2**64-1 or y>= 2**64-1 or z>=2**64-1:
        st.write("One of your inputs is to large enter smaller inputs")
    else:
        result = round(eval(default_shapes[shape]["formula"],{"x":x,"y":y,z:"z"}),3)
        st.write(f"The {default_shapes[shape]["formula type"]} of your {shape} is {result} units")
    