import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load both CSV files
df_withOF = pd.read_csv("drift_data_with_OF_t11.csv")
df_withoutOF = pd.read_csv("drift_data_without_OF_t11.csv")

# Extract signals
dx1 = df_withOF["dx_pixels_per_sec"]
dy1 = df_withOF["dy_pixels_per_sec"]
s1 = df_withOF["speed_pixels_per_sec"]

dx2 = df_withoutOF["dx_pixels_per_sec"]
dy2 = df_withoutOF["dy_pixels_per_sec"]
s2 = df_withoutOF["speed_pixels_per_sec"]

# Step 1: Equal number of samples
N = min(len(dx1), len(dx2))

dx1 = np.interp(np.linspace(0, len(dx1), N), np.arange(len(dx1)), dx1)
dy1 = np.interp(np.linspace(0, len(dy1), N), np.arange(len(dy1)), dy1)
s1 = np.interp(np.linspace(0, len(s1), N), np.arange(len(s1)), s1)

dx2 = np.interp(np.linspace(0, len(dx2), N), np.arange(len(dx2)), dx2)
dy2 = np.interp(np.linspace(0, len(dy2), N), np.arange(len(dy2)), dy2)
s2 = np.interp(np.linspace(0, len(s2), N), np.arange(len(s2)), s2)

t = np.arange(N)

# Common limits
dx_min, dx_max = min(dx1.min(), dx2.min()), max(dx1.max(), dx2.max())
dy_min, dy_max = min(dy1.min(), dy2.min()), max(dy1.max(), dy2.max())
s_min, s_max = min(s1.min(), s2.min()), max(s1.max(), s2.max())

# ============================================
# Plot 1: DX
# ============================================
plt.figure(figsize=(14, 8))

plt.subplot(3, 1, 1)
plt.plot(t, dx1, label="WITH Optical Flow", linewidth=2, color="blue")
plt.plot(t, dx2, label="WITHOUT Optical Flow", linewidth=2, color="red")
plt.ylim(dx_min, dx_max)
plt.ylabel("dx (pixels/sec)")
plt.grid(True)
plt.legend()

# ============================================
# Plot 2: DY
# ============================================
plt.subplot(3, 1, 2)
plt.plot(t, dy1, label="WITH Optical Flow", linewidth=2, color="blue")
plt.plot(t, dy2, label="WITHOUT Optical Flow", linewidth=2, color="red")
plt.ylim(dy_min, dy_max)
plt.ylabel("dy (pixels/sec)")
plt.grid(True)
plt.legend()

# ============================================
# Plot 3: SPEED
# ============================================
plt.subplot(3, 1, 3)
plt.plot(t, s1, label="WITH Optical Flow", linewidth=2, color="blue")
plt.plot(t, s2, label="WITHOUT Optical Flow", linewidth=2, color="red")
plt.ylim(s_min, s_max)
plt.xlabel("Time (samples)")
plt.ylabel("Velocity (pixels/sec)")
plt.grid(True)
plt.legend()

plt.suptitle("Overlapped Drift Measurements: WITH vs WITHOUT Optical Flow", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
