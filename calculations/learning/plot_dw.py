import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- load ---
d = np.loadtxt("problem4.out/table.txt")
t  = d[:, 0] * 1e9          # s -> ns
my = d[:, 2]
mz = d[:, 3]

# --- wall position from average mz ---
L = 512                     # strip length in nm
xw = L / 2 * (1 + mz)       # nm

# --- velocity: straight-line fit, skipping the first 0.2 ns of start-up ---
late = t > 0.2
v, x_start = np.polyfit(t[late], xw[late], 1)   # slope in nm/ns = m/s
print(f"wall moved from {xw[0]:.1f} nm to {xw[-1]:.1f} nm")
print(f"velocity = {v:.1f} m/s")

# --- theory (steady motion): v = gamma * Delta * B / alpha ---
gamma, Delta, B, alpha = 1.76e11, 4.07e-9, 10e-3, 0.3
print(f"theory   = {gamma*Delta*B/alpha:.1f} m/s")

# --- plot: position on top, <my> underneath ---
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(7, 6))
ax1.plot(t, xw, label="mumax3")
ax1.plot(t, v * t + x_start, "--", label=f"fit: {v:.1f} m/s")
ax1.set_ylabel("wall position (nm)")
ax1.legend()

ax2.plot(t, my)
ax2.set_xlabel("time (ns)")
ax2.set_ylabel(r"$\langle m_y \rangle$")

fig.tight_layout()
fig.savefig("dw_motion.png", dpi=300)
plt.close()
print("saved dw_motion.png")