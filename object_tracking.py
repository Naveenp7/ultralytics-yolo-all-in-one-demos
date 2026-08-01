import cv2
from ultralytics import YOLO

# Load model for object tracking
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # persist=True maintains object IDs across consecutive frames
    results = model.track(frame, persist=True, tracker="bytetrack.yaml")
    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 - Object Tracking", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()