# 3D-Object-Detection
 In this project we aim to create the website where the user feed the live video and it will be processed by models where it will identify the 3D Object and create the 3D bounding box around the object.
## MODELS TRAINED FOR OBJECT DETECTION:

- ### YOLOV7
 1. Using this model the objects detected shows more accuracy.
 2. But it give low fps in live video.

- ### YOLOV5
 1. In this model we get more FPS for video.
 2. But compared to YOLOV7 it does not have good detection accuracy even training after more epoch.

## YET TO DO:
1. We have successfully completed detection part, so now we have to create the 3D bounding box around the object.
2. For creating 3D bounding box we have to convert the 2D points of detected 2D object into 3D points to create the box around it.
