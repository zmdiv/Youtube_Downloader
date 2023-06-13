import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def download_video():
    url = url_entry.get()
    directory = filedialog.askdirectory()  # Open the directory selection
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path=directory)  # Specify the output path when downloading
    status_label.config(text="Download complete")

root = tk.Tk()

url_entry = tk.Entry(root)
url_entry.pack()

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
