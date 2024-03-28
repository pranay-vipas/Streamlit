import streamlit as st
import os
import k8s
import requests
from shell import Shell
import boto3
java_home = os.environ.get('JAVA_HOME') 
print(os.environ)
print(os.getenv())
st.query_params()
st.get_option()
