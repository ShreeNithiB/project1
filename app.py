import streamlit as st

st.title("Welcome")
st.write("hello welcome to my project")

name=st.text_input("enter your name")
st.write(f"welcome {name}")
st.write("welcome sir")
st.write("I have completed my schooling in coimbatore")
st.write("In this resume I have described about myself")
btn =st.button("click me")
if btn:
    st.write("hi how are you")

st.title("My Resume")
Dict={'Institution Name':['Avila convent school','KG college']}
st.dataframe(Dict)
skills=["python","java"]
for skill in skills:
    st.write(f"-{skill}")    
    
