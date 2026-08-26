import streamlit as st
import json
from supabase_client import supabase


def test_formula(formula):

    allowed_chars = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "x",
        "(", ")",
        ".",
        "*", "/", "+", "-", " "
    ]

    # Check length
    if len(formula) > 100:
        return False

    # Check sqrt usage
    while "sqrt" in formula:
        position = formula.find("sqrt")

        # Make sure sqrt is followed by (
        if position + 4 >= len(formula) or formula[position + 4] != "(":
            return False

        # Remove this sqrt so we can check the rest
        formula = formula[:position] + formula[position + 4:]

    # Check remaining characters
    for char in formula:
        if char not in allowed_chars:
            return False

    return True
def reset_form():
    st.session_state["name"] = ""
    st.session_state["formula_type"] = "Area"
    st.session_state["formula"] = ""
    st.session_state["number_of_inputs"] = 1
st.header("Make a Shape")
if "last_page" not in st.session_state:
    st.session_state["last_page"] = 'make'
else:
    st.session_state['last_page'] = 'make'
if "name" not in st.session_state:
    st.session_state["name"] = ""
if "formula_type" not in st.session_state:
    st.session_state["formula_type"] = "Area"
if "formula" not in st.session_state:
    st.session_state["formula"] = ""
if "number_of_inputs" not in st.session_state:
    st.session_state["number_of_inputs"] = 1
if "reset_form" not in st.session_state:
    st.session_state["reset_form"] = False
if st.button("Home", key= "Home button Make"):
    st.switch_page('pages/home.py')



if st.session_state["reset_form"]:
    reset_form()
    st.session_state["reset_form"] = False


number_of_inputs = st.number_input(f"How many inputs does your formula have? (Read the help!)",help= "Like for Base * height this would be 2. One for base, and one for height.",value=1,min_value= 1,key= 'number_of_inputs',max_value=10)
with st.form("shape_creation_form"):
    shape_name = st.text_input("What is the name of your custom shape",key= 'name')
    formula_type = st.selectbox(
        "Choose what you formula will say about your custom shape",
        ["Area","Perimiter","Surface Area","Volume"],
        key= 'formula_type'
    )
    formula = st.text_input(f"What is the formula for your shape? (Read the help!)", help="Use `3.141` for pi. Put a space between each operator, like `x1 * x2 / 6`. Use `x1`, `x2`, `x3`, etc. instead of variable names. You'll give each input a name separately later.",key= 'formula')
    list_of_names = []
    for i in range(number_of_inputs):
        new_name = st.text_input(f"What is the x{i+1} input called?")
        list_of_names.append(new_name)

    submitted = st.form_submit_button('Submit',key="Form Submit")
if submitted:
    safe_formula = test_formula(formula)

    if safe_formula:
        dict_of_names = {}
        for name in range(len(list_of_names)):
            name += 1
            dict_of_names[list_of_names[name-1]] = f"x{name}"
        json_of_names = dict_of_names
        supabase.table("Shapes").insert({
            "name": shape_name,
            "formula": formula,
            "formula_type": formula_type,
            "number_of_inputs": number_of_inputs,
            "name_of_inputs": json_of_names
        }).execute()
        
        st.write("Your shape has been eccepted and submitted to the database!")
        st.session_state["reset_form"] = True
        st.rerun()
    else:
        st.write("Our system has detected that your formula is not safe! Please write a new formula.")

