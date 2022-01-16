# MyMedia Bulk Content Downloader
This is a bulk download tool for the MyMedia platform.

USE ONLY WHERE ALLOWED BY THE COPYRIGHT OWNER. NOT AFFILIATED WITH ANYTHING/ANYONE/ANY ORGANISATION.

## Usage

### 0. Prerequisites
To use this tool, you will have to have all of the following installed.

As long as they are installed correctly, you can put them wherever you want, I have not hardcoded any default locations.

#### a. Python 3
This tool is written in Python and you need to have Python installed for it to work.

You can get Python from [its official website](https://www.python.org/downloads/). Download the installer, then finish the install before continuing.

#### b. Various Python packages
There are thee you neet to download:

- Selenium: This is what I use to interact with Google Chrome. It comes with its own Chrome installation, so no need to install it seperately, and it shouldn't change anything on your regular Chrome.
- webdriver-manager: Has some utility functions that make my life easier
- ffmpeg-python: This is used for Python to talk to a tool we'll download in just a second

Open your favorite terminal emulator (see the FAQ for how to do this) and type the following commands

```py -m ensurepip --upgrade```

```pip3 install selenium ffmpeg-python webdriver-manager ```

#### c. ffmpeg
MyMedia stores videos in a way that makes them difficult to download and use. ffmpeg is a tool that is used (among other things) to convert video formats. This tool uses it to convert that format to mp4 files.

You can download and install ffmpeg from [its official website](https://www.ffmpeg.org/). **Please make sure it is in your "path".** See the FAQ if you don't know what that means, or if you don't know how to put it in your path. The program will fail with a rather complicated error message if ffmpeg is not correctly installed and on your path.

### 1. Download the tool
Secondary (right) click [here](https://raw.githubusercontent.com/egefeyzioglu/mymedia-download/main/mymedia-downloader.py) then select "Save Link As" to download it. You can put it wherever you want, but if you put it in your Downloads folder, you can just go off the examples in this guide.

If you're using Mac and don't know what a secondary click is, just click the link normally, then save the resulting page with ⌘+S

### 2. Get a list of all the videos you want to download
Create a text file (not a Word document) of all the MyMedia URLs (the thingy in the address bar when you're watching the video) you want to get the videos for, one URL per line. Make a note of where you saved this file

### 3. Create a folder where all your downloaded videos will be put in
Again, make a note of where this folder is

### 4. Open a terminal emulator and navigate to where you downloaded the tool
Please see the FAQs if you don't know how to do this

### 5. Run the tool
#### On Windows (Using cmd)
Type `py .\mymedia-downloader.py (path to the list) (path to the folder to put all the videos with the trailing \)`

Replace the bits in the brackets with the paths. You can drag-and-drop the file and the folder to the terminal if you don't know how to find the path to a file, you will just need to add a `\` after the second one. (This not a regular slash, it is a backslah. You type it by pressing the key to the left of the shift key on most English keyboards.)

#### On Mac or Linux
You first need to allow your computer to run this file. To do that, type `chmod u+x mymedia-downloader.py` Then, type `./mymedia-downloader.py (path to the list) (path to the folder to put all the videos with the trailing /)`

Replace the bits in the brackets with the paths. You can _probably_ drag-and-drop the file and the folder to the terminal if you don't know how to find the path to a file, you might need to add a `/` after the second one.

The reason I'm saying probably is because Linux comes in a variety of flavours, and yours might not support this. I assume if you're using Linux, you know what a path is and how to find one. Otherwise google "find absolute path in (name of your Linux distro)".

### 6. Log in with your UTORid and password
Wait for the Chrome window to pop up, then click Log In and authenticate. I do not ever see your UTORid and password, all the communication happens directly between you and the university. Please see the source code if you don't believe me.

### 7. Wait until the screen says "Done."
After that, you should see all the videos you wanted to download in the folder you provided. Unfortunately I have not implemented naming these files correctly, so they are just numbered from 0 onwards. I might come back at this and fix that at some point.


## Frequently Asked Querstions

### Why should I trust you to enter my UTORid and password?
Great question. In theory, you shouldn't. However, I have provided the source code and you can see if you speak Python that the login process is identical to what would happen if you used Google Chrome yourself. After you log in, I hide the Chrome window to make things more efficient and create less of an eye sore, and download all the videos. If you don't speak Python, please feel free to show this to a friend who does. (Hint: Anyone who studies anything adjacent to computer science, data science or engineering should know Python after their first semester.)

### Are you affiliated with (inster organisation here)?
No. I am not. I created this tool on my own, all errors are mine only and I do not claim to represent anyone. This tool is not "official" in any way, shape or form.

### I am affiliated with (insert organisation here) and want to yell at you for creating this.
I have made my absolute best to make sure I'm not violating any EULA's or trademarks etc. It does not exploit any vulnerabilities, it simply automates a task that would be very tedious to do by hand. If you disagree and think that I'm either breaking some law/agreement/etc. or if you think this tool will create harm, please contact me. I'm sure you can find my UofT email, email me there. If you can't, please [create an issue](https://github.com/egefeyzioglu/mymedia-download/issues/new) here.

### What is a terminal emulator and how do I open/use one?
Using a terminal is like having a text message conversation with your computer. You tell it (in a very specific format) to do things, press enter, and it does them for you, and replies with the result.
#### On Windows (cmd)
Open the start menu, then type `cmd.exe` and press enter. This will open "Command Prompt". You can type `cd` then where you want to go to, to navigate to a folder. Again, cou can drag-and-drop folders to the command prompt to place avoid having to type their "paths" out. For example, to go to your Downloads folder, you can type `cd Downloads` right after launching command prompt. You will notice the bit before where you type your command change from `C:\Users\yourusername` to `C:\Users\yourusername\Downloads`. If you have changed the location of your Downloads folder, this will not work. I trust if you know how to do that, you know how to use command prompt and can figure this out on your own (or just drag-and-drop the folder.)
#### On Mac
[Read this](https://support.apple.com/en-ca/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac). You can use the `cd` gommand to move around. For example, you can type `cd ~/Downloads` to go to your downloads folder
#### On Linux
If you run Linux, you probably know how to do this. If you don't, google "(your distribution name) how to use terminal".

### How do I put something on my path?
Your path is where your computer looks for things to run.
#### On Mac/Linux
Run `export (path to the thing you want to add to your path)` in your terminal each time
#### On Windows
[Read this](https://docs.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ee537574(v=office.14)) and do it once. You can remove what you added when you're done if you'd like.
