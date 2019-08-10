import numpy as np
import cv2
from sklearn.externals import joblib

import warnings
warnings.filterwarnings("ignore")

def calc_hist(img):
    histogram = [0] * 3
    for j in range(3):
        histr = cv2.calcHist([img], [j], None, [256], [0, 256])
        histr *= 255.0 / histr.max()
        histogram[j] = histr
    return np.array(histogram)

class AntiSpoofing:
    def __init__(self, threshold=.6):
        self.threshold = threshold
        self.clf = joblib.load('./faceRec/antispoofing/replay-attack_ycrcb_luv_extraTreesClassifier.pkl')

    def __call__(self, face):
        img_ycrcb = cv2.cvtColor(face, cv2.COLOR_BGR2YCR_CB)
        img_luv = cv2.cvtColor(face, cv2.COLOR_BGR2LUV)

        ycrcb_hist = calc_hist(img_ycrcb)
        luv_hist = calc_hist(img_luv)

        feature_vector = np.append(ycrcb_hist.ravel(), luv_hist.ravel())
        feature_vector = feature_vector.reshape(1, len(feature_vector))

        prediction = self.clf.predict_proba(feature_vector)
        
        # 1 Значит лицо настоящее, 0 наоборот
        if np.mean(prediction[0][1]) < self.threshold:
            print("------------>",prediction[0][1])
            
        return np.mean(prediction[0][1]) < self.threshold

