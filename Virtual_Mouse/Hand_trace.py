import cv2
import mediapipe as mp
import time
import math
import numpy as np

class HandDetector:
    def __init__(self, mode=False, max_hands=1, model_complexity=1, detection_confidence=0.5, track_confidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.model_complexity = model_complexity
        self.detection_confidence = detection_confidence
        self.track_confidence = track_confidence

        self.mediapipe_hands = mp.solutions.hands
        self.hands = self.mediapipe_hands.Hands(self.mode, self.max_hands, self.model_complexity, self.detection_confidence, self.track_confidence)
        self.mediapipe_draw = mp.solutions.drawing_utils
        self.tip_ids = [4, 8, 12, 16, 20]

    def find_hands(self, image, draw=True):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(image_rgb)
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mediapipe_draw.draw_landmarks(image, hand_landmarks, self.mediapipe_hands.HAND_CONNECTIONS)

        return image

    def find_hand_position(self, image, hand_number=0, draw=True):
        x_list = []
        y_list = []
        bounding_box = []
        self.landmark_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_number]
            for id, landmark in enumerate(my_hand.landmark):
                height, width, _ = image.shape
                cx, cy = int(landmark.x * width), int(landmark.y * height)
                x_list.append(cx)
                y_list.append(cy)
                self.landmark_list.append([id, cx, cy])
                if draw:
                    cv2.circle(image, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            x_min, x_max = min(x_list), max(x_list)
            y_min, y_max = min(y_list), max(y_list)
            bounding_box = x_min, y_min, x_max, y_max

            if draw:
                cv2.rectangle(image, (x_min - 20, y_min - 20), (x_max + 28, y_max + 28), (0, 255, 0), 2)

        return self.landmark_list, bounding_box

    def fingers_up(self):
        fingers = []
        try:
            # Thumb
            if self.landmark_list[self.tip_ids[0]][1] > self.landmark_list[self.tip_ids[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Fingers
            for id in range(1, 5):
                if self.landmark_list[self.tip_ids[id]][2] < self.landmark_list[self.tip_ids[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        except:
            pass

        return fingers

    def find_distance(self, point1, point2, image, draw=True, radius=15, thickness=3):
        x1, y1 = self.landmark_list[point1][1:]
        x2, y2 = self.landmark_list[point2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), thickness)
            cv2.circle(image, (x1, y1), radius, (255, 0, 255), cv2.FILLED)
            cv2.circle(image, (x2, y2), radius, (255, 0, 255), cv2.FILLED)
            cv2.circle(image, (cx, cy), radius, (0, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)
        return length, image, [x1, y1, x2, y2, cx, cy]
