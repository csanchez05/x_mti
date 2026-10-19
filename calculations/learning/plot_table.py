import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt #save file, don't display
import numpy as np

#load the data
d = np.loadtxt("problem2.out/table.txt")
t = d[:, 0] * 1e9 #seconds -> ns
mx = d[:, 1]
my = d[:, 2]
mz = d[:, 3]

#plot mx
plt.figure()
plt.plot(t, mx)
plt.title('Evolution of magnetic moment (X)', fontsize = 25)
plt.xlabel("time (ns)", fontsize=25)
plt.ylabel("mx", fontsize = 25)
plt.savefig("mx.png", dpi=600)
plt.close()
print("saved mx.png")

#plot my
plt.figure()
plt.plot(t, my)
plt.title('Evolution of magnetic moment (Y)', fontsize = 25)
plt.xlabel("time (ns)", fontsize=25)
plt.ylabel("my", fontsize = 25)
plt.savefig("my.png", dpi=600)
plt.close()
print("saved my.png")

#plot mz
plt.figure()
plt.plot(t, mz)
plt.title('Evolution of magnetic moment (Z)', fontsize = 25)
plt.xlabel("time (ns)", fontsize=25)
plt.ylabel("mz", fontsize = 25)
plt.savefig("mz.png", dpi=600)
plt.close()
print("saved mz.png")

