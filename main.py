import cv2 as cv
import torch
import numpy as np

path = "D:\\Downloads\\Car-Detector\\best.pt" # Set your path of best.pt file here
model = torch.hub.load('ultralytics/yolov5', 'custom', path, force_reload=True)

def image():
    img = cv.imread("D:\\Downloads\\Car-Detector\\car.jpg") # Set your path of image file here
    img = cv.resize(img, (676, 380))
    results = model(img)
    img = np.squeeze(results.render())
    cv.imshow("Image", img)
    # cv.resizeWindow("Image", 700, 300)
    cv.waitKey(0)

def video():
    cap = cv.VideoCapture("travel_-_47901 (Original).mp4")
#     cap = cv.VideoCapture("video (1080p).mp4")
    while True:
        success, frame = cap.read()
        frame = cv.resize(frame, (676, 380))
        results = model(frame)
        frame = np.squeeze(results.render())
        cv.imshow("Video", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
                break

def cam():
     cap = cv.VideoCapture(0)
     while True:
        ret, frame = cap.read()
        frame = cv.resize(frame, (676, 380))
        results = model(frame)
        frame = np.squeeze(results.render())
        cv.imshow("FRAME", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    while True:
        choice = int(input("Enter 0 to exit\nEnter 1 for image input\nEnter 2 for video input\nEnter 2 for live web cam input\nEnter your choice : "))
        if choice == 0 : break
        if choice == 1 : image()
        elif choice == 2 : video()
        else : cam()
