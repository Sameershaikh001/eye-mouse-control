import cv2
from src.eye_tracker import EyeTracker
from src.cursor_control import CursorControl

eye_tracker = EyeTracker()
cursor = CursorControl()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    landmarks = eye_tracker.get_eye_landmarks(frame)
    if landmarks:
        cursor.move_cursor(300, 300)  # Replace with real eye-tracking logic

    cv2.imshow("Eye Tracker", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
