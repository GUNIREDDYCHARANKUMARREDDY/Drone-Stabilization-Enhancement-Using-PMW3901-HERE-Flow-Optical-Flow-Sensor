# Drone-Stabilization-Enhancement-Using-PMW3901-HERE-Flow-Optical-Flow-Sensor
This project demonstrates how drone stability can be improved using an optical flow sensor (PMW3901/HERE Flow).   The system reduces drift during hover, enhances indoor stability, and makes the drone capable of holding position even without GPS.


The repository includes:
- Drift measurement using Raspberry Pi + Camera  
- Drone integration with HERE Flow optical flow sensor  
- Drift analysis with & without optical flow  
- Python scripts for plotting and comparison  
- Complete documentation and results  

---

## 🚀 Project Motivation

Drones naturally drift due to:
- Air turbulence  
- IMU inaccuracy  
- Poor GPS signals  
- Mechanical vibration  

To solve this, an **optical flow sensor** is used to track ground texture.  
It provides real-time motion feedback that helps stabilize the drone in the X-Y plane.

---

## 📦 Features of This Project

### ✔ Raspberry Pi Optical Flow System
- Reads camera frames  
- Computes drift (dx, dy, speed)  
- Logs data to CSV  
- Provides visual graphs  

### ✔ HERE Flow Sensor Integration
- PMW3901-based optical flow  
- Mounted on drone bottom  
- Interfaces with Pixhawk/Cube  
- Provides stable hover indoors  

### ✔ Drift Comparison (With vs Without Optical Flow)
- Reduced drift recorded  
- Improved position hold accuracy  
- Visual overlapped plots included  

---

## 🛠 Hardware Used

- **PMW3901 / HERE Flow Optical Flow Sensor**  
- **Pixhawk or Cube flight controller**  
- **Raspberry Pi (4/5) with CSI camera**  
- **Quadcopter frame (custom built)**  
- BLDC motors + ESCs  
- LiPo battery  
- Power distribution board  

---

## 🧰 Software Used

- **Python 3**  
- **OpenCV** (Optical flow calculation)  
- **NumPy**  
- **MAVLink / PX4 parameters** (for HERE Flow)  

---

## 📁 Repository Structure

