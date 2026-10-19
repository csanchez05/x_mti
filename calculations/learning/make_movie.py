import glob
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

files = sorted(glob.glob("problem4b.out/m*.npy"))
dt = 50e-12 * 1e9                 # ns between frames (match autosave)
x0, x1 = 180, 380                 # crop window in cells (1 nm cells -> nm)

frames = [np.load(f)[:, 0, :, x0:x1] for f in files]   # (3, y, x) each
print(f"loaded {len(frames)} frames")

fig, (a1, a2) = plt.subplots(2, 1, figsize=(8, 4.5), sharex=True)
kw = dict(origin="lower", extent=[x0, x1, 0, 128], aspect="auto",
          cmap="RdBu_r", vmin=-1, vmax=1)
im1 = a1.imshow(frames[0][2], **kw)   # mz: shows where the wall is
im2 = a2.imshow(frames[0][1], **kw)   # my: shows the wall's interior
a1.set_ylabel("y (nm)"); a1.set_title("$m_z$")
a2.set_ylabel("y (nm)"); a2.set_title("$m_y$")
a2.set_xlabel("x (nm)")
fig.colorbar(im1, ax=a1); fig.colorbar(im2, ax=a2)
title = fig.suptitle("")

def update(i):
    im1.set_data(frames[i][2])
    im2.set_data(frames[i][1])
    title.set_text(f"t = {i*dt:.2f} ns")
    return im1, im2, title

ani = FuncAnimation(fig, update, frames=len(frames))
ani.save("dw_motion.gif", writer=PillowWriter(fps=20))
print("saved dw_motion.gif")