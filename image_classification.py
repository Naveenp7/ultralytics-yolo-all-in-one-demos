import cv2
from ultralytics import YOLO

# Load YOLOv8 classification model
model = YOLO("yolov8n-cls.pt")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Run top-1/top-5 classification
    results = model(frame)
    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 - Image Classification", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()