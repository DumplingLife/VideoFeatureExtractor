import numpy as np
import sys

print(f"Shape of {sys.argv[1]}: {np.load(sys.argv[1]).shape}")

# usage: python view_npy.py path_to_your_npy_file.npy