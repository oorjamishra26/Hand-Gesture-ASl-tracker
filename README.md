I have created two models:

1 - Video Gesture Dectection

2 - Hand Tracker in Realtime to create data for training image models

# **Video Gesture Dectection**

The code implements a video gesture detection system. It processes input video data, applies background subtraction using the MOG2 model, detects gestures using contour analysis, overlays "DETECTED" text on identified gestures, and generates an output video with annotated frames. The system is designed to identify gestures by detecting moving objects in the video frames and annotating them for visual indication. 

# **Hand Tracker in Realtime**

This code captures images from a video stream in real-time using a webcam. It utilizes the HandTrackingModule from the cvzone library to detect hands in the video frames. When a hand is detected, it crops the region around the hand and resizes it to a fixed size. The cropped and resized hand image is then saved along with a label ('A/B/C') in a designated folder. The process is repeated continuously, allowing the user to capture multiple images of hand gestures according to its label. This functionality facilitates the creation of a dataset for training an image recognition model to recognize and classify hand gestures.

.mov files are the output recorded of the above models
