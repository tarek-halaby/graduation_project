import numpy as np
import cv2
import matplotlib.pyplot as plt

def detect_person(image_path):
    model = 'MobileNetSSD_deploy.caffemodel'
    prototxt = 'MobileNetSSD_deploy.prototxt.txt'
    net = cv2.dnn.readNetFromCaffe(prototxt, model)
    image = cv2.imread(image_path)
    cv2.imshow("Original", image)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    for i in range(0, detections.shape[2]):

        confidence = detections[0, 0, i, 2]
        if confidence > 0.2:

            idx = int(detections[0, 0, i, 1])
            if idx == 15:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                crop_img = image[startY:endY, startX:endX + 5]
                edge_img = detect_edge(crop_img)
                fill_edge(edge_img)

def detect_edge(crop_img):
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    edge_img = cv2.Canny(blurred, 10, 200)
    cv2.imshow("Edge", edge_img)

    # gray = cv2.cvtColor(crop_img, cv2.COLOR_RGB2GRAY)
    # # create a binary thresholded image
    # _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
    # # show it
    # plt.imshow(binary, cmap="gray")
    # plt.show()
    # # find the contours from the thresholded image
    # contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # # draw all contours
    # edge_img = cv2.drawContours(crop_img, contours, -1, (0, 255, 0), 2)
    # plt.imshow(edge_img)
    # plt.show()
    return edge_img

def fill_edge(edge_img):
    thresh = cv2.threshold(edge_img, 128, 255, cv2.THRESH_BINARY)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    filled = np.zeros_like(thresh)
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    the_contour = contours[0]
    cv2.drawContours(filled, [the_contour], 0, 255, -1)
    cv2.imshow("Fill", filled)

image_path = 'l.jpg'
detect_person(image_path)
cv2.waitKey(0)
