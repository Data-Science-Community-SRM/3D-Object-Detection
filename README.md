# 3D-Object-Detection
 In this project we aim to create the website where the user feed the live video and it will be processed by models where it will identify the 3D Object and create the 3D bounding box around the object.
## MODELS TRAINED FOR OBJECT DETECTION:

- ### YOLOV7
 1. Using this model the objects detected shows more accuracy.
 2. But it give low fps in live video.

- ### YOLOV5
 1. In this model we get more FPS for video.
 2. But compared to YOLOV7 it does not have good detection accuracy even training after more epoch.
 
 ![alt text](https://github.com/Data-Science-Community-SRM/3D-Object-Detection/blob/ml-ks/Data/Yolo%20model.png)
 
## MODELS FOR 3D BOUNDING BOX BUILDING:

- ### Mediapipe objectron
 1. Creates the 3D boundry box successfully.
 2. But the create only for 4 available models(Cup, Shoes, Camera, Chair).
 
 ![alt text](https://github.com/Data-Science-Community-SRM/3D-Object-Detection/blob/ml-ks/Data/Output%20of%20mediapipe%20model.png)


## WORK DONE:
1. Successfully completed detection part using yolov models, where it classify and creates a 2D bounding box.
2. For creating 3D bounding box we have tried convert the 2D points of detected 2D object into 3D points to create the box around it using mediapipe.

## YET TO DO:
1. Need to figure out how to train model for the custom dataset, so that it can create 3D box for more object types.
2. Need to test the model after completing each module and after integrating them as single model.
