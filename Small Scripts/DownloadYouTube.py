from pytube import YouTube, Playlist
from tkinter import Tk, filedialog
from os import mkdir

root = Tk()
root.withdraw()
SAVE_PATH = filedialog.askdirectory()

while (choice := input("Songs or an album? [s/a] (Ctrl + c to exit): ")).lower() not in ["s", "a"]:
    print("Type 's' and hit enter for a song, or 'a' and hit enter for an album.")
choice = choice.lower()

TEMP_PATH = SAVE_PATH + "/temporary"
mkdir(TEMP_PATH)


def download(song: YouTube):
    print("Downloading " + song.title)

    mp4files = song.streams.filter(file_extension="mp4")

    path = mp4files[-1].download(TEMP_PATH, mp4files[-1].default_filename)




if choice == "s":
    links = []
    while (link := input("Video link: ")) != "":
        yt = YouTube(link)
        print(yt.title)
        links.append(yt)

    map(download, links)

    print("Videos downloaded!")
else:
    yta = Playlist(input("Album link: "))

    for yt in yta.videos:
        download(yt)
