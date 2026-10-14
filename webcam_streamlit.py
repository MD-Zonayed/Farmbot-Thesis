import cv2
import streamlit as st
import numpy as np
import tempfile

# Capture video from the webcam
cap = cv2.VideoCapture(1)

st.title("Video Capture with OpenCV")
frame_placeholder = st.empty()
stop_button_pressed = st.button("Stop")

while cap.isOpened() and not stop_button_pressed:
    ret, frame = cap.read()

    if not ret:
        st.write("The video capture has ended.")
        break

    # Convert the frame from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the frame in Streamlit
    frame_placeholder.image(frame, channels="RGB")

    # Break the loop if the 'q' key is pressed or Stop is clicked
    if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
        break

cap.release()
cv2.destroyAllWindows()
