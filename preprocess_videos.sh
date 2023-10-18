#!/bin/bash

input_dir="videos_raw"
output_dir="videos"

for video in "$input_dir"/*.avi; do
    name=$(basename "$video" .avi)
    mkdir -p "$output_dir/$name"
    ffmpeg -i "$video" -vf "fps=10,setpts=N/10/TB" -c:v libx264 -an -f segment -segment_time 320 -reset_timestamps 1 "$output_dir/$name/%d.avi"
done
