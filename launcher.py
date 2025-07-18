import os
import sys
import tkinter as tk
import subprocess
from tkinter import ttk, messagebox
from settings import SettingsDialog, APP_SETTINGS, LANGUAGES, THEMES
from onboarding_dashboard import show_onboarding_and_continue

TUTORIAL_FLAG = "user_data/tutorial_complete.txt"

def show_mode_menu():
    root = tk.Tk()
    theme = THEMES[APP_SETTINGS["theme"]]
    bg, fg = theme["bg"], theme["fg"]
    btn_bg, btn_fg = theme["btn"], theme["btn_fg"]
    fs = APP_SETTINGS["font_size"]
    labels = LANGUAGES[APP_SETTINGS["language"]]

    root.title("AI Hand Tracker Launcher")
    root.geometry("540x340")
    root.minsize(430, 280)
    root.configure(bg=bg)

    tk.Label(root, text="🚀 " + labels["Welcome"],
             font=("Arial", fs+5, "bold"),
             bg="#582cff", fg="white", pady=12).pack(fill="x")

    tk.Label(root, text=labels["Select Your Mode"],
             font=("Arial", fs+2, "bold"),
             bg=bg, fg=fg).pack(pady=(20, 8))

    modes = [
        labels["Finger Counting"],
        labels["Gesture Recognition"],
        labels["Music Controller"]
    ]
    
    actual = {
        modes[0]: "count",
        modes[1]: "gesture",
        modes[2]: "music"
    }

    var = tk.StringVar(value=modes[0])
    cb = ttk.Combobox(root, textvariable=var, values=modes,
                      font=("Arial", fs+1), state="readonly", width=25)
    cb.pack(pady=4)

    def launch_mode():
        m = var.get()
        pm = actual[m]
        try:
            if pm == "count":
                subprocess.Popen([sys.executable, "main_tracker.py", "count"], creationflags=subprocess.CREATE_NO_WINDOW)
            elif pm == "gesture":
                subprocess.Popen([sys.executable, "main_tracker.py", "gesture"], creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                subprocess.Popen([sys.executable, "music_selector.py"], creationflags=subprocess.CREATE_NO_WINDOW)
            root.destroy()
        except Exception as e:
            messagebox.showerror(labels["Error"],
                                 f"{labels['Failed to start the selected mode']}:\n{e}")

    tk.Button(root, text=labels["Start"],
              font=("Arial", fs+2, "bold"),
              command=launch_mode,
              bg=btn_bg, fg=btn_fg,
              width=18, height=2, relief="solid").pack(pady=(18, 8))

    def revisit():
        if os.path.isfile(TUTORIAL_FLAG):
            os.remove(TUTORIAL_FLAG)
        root.destroy()
        show_onboarding_and_continue(show_mode_menu)

    tut_bg = "#ffd691" if bg == "#181028" else "#ebe2ff"
    tut_fg = "#ae630a" if bg == "#181028" else "#582cff"

    tk.Button(root, text=labels["Show Tutorial"],
              font=("Arial", fs+2, "bold"),
              command=revisit,
              bg=tut_bg, fg=tut_fg,
              width=18, height=2, relief="solid").pack(pady=(2, 8))

    def open_settings():
        def redraw():
            root.destroy()
            show_mode_menu()
        SettingsDialog(root, callback=redraw)

    sbg = "#dbfff0" if bg == "#181028" else "#ebe2ff"
    sfg = "#009671" if bg == "#181028" else "#582cff"

    tk.Button(root, text=labels["Settings"],
              font=("Arial", fs+2, "bold"),
              bg=sbg, fg=sfg,
              width=18, height=2, relief="solid",
              command=open_settings).pack(pady=(3, 10))

    tk.Label(root, text=labels["CloseApp"],
             font=("Arial", fs), fg="#999", bg=bg).pack(side="bottom", pady=8)

    root.mainloop()

if __name__ == "__main__":
    show_onboarding_and_continue(show_mode_menu)
