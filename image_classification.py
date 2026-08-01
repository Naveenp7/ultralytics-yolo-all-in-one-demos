import cv2
from ultralytics import YOLO

# Load YOLOv8 classification model
model = YOLO("yolov8n-cls.pt")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Run classification inference
    results = model(frame)
    probs = results[0].probs

    # Get Top-1 class name and confidence score
    top1_id = probs.top1
    top1_conf = probs.top1conf.item()
    class_name = model.names[top1_id]

    # Draw prediction banner on the screen
    label = f"Prediction: {class_name} ({top1_conf * 100:.1f}%)"
    cv2.rectangle(frame, (10, 10), (500, 60), (0, 0, 0), -1)  # Background box
    cv2.putText(
        frame, label, (20, 45),
        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
    )

    cv2.imshow("YOLOv8 - Image Classification", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()