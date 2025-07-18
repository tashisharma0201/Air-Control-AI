import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import sys

def launch_controller(path, is_folder=False):
    # Pass chosen path and folder flag to music controller
    args = [sys.executable, 'music_controller.py', path]
    if is_folder:
        args.append('folder')
    subprocess.Popen(args)

root = tk.Tk()
root.withdraw()

msg = "Choose a music file or a music folder for playlist control."

if messagebox.askyesno("Music Controller - Select Type", "Do you want to select a music folder as playlist? (No to select a single file)"):
    path = filedialog.askdirectory(title="Select Music Folder")
    if path:
        launch_controller(path, is_folder=True)
    else:
        messagebox.showinfo("Exit", "No folder selected. Exiting.")
else:
    path = filedialog.askopenfilename(
        title="Select Music File",
        filetypes=[("Audio Files", "*.mp3 *.wav *.aac *.m4a")]
    )
    if path:
        launch_controller(path)
    else:
        messagebox.showinfo("Exit", "No file selected. Exiting.")
