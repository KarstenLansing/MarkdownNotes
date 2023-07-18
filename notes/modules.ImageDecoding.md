---
id: jfds8zcos6ggghmo99ha9z1
title: ImageDecoding
desc: ''
updated: 1678141210135
created: 1676668234276
---
## Overview
- exiftool
    - extract all metadata from image: exiftool -a -u -g1 -G1 -j image.jpg
- steghide
    - extract hidden data from image: steghide extract -sf image.jpg
- ImageMagick
    - convert image to text: convert image.jpg image.txt
    - convert image to hex: convert image.jpg image.hex
    - convert image to binary: convert image.jpg image.bin
- Binwalk
    - extract hidden data from image: binwalk -e image.jpg
