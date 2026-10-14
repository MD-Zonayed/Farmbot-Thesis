import streamlit as st
import base64
from datetime import date
import time
import cv2

def set_bg_hack():
    # Set background image
    main_bg = "background.jpg"
    main_bg_ext = "jpg"

    st.markdown(
        f'''
         <style>
         .reportview-container {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
         }}
         </style>
         ''',
         unsafe_allow_html=True
     )

def header(text):
    html_temp = f'''<center>
    <h2 style = "color:#F26531; text_align:center; font-weight: bold;"> {text} </h2></center>
    </div>
    '''
    st.markdown(html_temp, unsafe_allow_html=True)

def sub_text(text):
    html_temp = f'''
    <center><strong style = "color:#FFFFFF; font-weight: bold; text_align:justify;"> {text} </strong></center>
    </div>
    '''
    st.markdown(html_temp, unsafe_allow_html=True)

def expander():
    expander_text = '''
        <p> Object detection functionality &#10024 </p>
        <p> The models used here are <b>tflite</b> models, the notebook & codes on how I built the A.I models from scratch are in my github repo
        <a href= 'https://github.com/osinkolu?tab=repositories' style="color:#F26531;" target = "_blank" >here  </a>. They will be kept private until the project is completed.
        My name is Olufemi Victor Tolulope, an ML and A.I enthusiast, feel free to reach out on
        <a href = 'https://www.linkedin.com/in/olufemi-victor-tolulope/' style="color:#F26531;" target = "_blank" >LinkedIn</a>. </p>
        <p> Snapshot functionality &#128247 </p>
        <p> The webrtc snapshot functionality was shared in
        <a href = 'https://discuss.streamlit.io/t/new-component-streamlit-webrtc-a-new-way-to-deal-with-real-time-media-streams/8669/23?u=whitphx'  style="color:#F26531;" target = "_blank" > this discussion  </a>
        by the author of the component
        <a href = 'https://github.com/whitphx'  style="color:#F26531;" target = "_blank" > whitphx </a>. </p>
        <p> Big thanks to Tijana Nikolic who created the
        <a href = 'https://medium.com/@tijana.nikolic'  style="color:#F26531;"  target = "_blank" > blog post  </a>
        I used to learn streamlit, she made it really easy</p>
        <p> Thanks so much to both authors and their amazing work &#129330 </p>
        '''
    expander = st.expander("References & special thanks", expanded=False)
    with expander:
        sub_text(expander_text)

def write_image(out_image):
    today = date.today()
    d = today.strftime("%b-%d-%Y")
    t = time.localtime()
    current_time = time.strftime("%H-%M-%S", t)
    file_name = "tempDir/photo_" + d + "_" + current_time + ".jpg"
    cv2.imwrite(file_name, out_image)
    return file_name
