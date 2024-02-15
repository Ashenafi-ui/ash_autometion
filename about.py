import streamlit as st
def app():
  st.write('About')
  st.sidebar.header("Option")
  text = st.sidebar.text_area('inter data Here')
  button1 = st.sidebar.button("Clean text")
 # if button1:
             # st.write(text)
