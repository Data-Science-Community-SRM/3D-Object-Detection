# from .base_camera import BaseCamera
from base_camera import BaseCamera
import cv2
import os
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_objectron = mp.solutions.objectron
from flask import Flask

class Camera(BaseCamera):
    video_source = 0
    stopped = False
    started = False

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        elif os.environ.get('WERKZEUG_RUN_MAIN') or Flask.debug == False:
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']) or 0)

        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source
        Camera.started = True
        Camera.stopped = False

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # _, img = camera.read()
            # yield cv2.imencode('.jpg', img)[1].tobytes()
            with mp_objectron.Objectron(static_image_mode=False,
                            max_num_objects=5,
                            min_detection_confidence=0.4,
                            min_tracking_confidence=0.7) as objectron:
                while camera.isOpened():
                    success, image = camera.read()
                    if not success:
                        print("Ignoring empty camera frame.")
                        continue

                    image.flags.writeable = False
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    results = objectron.process(image)

                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    if results.detected_objects:
                        for detected_object in results.detected_objects:
                            
                            mp_drawing.draw_landmarks(image, 
                                                    detected_object.landmarks_2d, 
                                                    mp_objectron.BOX_CONNECTIONS)
                            
                            mp_drawing.draw_axis(image, 
                                                detected_object.rotation,
                                                detected_object.translation)
                    yield cv2.imencode(".jpg", cv2.flip(image,1))[1].tobytes()
                    # if cv2.waitKey(5) & 0xFF == 27:
                    #     break

    @staticmethod
    def __del__():
        if Camera.started:
            Camera.stopped = True
            camera = cv2.VideoCapture(Camera.video_source)
            camera.release()
            cv2.destroyAllWindows()