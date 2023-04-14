# 3D-Object-Detection
 We have updated our individual work in the branch directory. 
 
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
 2. But they create only for 4 available models(Cup, Shoes, Camera, Chair).
 
 ![alt text](https://github.com/Data-Science-Community-SRM/3D-Object-Detection/blob/ml-ks/Data/Output%20of%20mediapipe%20model.png)

- ### To start your model :-
 1. Install all dependency from requirements.txt file 
 ```bash
    git clone https://github.com/Data-Science-Community-SRM/3D-Object-Detection.git # clone
    cd 3D-Object-Detection
    pip install -r requirements.txt  # install
 ```
 2. Start your server
 ```bash
    gunicorn --workers 4 app.main:app --threads=1 --bind 0.0.0.0
 ```
 3. your server will start at 0.0.0.0:8000 port and enjoy!!!



