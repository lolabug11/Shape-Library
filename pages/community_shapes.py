import streamlit as st
import json
from supabase_client import supabase
st.header("Community Shape")
if "last_page" not in st.session_state:
    st.session_state["last_page"] = 'community'
else:
    st.session_state['last_page'] = 'community'

if "search" not in st.session_state:
    st.session_state["search"] = False

if st.button("Home", key= "Home button Community"):
    st.switch_page('pages/home.py')

search = st.text_input("What shape do you want to search for?",value=" ")

if "custom_shape_name" not in st.session_state:
    st.session_state["custom_shape_name"] = []
if "custom_shape_properties" not in st.session_state:
    st.session_state["custom_shape_properties"] = []

class shape_card:

    def __init__(self,name,formula,formula_with_correct_names,formula_type,number_of_inputs,name_of_inputs,button_key):
        self.name = name
        self.formula = formula
        self.formula_with_correct_names = formula_with_correct_names
        self.formula_type = formula_type
        self.name_of_inputs = name_of_inputs
        self.button_key = button_key
        self.number_of_inputs = number_of_inputs

    def create_card(self):
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.subheader(self.name)
                st.write(f"Type: {self.formula_type}")
                st.write(f"Formula: {self.formula_with_correct_names} ")
                st.write(f"Number of Inputs: {self.number_of_inputs}")
            with col2:
                st.subheader('')
                if st.button("Use this shape",key=self.button_key):
                    st.session_state["custom_shape_name"].append( self.name + " (Custom)")
                    st.session_state["custom_shape_properties"].append( {
                        "formula": self.formula,
                        "number of inputs": self.number_of_inputs,
                        "name for the inputs": self.name_of_inputs,
                        "formula type": self.formula_type
                    })
                    st.session_state["using_custom"] = True
                    st.switch_page('pages/calculator.py',)




    @staticmethod
    def get_correct_names(formula,name_of_inputs: list):
        x_identifyer = False
        number_identifyer = False
        new_formula = ''
        for char in formula:

            if char.lower() == "x":
                x_identifyer = True
            else:
                if x_identifyer:

                    new_formula += f' {name_of_inputs[int(char)-1]}'
                    x_identifyer = False
                else:
                    new_formula += f' {char}'
        return new_formula



response = supabase.table("Shapes").select("*").execute()
number_of_community_shapes = len(response.data)
for shape in range(len(response.data)):
    shape_id = shape
    shape = response.data[shape]
    shape['name'] += " "
    if search in shape['name'] or shape['name'] in search:

        formula_with_correct_names = shape_card.get_correct_names(shape['formula'],list(shape['name_of_inputs']))

        shape_shapecard = shape_card(shape['name'],shape['formula'],formula_with_correct_names,shape['formula_type'],shape['number_of_inputs'],list(shape['name_of_inputs']),f"{shape_id}{shape['name']}" )
        shape_shapecard.create_card()