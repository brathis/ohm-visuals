# What is this?
This scrapes the [@cd_masterizzato](https://www.instagram.com/cd_masterizzato/) Instagram page
and creates a movie from the first image of each post in the correct order,
such that [@ohmmusiccollective](https://www.instagram.com/ohmmusiccollective/) may then use it for their epic live shows.

# Prerequisites
  - Python (tested on 3.8)
  - [jq](https://stedolan.github.io/jq/)
  - [Pillow](https://pillow.readthedocs.io/en/stable/)
  - [instagram-scraper](https://github.com/arc298/instagram-scraper)
  - [ffmpeg](https://ffmpeg.org/)

# How To
  1. download all images from cd_masterizzato
        ```bash
        $ instagram-scraper cd_masterizzato -t image --media-metadata
        ```

  2. extract URLs of first image of each post
        ```bash
        $ jq -r .GraphImages[].urls[0] cd_masterizzato/cd_masterizzato.json > urls_first_image.txt
        ```

  3. ohmify the pictures
        ```bash
        $ python ./ohmify.py
        ```

  4. stitch pictures together to a video
        ```bash
        $ ffmpeg -framerate 10 -i out/%04d.jpg ohm.mp4
        ```

  5. (optional) convert video to "boomerang" style for convenient looping
        ```bash
        $ ffmpeg -i ohm.mp4 -filter_complex "[0:v]reverse,fifo[r];[0:v][r] concat=n=2:v=1 [v]" -map "[v]" ohmmho.mp4
        ```
