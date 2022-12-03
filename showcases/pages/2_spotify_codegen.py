import streamlit as st
from spotifycodegen.main import SpotifyCodeGen

st.set_page_config(layout="wide")
st.write(
    "<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

st.title("spotify codegen")

st.markdown(
    "Spotify removed the feature to get a stitched image of an album / artist / track cover with their own [Spotify Code](https://www.spotifycodes.com/). This package mimicks that behaviour and creates stitches, based on supplied URL, URI or query."
)

st.markdown("""---""")
scg = SpotifyCodeGen()

left_column, right_column = st.columns([1, 3])

with left_column:
    by_option = st.radio(label="Generate Spotify Code with:",
                         options=["URI", "URL", "Query"])
    user_input = st.text_area(label=by_option)
    if by_option == "Query":
        search_type = st.radio(label="Query for:", options=[
                               "album", "artist", "track"], horizontal=True)
    submit_button = st.button("Submit")

    try:
        im = None
        if by_option == "URI" and submit_button:
            im = scg._generate_code(user_input)
        elif by_option == "URL" and submit_button:
            url_uri = scg._url_to_uri(user_input)
            if url_uri is not None:
                im = scg._generate_code(url_uri)
        elif by_option == "Query" and submit_button:
            query_uri = scg._query_to_uri(user_input, search_type)
            if query_uri is not None:
                im = scg._generate_code(query_uri)
    except Exception as e:
        st.exception(e)

with right_column:
    if submit_button and im is not None:
        st.image(im, use_column_width="auto")
