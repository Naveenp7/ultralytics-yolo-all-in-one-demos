from ultralytics import YOLO

# Load model for multi-object persistent tracking
model = YOLO("yolov8n.pt")

# Runs real-time object tracking with ByteTrack on live webcam feed
model.track(source=0, show=True, tracker="bytetrack.yaml")