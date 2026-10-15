import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path
matplotlib.use("Agg") #save file, don't display

path = Path(sys.argv[1] if len(sys.argv) > 1 else "problem2.out/table.txt")
d = np.loadtxt(path) # "#" header line is skipped automatically
t = d[:, 0] * 1e9
