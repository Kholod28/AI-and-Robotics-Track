import cv2
import numpy as np

cap = cv2.VideoCapture(0)

colors = {
    "Red": ([0, 120, 70], [10, 255, 255], (0, 0, 255)),
    "Blue": ([100, 150, 50], [140, 255, 255], (255, 0, 0)),
    "Green": ([40, 70, 70], [80, 255, 255], (0, 255, 0)),
    "Yellow": ([20, 100, 100], [35, 255, 255], (0, 255, 255)),
    "White": ([0, 0, 200], [180, 40, 255], (255, 255, 255)),
    "Black": ([0, 0, 0], [180, 255, 40], (120, 120, 120))
}

while True:
    ret, frame = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    y_position = 30

    for color_name, (lower, upper, box_color) in colors.items():

        lower = np.array(lower)
        upper = np.array(upper)

        mask = cv2.inRange(hsv, lower, upper)

        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        count = 0

        for cnt in contours:

            area = cv2.contourArea(cnt)

            if area > 800:

                x, y, w, h = cv2.boundingRect(cnt)

                cv2.rectangle(frame, (x, y), (x+w, y+h), box_color, 2)

                cv2.putText(frame,
                            color_name,
                            (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            box_color,
                            2)

                count += 1

        cv2.putText(frame,
                    f"{color_name}: {count}",
                    (10, y_position),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    box_color,
                    2)

        y_position += 25

    cv2.imshow("Color Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()