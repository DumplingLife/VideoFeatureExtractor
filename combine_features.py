# usage: python combine_features.py name

import numpy as np
import sys
import os

name = sys.argv[1]
directory_path = f"features_segmented/{name}"

def sort_files(file):
    return 

file_paths = sorted(
    [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith('.npy')],
    key=lambda file: int(file.split('.')[0])
    )

arrays = []
for file_path in file_paths:
    array = np.load(file_path)
    arrays.append(array)
concatenated_array = np.concatenate(arrays, axis=0)

output_path = f"features/{name}.npy"
np.save(output_path, concatenated_array)
print(f"Saved concatenated array to {output_path}")