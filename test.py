from pathlib import Path
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.id3 import ID3

import os
import json



def file_read(filename):
    with open (filename, "r") as f:
        temp = json.load (f)
    return temp

def file_write(filename, data):
    with open (filename, "w") as f:
        json.dump(data, f, indent = 4)


def lijst(filename):
    temp = file_read(filename)
    for entry in temp:
        for key in entry:
            print (key,":", entry[key])
        print ("==================") 

def toevoegen(filename, data):
    temp = file_read(filename)
    temp.append(data)
    file_write(filename, temp)

def read_metadata(file_path):
    ext = file_path.suffix.lower()

    if ext == ".mp3":
        audio = MP3(file_path, ID3=ID3)
        tags = audio.tags
    elif ext == ".flac":
        audio = FLAC(file_path)
        tags = audio.tags
    else:
        print(f"Unsupported file type: {ext}")
        return
    
    # Extract common metadata
    try:
        title = tags.get("TIT2") or tags.get("title", ['Unknown'])[0]
        artist = tags.get("TPE1") or tags.get("artist", ['Unknown'])[0]
        album = tags.get("TALB") or tags.get("album", ['Unknown'])[0]

        data = {
            "filename": file_path.name,
            "title": title,
            "ablum": album,
            "artist": artist
        }
        print (data)
        toevoegen("test.json", data)
    except Exception as e:
        print(f"Error reading tags: {e}")

# Function to process all music files in a folder
def process_folder(folder_path):
    folder = Path(folder_path)
    file_write("test.json", [])

    if not folder.is_dir():
        print(f"{folder_path} is not a valid folder.")
        return

    # Iterate through all files in the folder
    for file_path in folder.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in [".mp3", ".flac", ".ogg"]:
            read_metadata(file_path)

# Specify the folder path
folder_path = "media"

# Process all files in the folder
process_folder(folder_path)
