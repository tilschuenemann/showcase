import streamlit as st

st.set_page_config(layout="wide")
st.write("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

st.header("About")

st.markdown("Hey there!")
st.markdown("Here I present some of programs / packages I've written.")
st.markdown(
    """ 
|program|about|GitHub Repository|
|---|---|---|
|movieparse|`movieparse` is a lazy utility for fetching bulk movie data with a Python API and CLI. |[GitHub](https://github.com/tilschuenemann/movieparse)|
|spotify codegen|`spotify codegen` is Python CLI for stitching Spotify Album / Artist / Track cover with Spotify Code|[GitHub](https://github.com/tilschuenemann/spotifycodegen)|

"""
)
