import streamlit as st

from supabase_client import supabase
def test_formula(formula):
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
if st.button("Home"):
    st.switch_page('pages/home.py')
st.write("Work in progress")


if st.session_state["reset_form"]:
    reset_form()
    st.session_state["reset_form"] = False



with st.form("shape_creation_form"):
    name = st.text_input("What is the name of your custom shape",key= 'name')
    formula_type = st.selectbox(
        "Choose what you formula will say about your custom shape",
        ["Area","Surface Area","Volume"],
        key= 'formula_type'
    )
    formula = st.text_input(f"What is the formula for your shape", help="Use 3.141 for pi. Seperate all signs by a space so like x * y / 6.",key= 'formula')
    number_of_inputs = st.number_input(f"How many inputs does your formula have?",help= "Like for Base * height this would be 2. One for base, and one for height.",value=1,min_value= 1,key= 'number_of_inputs')

    submitted = st.form_submit_button('Submit')
if submitted:
    safe_formula = test_formula(formula)
    if safe_formula:
        supabase.table("Shapes").insert({
            "name": name,
            "formula": formula,
            "formula_type": formula_type,
            "number_of_inputs": number_of_inputs
    }).execute()
        
        st.write("Your shape has been eccepted and submitted to the database!")
        st.session_state["reset_form"] = True
        st.rerun()
    else:
        st.write("Our system has detected that your formula is not safe! Please write a new formula.")

