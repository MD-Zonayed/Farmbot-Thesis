import streamlit as st
import numpy as np
import pandas as pd
import helper as help
import cv2
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
from PIL import Image
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(
    page_title="Farmbot",
    page_icon="🪴",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    #footer {visibility: hidden;}
    </style>"""

with st.sidebar:
    app_page = option_menu(
        menu_title="Farmbot",
        options=["Home"],
        icons=["house-fill"],
    )

st.sidebar.success("Select Any Page from here")

def main():
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    #footer {visibility: hidden;}
    </style>"""

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

home = lambda: (
    help.header("Welcome to Farmbot"),
    help.sub_text("A place where A.I meets Agriculture to give you the best Farming experience<p> </p>")
)

col1 = st.columns(1)

# NOTE:
# Replace this with a relative repository path before publishing.
video_file = open("videos/FarmBot_Thesis_Vedio_Updated.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)

if app_page == "Home":
    home()

if __name__ == '__main__':
    main()
