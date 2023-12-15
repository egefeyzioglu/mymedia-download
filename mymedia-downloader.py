#! /usr/bin/env python3

import ffmpeg
import sys
import re

playlist_url = (
        "https://stream.library.utoronto.ca:1935"
        "/MyMedia/play/mp4:1/{}.mp4/playlist.m3u8"
        )
# This is pretty terrible performance-wise but honestly I don't care that much
video_id_pattern = "(?<=embed/)|(?<=watch/)[0-9a-zA-Z]*"

# Check if argc is correct
if len(sys.argv) != 3:
    print(
            "Usage: py " +
            sys.argv[0] +
            (
                " (file containing one URL per line) "
                "(output folder with trailing slash)"
            )
            )
    exit()

print(
        (
            "This will not work unless ffmpeg is installed and in your path. "
            "Read the GitHub page if you do not know how to do that.")
        )
yn = input("Is ffmpeg installed and in your path? [Y/n] ")
if yn != "Y" and yn != "y":
    print("Please go do that and run me again.")
    exit()


# Get MyMedia URLs
fp = open(sys.argv[1], "r")

# Set globals
# Video URLs
video_urls = fp.readlines()
# Output path
slash = '\\' if sys.platform == "win32" else '/'
# Add trailing back/slash if it isn't there
outpath = sys.argv[2] if sys.argv[2][-1] == slash else (sys.argv[2] + slash)
# We're done with this file
fp.close()

# List to hold all the video  URLs
playlists = []
# List to hold all the video titles
titles = []

# Get video URLs and titles
for url in video_urls:
    # Get video ID
    video_id = re.search(video_id_pattern, url, flags=re.MULTILINE)
    if video_id is None:
        continue
    video_id = video_id.group(0)
    playlists.append(playlist_url.format(video_id))
    # print(video_id)
print("Read {} video URLs, extracted {} playlists.".format(
    len(video_urls),
    len(playlists)))
print("")
print("Reading video titles is currently not supported.")
print("I'm going to fix this at some point but I need to study for finals")
print("So the files are just going to be numbered.")
titles = [str(x) for x in range(len(playlists))]
print("")
print("Also another thing -I promise I'll fix it after finals, but for now")
print("you need to specify beforehand if you want to overwrite files in")
print("the output directory. The file names will be:")
print("\n".join([x+".mp4" for x in titles]))
print("If these exist in the output directory, would you like them to")
yn = input("be overwritten? [Y/n] ")
overwrite_output = (yn == "Y" or yn == "y")
# Download videos
print("Starting download...")
for i, playlist in enumerate(playlists):
    # print(playlist)
    stream = ffmpeg.input(playlist)
    stream = ffmpeg.output(stream, outpath + titles[i] + ".mp4", c="copy")
    ffmpeg.run(stream, overwrite_output=overwrite_output, quiet=True)
    print(".", end="")
print("\nDone.")
