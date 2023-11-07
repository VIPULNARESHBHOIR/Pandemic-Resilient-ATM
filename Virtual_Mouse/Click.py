import cv2
import numpy as np
import Hand_trace as ht
import time
import autopy

width_camera, height_camera = 640, 480
width_screen, height_screen = autopy.screen.size()  # Screen size
frame_reduction = 100  # Frame reduction
smoothening = 5

previous_time = 0
previous_location_x, previous_location_y = 0, 0
current_location_x, current_location_y = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, width_camera)
cap.set(4, height_camera)
detector = ht.HandDetector(max_hands=1)

while True:
    # Finding the hand landmarks
    success, image = cap.read()
    image = detector.find_hands(image)
    landmark_list, bounding_box = detector.find_hand_position(image)
    # print(landmark_list)

    # Get the tip of the index and middle finger
    if len(landmark_list) != 0:
        x1, y1 = landmark_list[8][1:]
        x2, y2 = landmark_list[12][1:]
        # print(x1, y1, x2, y2)

    # Check up fingers
    fingers = detector.fingers_up()
    # print(fingers, "\n")

    cv2.rectangle(image, (frame_reduction, frame_reduction), (width_camera - frame_reduction, height_camera - frame_reduction),
                  (255, 0, 255), 2)
    if len(fingers) != 0:
        # Only index finger in moving position
        if fingers[1] == 1 and fingers[2] == 0:
            # Converting coordinates for perfect movement of hands
            x3 = np.interp(x1, (0, width_camera), (0, width_screen))
            y3 = np.interp(y1, (0, height_camera), (0, height_screen))

            # Setting to mouse cursor properly over the screen (smoothening)
            current_location_x = previous_location_x + (x3 - previous_location_x) / smoothening
            current_location_y = previous_location_y + (y3 - previous_location_y) / smoothening
            # Movement of mouse over the screen
            autopy.mouse.move(width_screen - current_location_x, current_location_y)
            cv2.circle(image, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

            previous_location_x, previous_location_y = current_location_x, current_location_y

        # When index and middle finger are up then click
        if fingers[1] == 1 and fingers[2] == 1:
            # Find distance between fingers
            distance, image, line_info = detector.find_distance(8, 12, image)

            if distance < 20:
                cv2.circle(image, (line_info[4], line_info[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()
                time.sleep(0.2)

    # Framerate
    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time
    cv2.putText(image, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow('myimage', image)
    cv2.waitKey(1)
