import streamlit as st
from supabase import create_client

supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

st.title("Geometry Calc")
"""
    Insert New row example for later referance
supabase.table("Shapes").insert({
    "name": "Python Test",
    "formula": "x + y",
    "calculation_type": "Test"
}).execute()
"""

"""
    Get col from table
    response = supabase.table("shapes").select("*").eq("id", 5).execute()
    change the .eq("id", 5) to change the id that you get
"""



