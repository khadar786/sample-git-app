import streamlit as st

st.title('CampusX')

col1,col2=st.columns(2)

with col1:
    st.image('datascience_1718760959885.jpg')

with col2:
    st.header('CampusX is an online platform')
    
st.header('Courses')
st.subheader('DSMP')
st.subheader('DAMP')
st.subheader('DEMP')
st.subheader('DSA')

st.sidebar.title('Menu')
st.sidebar.markdown("""
- Home
- About
- Contact
- Career
- Login
""")

