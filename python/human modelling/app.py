import base64
import cv2
import numpy as np
from detectron2.demo.test import detect_human
from flask import Flask, request, jsonify, make_response
from werkzeug.serving import WSGIRequestHandler
import threading,time
WSGIRequestHandler.protocol_version = "HTTP/1.1"
app = Flask(__name__)
app.config['FLASK_ENV'] = 'development'
import gc
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
@app.route('/upload-image', methods=['POST'])
def create_task():
    if request.json and 'wait' in request.json:
        with open("detectron2/demo/img.jpg", "rb") as image:
            f = image.read()
            b = bytearray(f)

        # baseImage=base64.b64encode(img)
        # bytedEdge=edgedImage.tobytes()
        b64Image = base64.b64encode(b)
        return jsonify({'image': b64Image.decode('utf-8'),'processing': 'False',})
    elif not request.json or not 'image' in request.json:
        return "not found", 400
    image = request.json['image']
    # im = Image.open(BytesIO(base64.b64decode(image)))
    # im.save('image.png', 'PNG')
    imgdata = base64.b64decode(image)
    filename = 'detectron2/demo/some_image.jpg'  # I assume you have a way of picking unique filenames

    with open(filename, 'wb') as f:
        f.write(imgdata)
    # img = cv2.imread('flask_test.jpg', cv2.IMREAD_GRAYSCALE)
    thread = myThread()
    thread.start()
    del image
    del imgdata
    gc.collect()
    return jsonify({'processing': 'True'})



class myThread (threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)
      self._running = True
   def isRunning(self):
       return self._running
   def terminate(self):
       self._running = False
   def run(self):
       print('1')
       detect_human('detectron2/demo/some_image.jpg')
       self._running = False
       print('2')
       del self
       gc.collect()

#
# def detect_person(image_path):
#     model = 'MobileNetSSD_deploy.caffemodel'
#     prototxt = 'MobileNetSSD_deploy.prototxt.txt'
#     net = cv2.dnn.readNetFromCaffe(prototxt, model)
#     image = cv2.imread(image_path)
#     (h, w) = image.shape[:2]
#     blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
#     net.setInput(blob)
#     detections = net.forward()
#
#     for i in range(0, detections.shape[2]):
#
#         confidence = detections[0, 0, i, 2]
#         if confidence > 0.2:
#
#             idx = int(detections[0, 0, i, 1])
#             if idx == 15:
#                 box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
#                 (startX, startY, endX, endY) = box.astype("int")
#                 # cv2.rectangle(image,(startX,startY),(endX,endY),(0,0,255),2)
#                 crop_img = image[startY:endY, startX:endX + 5]
#                 edge_img = detect_edge(crop_img)
#                 binary_img = convert_to_binary(crop_img)
#                 cv2.imwrite("img.jpg", edge_img)
#
#
# def detect_edge(crop_img):
#     #
#     # gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
#     # blurred = cv2.GaussianBlur(gray, (3, 3), 0)
#     # edge_img = cv2.Canny(blurred, 10, 200)
#     # #cv2.imshow("Edge", edge_img)
#
#     gray = cv2.cvtColor(crop_img, cv2.COLOR_BGRA2GRAY)
#
#
#     # create a binary thresholded image
#     _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
#
#     # find the contours from the thresholded image
#     contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
#     # # draw all contours
#     edge_img = cv2.drawContours(crop_img, contours, -1, (0, 255, 0), 2)
#     cv2.imwrite("edge.jpg", edge_img)
#
#     return edge_img
#
# def fill_edge(edge_img):
#     thresh = cv2.threshold(edge_img, 128, 255, cv2.THRESH_BINARY)[1]
#     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
#     thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
#     filled = np.zeros_like(thresh)
#     contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     contours = contours[0] if len(contours) == 2 else contours[1]
#     the_contour = contours[0]
#     cv2.drawContours(filled, [the_contour], 0, 255, -1)
#     #cv2.imshow("Fill", filled)
#     return filled
#
# def convert_to_binary(crop_img):
#     gray = cv2.cvtColor(crop_img, cv2.COLOR_RGB2GRAY)
#     # create a binary thresholded image
#     _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
#     # show it
#     return binary
#
