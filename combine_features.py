# usage: python combine_features.py name

import numpy as np
import sys

name = sys.argv[1]

file_paths = [f"features_segmented/{name}/{i}.npy" for i in range(6)]
arrays = []
for file_path in file_paths:
    array = np.load(file_path)
    arrays.append(array)
concatenated_array = np.concatenate(arrays, axis=0)

output_path = f"features/{name}.npy"
np.save(output_path, concatenated_array)
print(f"Saved concatenated array to {output_path}")