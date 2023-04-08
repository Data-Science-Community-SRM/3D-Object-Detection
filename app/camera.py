from .base_camera import BaseCamera
import cv2
import os
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
            _, img = camera.read()
            yield cv2.imencode('.jpg', img)[1].tobytes()

    @staticmethod
    def __del__():
        if Camera.started:
            Camera.stopped = True
            camera = cv2.VideoCapture(Camera.video_source)
            camera.release()
            cv2.destroyAllWindows()