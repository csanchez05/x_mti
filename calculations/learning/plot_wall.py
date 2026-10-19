import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- load ---
m = np.load("problem3b.out/m000000.npy")
print("shape:", m.shape)   # expect (3, 1, 64, 256) = (component, z, y, x)

dx = 1e-9                  # cell size in x (m), must match the .mx3
ny = m.shape[2]
mz = m[2, 0, ny // 2, :]   # z-component, only layer, middle row, all x
x = (np.arange(mz.size) + 0.5) * dx * 1e9   # cell centers in nm

# --- fit the wall: mz = -tanh((x - x0)/Delta)  ->  atanh(-mz) is a straight line ---
core = np.abs(mz) < 0.9                    # use only points inside the wall
slope, intercept = np.polyfit(x[core], np.arctanh(-mz[core]), 1)
Delta = 1 / slope
x0 = -intercept / slope
print(f"wall center x0 = {x0:.1f} nm")
print(f"Delta = {Delta:.2f} nm   (theory ~4.2 nm), full width pi*Delta = {np.pi*Delta:.1f} nm")

# --- plot ---
plt.figure()
plt.plot(x, mz, "o", ms=3, label="mumax3")
plt.plot(x, -np.tanh((x - x0) / Delta), "-", label=f"fit, $\\Delta$ = {Delta:.2f} nm")
plt.xlim(x0 - 40, x0 + 40)                 # zoom in on the wall
plt.xlabel("x (nm)")
plt.ylabel("$m_z$")
plt.legend()
plt.savefig("wall_profile.png", dpi=300)
plt.close()
print("saved wall_profile.png")