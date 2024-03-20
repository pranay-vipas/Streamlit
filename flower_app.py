import streamlit as st
from app import *
def main():
    hide_streamlit_style = """
    <style>
    header {visibility: hidden;} 
    footer {visibility: hidden;} 	    
    </style>		
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    app()
if __name__ == "__main__":
    main()
