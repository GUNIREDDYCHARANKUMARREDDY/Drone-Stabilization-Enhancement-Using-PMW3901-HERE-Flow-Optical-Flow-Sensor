# Drone-Stabilization-Enhancement-Using-PMW3901-HERE-Flow-Optical-Flow-Sensor
This project demonstrates how drone stability can be improved using an optical flow sensor (PMW3901/HERE Flow).   The system reduces drift during hover, enhances indoor stability, and makes the drone capable of holding position even without GPS.


The repository includes:
- Drift measurement using Raspberry Pi + Camera  
- Drone integration with HERE Flow optical flow sensor  
- Drift analysis with & without optical flow  
- Python scripts for plotting and comparison  
- Complete documentation and results  

---

##  Project Motivation

Drones naturally drift due to:
- Air turbulence  
- IMU inaccuracy  
- Poor GPS signals  
- Mechanical vibration  

To solve this, an **optical flow sensor** is used to track ground texture.  
It provides real-time motion feedback that helps stabilize the drone in the X-Y plane.

---

##  Features of This Project

###  Raspberry Pi + camera module
- Reads camera frames  
- Computes drift (dx, dy, speed)  
- Logs data to CSV  
- Provides visual graphs

# Placement of Camera on the Drone
- **X-axis → Drone’s Left–Right**
- **Y-axis → Drone’s Forward–Backward**
- 
The camera is used for software-based optical flow and drift measurement.

# Correct Orientation:
- Must face **straight downward** toward the ground.
- The **top of the camera points toward the drone front**.
- The **left side of the camera aligns with the drone left side**.
- The lens must be **flat (0° tilt)**.

This ensures:
- Drone moving forward → ground texture moves backward in the image.
- Drone moving right → texture moves left in the image.

###  HERE Flow Sensor Integration
- PMW3901-based optical flow  
- Mounted on drone bottom  
- Interfaces with Pixhawk/Cube  
- Provides stable hover indoors

# Placement of optical flow sensor on the Drone  
- Must be mounted **facing downward**, same as the camera.
- The **arrow on the HERE Flow must point toward the drone front**.
- The sensor must be **flat**, without tilt.
- X and Y axes must align with the drone axes.

#### Height Requirement:
- Minimum: **8–10 cm**
- Best performance: **20–200 cm**
- Too high (>3 m) or too low (<5 cm) can reduce accuracy.

###  Drift Comparison (With vs Without Optical Flow)
- Reduced drift recorded  
- Improved position hold accuracy  
- Visual overlapped plots included  

---

## 🛠 Hardware Used

- **PMW3901 / HERE Flow Optical Flow Sensor**  
- **Cube flight controller**  
- **Raspberry Pi 4 with camera module**  
- **Quadcopter frame (custom built)**  
- BLDC motors + ESCs  
- LiPo battery  
- Power distribution board  

---

## 🧰 Software Used

- **RaspberryPi3-64bit Operating System**
- **Python 3**  
- **OpenCV** (Optical flow calculation)  
- **NumPy**  
- **MAVLink / PX4 parameters** (for HERE Flow)  

---


