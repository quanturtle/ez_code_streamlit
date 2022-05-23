import streamlit as st
from multiapp import MultiApp
from apps import home, linux, git # import your app modules here
import os

app = MultiApp()

st.title('EZ Code Cheatsheet')
st.markdown('Powered by [Streamlit](https://streamlit.io/)')

# Apps
app.add_app("Home", home.app)
app.add_app("Linux", linux.app)
app.add_app("Git", git.app)

# Run main app
app.run()
