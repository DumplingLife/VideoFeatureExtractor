import numpy as np

name = "2022-06-07_17-18-46_S00_eye-tracking-video-worldGaze_frame"

file_paths = [f"features_segmented/{name}/{i}.npy" for i in range(6)]
arrays = []
for file_path in file_paths:
    array = np.load(file_path)
    arrays.append(array)
concatenated_array = np.concatenate(arrays, axis=0)

output_path = f"features/{name}.npy"
np.save(output_path, concatenated_array)
print(f"Saved concatenated array to {output_path}")