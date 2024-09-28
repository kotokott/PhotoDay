import cv2
from datetime import datetime
import time
import os


if not os.path.exists(rf'C:\PhotoDay\Collection'):
    os.makedirs(rf'C:\PhotoDay\Collection', exist_ok=True)


now = datetime.now()
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera error=(")
    exit()
datenow = now.date()

ret, frame = cap.read()
time.sleep(1.5)
ret, frame = cap.read()

if not ret:
    print("Capture error=(")
    exit()

save_path = rf'C:\PhotoDay\Collection\photo{datenow}.jpg'
print(save_path)

cv2.imwrite(save_path, frame)

cap.release()

print("Success:^")