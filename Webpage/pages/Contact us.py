import streamlit as st


st.header("Contact us")

with st.form("Myform"):
    user_email = st.text_input("Your email address")
    text = st.text_area("Your Message here")

    button=st.form_submit_button("Submit")
    if button:
        print("Submit button pressed")
