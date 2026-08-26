import streamlit as st
import json
from supabase_client import supabase
st.header("Community Shape")
if "last_page" not in st.session_state:
    st.session_state["last_page"] = 'community'
else:
    st.session_state['last_page'] = 'community'


if st.button("Home"):
    st.switch_page('pages/home.py')



class shape_card:

    def __init__(self,name,formula,formula_with_correct_names,formula_type,number_of_inputs):
        self.name = name
        self.formula = formula
        self.formula_with_correct_names = formula_with_correct_names
        self.formula_type = formula_type
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
                if st.button("Use this shape"):
                    st.write('WIP')

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
                    print(name_of_inputs[0])
                    new_formula += f' {name_of_inputs.pop(0)}'
                    x_identifyer = False
                else:
                    new_formula += f' {char}'
        return new_formula


response = supabase.table("Shapes").select("*").execute()
number_of_community_shapes = len(response.data)
for shape in range(len(response.data)):
    shape = response.data[shape]
    formula_with_correct_names = shape_card.get_correct_names(shape['formula'],list(shape['name_of_inputs']))
    shape_shapecard = shape_card(shape['name'],shape['formula'],formula_with_correct_names,shape['formula_type'],shape['number_of_inputs'])
    shape_shapecard.create_card()