import streamlit as st
import pandas as pd

# st.set_page_content()

col1, col2=st.columns(2)

with col1:
    st.image("images/foto_1.jpg", width=200)



with col2:
    st.title("Matteo Villani")
    content="""
    Description of myself
    """

    st.info(content)
    content2="""
    Below you can find all my apps coded in Python.
    """
    st.write(content2)

col3, emptycol, col4=st.columns([1.5,0.5,1.5])

df=pd.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    st.write(content2)
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(f"[Source Code]({row['url']})")
