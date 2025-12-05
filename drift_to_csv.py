from picamera2 import Picamera2
import cv2
import numpy as np
import time
import csv

# -----------------------------
# Initialize camera
# -----------------------------
picam2 = Picamera2()
config = picam2.create_video_configuration({"size": (640, 480)})
picam2.configure(config)
picam2.start()
time.sleep(1)

# -----------------------------
# Prepare CSV file
# -----------------------------
csv_file = "drift_data_without_OF_t11.csv"
csv_header = ["timestamp", "dx_pixels_per_sec", "dy_pixels_per_sec", "speed_pixels_per_sec"]

file = open(csv_file, "w", newline="")
writer = csv.writer(file)
writer.writerow(csv_header)

# -----------------------------
# Read first frame
# -----------------------------
prev = picam2.capture_array()
prev_gray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
prev_time = time.time()

print("Recording drift data to drift_data.csv ...")
print("Press CTRL + C to stop.\n")
print("time, dx, dy, speed\n")

# -----------------------------
# Optical Flow Loop
# -----------------------------
try:
    while True:
        frame = picam2.capture_array()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        now = time.time()
        dt = now - prev_time

        flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None,
                                            0.5, 3, 15, 3, 5, 1.2, 0)

        dx = np.median(flow[..., 0]) / dt
        dy = np.median(flow[..., 1]) / dt
        speed = (dx**2 + dy**2) ** 0.5

        # Print on screen
        print(f"{now:.2f}, {dx:.4f}, {dy:.4f}, {speed:.4f}")

        # Write to CSV
        writer.writerow([now, dx, dy, speed])

        prev_gray = gray
        prev_time = now

except KeyboardInterrupt:
    print("\nStopped recording.")

finally:
    file.close()
    print("CSV file saved:", csv_file)
