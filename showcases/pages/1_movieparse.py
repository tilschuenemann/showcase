
from movieparse.main import Movieparse
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(layout="wide")
st.write(
    "<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

st.title("movieparse")
st.markdown(
    "`movieparse` is a lazy utility for fetching bulk movie data from TMDB using movie release year and title. It has both an Python API and CLI."
)
st.markdown(
    """Supported naming conventions:
* 1999 The Matrix
* 1999 - The Matrix"""
)
st.markdown("""---""")


def lookup(user_input: str):
    # disable caching for demonstration
    m = Movieparse()
    m.parse_movielist([user_input])

    mapping_file = Path.cwd() / "mapping.csv"

    if mapping_file.exists():
        mapping_file.unlink()
    return (m.cast, m.collect, m.crew, m.details, m.genres, m.prod_comp, m.prod_count, m.spoken_langs, m.mapping)


left_column, right_column = st.columns([1, 3])

with left_column:
    user_input = st.text_input(
        "Supply movie (and optionally a release year):", value="1999 Matrix")
    submit_button = st.button("Submit!")

with right_column:
    expand = True
    if submit_button:
        cast, collect, crew, details, genres, prod_comp, prod_count, spoken_langs, mapping = lookup(
            user_input)
        with st.expander("mapping.csv", expanded=expand):
            st.write(mapping)

        with st.expander("cast.csv", expanded=expand):
            st.write(cast)

        with st.expander("collect.csv", expanded=expand):
            st.write(collect)

        with st.expander("crew.csv", expanded=expand):
            st.write(crew)

        with st.expander("details.csv", expanded=expand):
            st.write(details)

        with st.expander("genres.csv", expanded=expand):
            st.write(genres)

        with st.expander("prod_comp.csv", expanded=expand):
            st.write(prod_comp)

        with st.expander("prod_count.csv", expanded=expand):
            st.write(prod_count)

        with st.expander("spoken_langs.csv", expanded=expand):
            st.write(spoken_langs)
