import cv2
from ultralytics import YOLO

# Load lightweight YOLOv8 model
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Run object detection
    results = model(frame)
    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 - Object Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()