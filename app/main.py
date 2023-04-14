from flask import Flask, render_template, Response, request

# from .camera import Camera
from camera import Camera

stopped = False
started = False



app = Flask(__name__)
app.threaded = True


@app.route('/', methods=['GET', 'POST'])
def index():
    start = Camera.started
    stop = Camera.stopped
    if request.method == 'POST':
        formStart = request.form.get("start")
        formStop = request.form.get("stop")
        if formStart == "start":
            Camera.started = True
            Camera.stopped = False
        if formStop == "stop":
            Camera.started = False
            Camera.stopped = True

    start = Camera.started
    stop = Camera.stopped
    print("start: ", start)
    print("stop: ", stop)
    return render_template('index.html', start=start, stop=stop)


def gen(camera):
    yield b'--frame\r\n'
    while True:
        frame = camera.get_frame()
        yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'


@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop')
def stop():
    if Camera.started:
        Camera.stopped = True
        Camera.started = False
        return "stopped"
    else:
        return "already stopped"