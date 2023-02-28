import streamlit as st

st.header(":blue[About me]")
st.subheader('Hello!! My name is Sahithi:smile:')
st.snow()

btn_click = st.button("I Want to introduce myself to you please click me")

if btn_click == True:
    st.balloons()
    btn_click = st.button("Thank you so much :smile:")
    st.subheader("I am Data Science Learner who is at the starting stage currently I am a data science intern at INNOMATICS RESEARCH LABS upgrading myself day by day with the help of innomatics reasearch labs")
    

    