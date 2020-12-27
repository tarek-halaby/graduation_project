from flask import Flask, request, jsonify, make_response
from venv.src.demo import show_app
from werkzeug.serving import WSGIRequestHandler
WSGIRequestHandler.protocol_version = "HTTP/1.1"
app = Flask(__name__)
app.config['FLASK_ENV'] = 'development'
import gc
@app.route('/create-model', methods=['POST'])
def create_task():
    if not request.json or not 'measurement' in request.json:
        return "not found", 400
    measurements = request.json['measurement']
    print("hello")
    show_app(measurements)
    with open("src/result.obj", "rb") as object:
        f = object.read()
        b = bytearray(f)
    b64Object = base64.b64encode(b)
    gc.collect()
    return jsonify({'object': b64Object})



