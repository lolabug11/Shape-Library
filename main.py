import streamlit as st

from supabase import create_client
pg = st.navigation([
    st.Page('pages/home.py',title="Home"),
    st.Page('pages/calculator.py',title= "Calculator"),
    st.Page('pages/make_a_shape.py',title= "Make a Shape"),
    st.Page('pages/community_shapes.py',title= 'Community Shapes')
],position="hidden")

pg.run()




supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)


#     Insert New row example for later referance
# supabase.table("Shapes").insert({
#     "name": "Python Test",
#     "formula": "x + y",
#     "calculation_type": "Test"
# }).execute()


# 
#    Get col from table
# response = supabase.table("shapes").select("*").eq("id", 5).execute()
# change the .eq("id", 5) to change the id that you get
# 



