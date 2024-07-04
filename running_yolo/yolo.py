from ultralytics import YOLO
import cv2

model= YOLO('yolov8n.pt')
results=model('E:\object detection\images', show=True)
cv2.waitKey(0)