#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time # sleep
import json
import os
import ffmpeg
import sys

# Check if argc is correct
if len(sys.argv) != 3:
    print("Usage: py " + sys.argv[0] + " (file containing one URL per line) (output folder with trailing slash)")
    exit()

print("This will not work unless ffmpeg is installed and in your path. Read the GitHub page if you do not know how to do that.")
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
outpath = sys.argv[2] if sys.argv[2][-1] == slash else (sys.argv[2] + slash) # Add trailing back/slash if it isn't there

# We're done with this file
fp.close()

# Enable network logs to get true video URLs
caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}

# Launch Chrome with no console output (network logs not enabled while accepting user credentials)
os.environ["WDM_LOG_LEVEL"] = "0"
opts = webdriver.ChromeOptions()
opts.add_argument("--log-level=3")
driver = webdriver.Chrome(ChromeDriverManager().install(), service_log_path=os.devnull, chrome_options=opts)

# Authenticate
print("\n"*100) # Clear screen because ChromeDriverManager doesn't know how to shut up
print("Please authenticate in the Chrome window")
driver.get("https://play.library.utoronto.ca/login")
while 'Welcome to' not in driver.page_source:
    pass

# Get cookies to stay logged in as we're switching to headless mode
cookies = driver.get_cookies()
# Then launch again in headless mode with no console output and set the old cookies")
opts = webdriver.ChromeOptions()
opts.add_argument("headless")
opts.add_argument("--log-level=3")
driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=caps, chrome_options=opts, service_log_path=os.devnull)

print("\n"*100) # Clear screen because ChromeDriverManager doesn't know how to shut up
print("Authenticated. Collecting video URLs... ", end='')

driver.get("https://play.library.utoronto.ca/login") # Browse to a MyMedia domain to be able to set cookies
for cookie in cookies:
    driver.add_cookie(cookie)

# List to hold all the video  URLs
playlists = []
# List to hold all the video titles
titles = []

# Get video URLs and titles
for url in video_urls:
    driver.get(url)
    time.sleep(3) # Wait until page loads. Hopefully will be replaced with a non-janky method later

    #Get video title
    titles.append(driver.find_element(By.CSS_SELECTOR, "h2.chakra-heading").text)

    #Get video URL
    log = driver.get_log('performance')
    for item_ in log:
        item = json.loads(item_["message"])["message"]
        if item["method"] == "Network.responseReceived":
            if item["params"]["response"]["url"].endswith("playlist.m3u8"):
                playlists.append(item["params"]["response"]["url"])

# Download videos
print("Done.\nStarting download...")
for i, playlist in enumerate(playlists):
    stream = ffmpeg.input(playlist)
    stream = ffmpeg.output(stream, outpath + titles[i] + ".mp4", c="copy")
    ffmpeg.run(stream)
    print(".",end="")
print("\n"*100 + "Done.")

