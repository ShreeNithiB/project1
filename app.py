import streamlit as st

st.title("Welcome")
st.write("hello sir")

name=st.text("SHREE NITHI BALASUBRAMANI")
st.write("Thank you for giving me this wonderful opportunity to attend this interview sir")

st.write("In this resume I have described about myself")
st.write("Im sure that, from this resume you will get a clear outline about me.")

btn =st.button("click")
if btn:
    st.write("hi how are you")

st.title("MY RESUME")
st.write("""My name is Shreenithi.B.I am from coimbatore.
         I have completed my studies in coimbatore. Now Iam trying for a new job.""")
st.write("My hobbies are listening to music,reading books and chatting with my friends")
st.write("Email address:abc1234@gmail.com")
st.write("Linked in profile:Shreenithi Balasubramani")
st.write("""1)Certification:project based on AI  in daily life.
         2)eigen values analysis based project.3)cloud and deveops expert... """)
st.write("Experience:zoho(1year)")
st.write("I have also been teamleader for 2 projects")
st.write("My talents are read and write fast.Im havinhg a good communication")

Dict={'Institution Name':['Avila convent school','KG college'],'Phone number':[8970897654],'Address':['vadavalli, coimbatore']}
st.dataframe(Dict)
skills=["python","java","c","c++"]
for skill in skills:
    st.write(f"-{skill}")    
    
