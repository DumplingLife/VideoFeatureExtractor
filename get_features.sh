#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <name>"
    exit 1
fi

NAME="$1"

mkdir videos/${NAME}

ffmpeg -i videos_raw/${NAME}.avi -vf "fps=10,scale=224:224" -c:v libx264 -preset fast -c:a copy -map 0 -segment_time 320 -f segment videos/${NAME}/%d.avi

mkdir features_segmented/${NAME}

python preprocess_generate_csv.py --csv=input.csv --video_root_path "./videos/${NAME}" --feature_root_path "./features_segmented/${NAME}" --csv_save_path .

python extract.py --csv=./input.csv --type=s3dg --batch_size=64 --num_decoding_thread=1

python combine_features.py "${NAME}"
