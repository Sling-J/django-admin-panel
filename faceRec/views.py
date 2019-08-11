from django.shortcuts import render
import cv2
import numpy as np
import face_recognition
from userAPI.models import UserProfile as User
from turnstile.models import Turnstile
import time
import tensorflow as tf
import sys
import threading
from PIL import Image, ImageDraw, ImageOps
sys.path.append('./facerec/faceboxes')
sys.path.append('./facerec/antispoofing')
from face_detector import FaceDetector
import antispoofing
from django.http import HttpResponse

# import os

import warnings
warnings.filterwarnings("ignore")

import pickle

# os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'
answer = False
seconds = 0
timer = None
def timer_start():
    global seconds, timer
    seconds-=1
    print("%i second(s) left" % seconds)
    if seconds == 0:
        print("Access is denied!")
        # timer_stop()
        return
    timer = threading.Timer(1, timer_start)
    timer.start()

def timer_stop():
    global timer, seconds
    seconds = 0
    timer.cancel()

def find_closest(face_detector, frame, score_threshold=.25):
    image_array = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    boxes, scores = face_detector(image_array, score_threshold=score_threshold)
    if len(boxes) < 1:
        return [], [], 0
    image = Image.fromarray(image_array)

    boxes = np.array(np.array(boxes))
    areas = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])
    closest_id = sorted(zip(np.arange(0, len(boxes)), areas), reverse=True, key=lambda x: x[1])[0][0]

    ymin, xmin, ymax, xmax = boxes[closest_id].tolist()

    return np.array(image.crop([xmin, ymin, xmax, ymax])), boxes, closest_id

def videoShow(frame, face_locations, closest_id):
    image = Image.fromarray(frame)

    for i, (top, right, bottom, left) in enumerate(face_locations):
        top, right, bottom, left = int(top), int(right), int(bottom), int(left)
        color = (255, 0, 255) if i == closest_id else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return

def faceRecog(self, username, turnstile):
    # Маркер для визуального отображения камеры и времени
    build = True
    global seconds, answer
    answer = False
    seconds = 7
    timer = None
    user = User.objects.get(username=username)
    turnstile = Turnstile.objects.get(name=turnstile)
    
    face_detector = FaceDetector("./faceRec/faceboxes/model.pb", gpu_memory_fraction=0.25, visible_device_list='0')
    clf = antispoofing.AntiSpoofing(.6)
    start = time.time()
    known_image =  face_recognition.load_image_file(user.avatar)
    known_face_endcoding = face_recognition.face_encodings(known_image)[0]
    # pickle.dump(known_face_endcoding, open('known_face_endcoding.pkl', 'wb'))
    # known_face_endcoding = pickle.load(open('known_face_endcoding.pkl', 'rb'))
    print("Preprocess: ", time.time()-start)

    if turnstile.id == 2:
        cap = cv2.VideoCapture(int(turnstile.ip_camera))
    else: 
        cap = cv2.VideoCapture(turnstile.ip_camera)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    timer_start() #Timer for waiting user! 
    process_this_frame = True

    while seconds > 0:
        _, frame = cap.read()
        if process_this_frame:
            start = time.perf_counter()
            closest_face_array, borders, closest_id = find_closest(face_detector, frame)

            if build:
                end = time.perf_counter()
                print('find_closest', end - start)
                start = end
            
            if build:
                videoShow(frame, borders, closest_id)
            
            if len(closest_face_array) == 0:
                continue

            result = clf(closest_face_array)
            if build:
                end = time.perf_counter()
                print('antispoofing', end - start)
                start = end
                print('\n')

            if result == 0:
                continue

            open_cv_image = np.array(closest_face_array) 
            open_cv_image = open_cv_image[:, :, ::-1]

            unknown_face_encoding = face_recognition.face_encodings(open_cv_image)
            if build:
                end = time.perf_counter()
                print('encodings', end - start)
                start = end
                print('\n')

            if len(unknown_face_encoding) > 0:
                result = face_recognition.compare_faces(known_face_endcoding, unknown_face_encoding)[0]
                if result:
                    print("Access is approved!")
                    answer = True
                    timer_stop() 
                    # break
                    
        process_this_frame = not process_this_frame
    
    
    

    cap.release()
    cv2.destroyAllWindows()

def show_result(request):
    global answer
    if answer is True:
        html = "<html><h1>ACCESS IS APPROVED</h1></html>"
    else:
        html = "<html><h1>ACCESS IS DENIED</h1></html>"
    return HttpResponse(html)
