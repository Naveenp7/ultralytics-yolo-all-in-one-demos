import cv2
from ultralytics import YOLO

# Load YOLOv8 Oriented Bounding Box (OBB) model
model = YOLO("yolov8n-obb.pt")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Run OBB detection (great for rotated objects)
    results = model(frame)
    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 - Oriented Bounding Box", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()