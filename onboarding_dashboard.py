import os
import tkinter as tk
from settings import SettingsDialog, APP_SETTINGS, LANGUAGES, THEMES

TUTORIAL_FLAG = "user_data/tutorial_complete.txt"
# Use white/bright emoji for icons in dark mode to ensure visibility
def get_icon(icon, dark):
    # For hand/finger emojis, add a white circle background (if possible in your font)
    white_icons = {
        "✋": "✋🏻", "👈": "👈🏻", "👉": "👉🏻", "✌️": "✌🏻", "👌": "👌🏻", "🤘": "🤘🏻"
        # ❤️ is clearly visible always, 🔢 is clear too; can be left as is.
    }
    return white_icons.get(icon, icon) if dark else icon

dashboard_slides = [
    {"icon":"✋","gesture":"Play / Pause","how":"Open hand (all 5 fingers up)","meaning":"Starts/stops your music"},
    {"icon":"🤘","gesture":"Next Track","how":"Raise index & pinky only (Rock)","meaning":"Plays the next song"},   # Changed: was "Rock", now mapped to Next Track
    {"icon":"✌️","gesture":"Previous Track","how":"Raise index & middle finger only (Peace)","meaning":"Plays previous song"}, # Changed: was "Peace", now mapped to Prev Track
    {"icon":"🔢","gesture":"Finger Counting","how":"Hold up any number of fingers","meaning":"Displays finger count"},
    
    {"icon":"👌","gesture":"OK","how":"Touch thumb & index to a circle","meaning":"Shows ‘OK’ label"},
    
    {"icon":"❤️","gesture":"Love (Heart)","how":"Both hands form heart","meaning":"Shows ‘Love (Heart)’"}
]


def show_onboarding_and_continue(callback):
    root = tk.Tk()
    theme = THEMES[APP_SETTINGS["theme"]]
    bg, fg = theme["bg"], theme["fg"]
    btn_bg, btn_fg = theme["btn"], theme["btn_fg"]
    fs = APP_SETTINGS["font_size"]
    labels = LANGUAGES[APP_SETTINGS["language"]]
    is_dark = (theme["bg"] == "#181028")

    root.title(labels["Welcome"])
    root.geometry("860x590")
    root.configure(bg=bg)

    top = tk.Frame(root, bg="#582cff"); top.pack(fill="x")
    tk.Label(top, text="👋 "+labels["Welcome"],
             bg="#582cff", fg="white",
             font=("Arial", fs+6, "bold"), pady=8).pack()

    canvas = tk.Canvas(root, bg=bg, highlightthickness=0)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    sb = tk.Scrollbar(root, orient="vertical", command=canvas.yview,
                      width=35,
                      troughcolor="#ffe85b" if is_dark else "#ffd691",
                      bg="#fff" if is_dark else "#1d7ef1",  # THICK white thumb on dark mode
                      activebackground="#21cbff")
    sb.pack(side=tk.RIGHT, fill=tk.Y, padx=(2,10), pady=8)
    canvas.configure(yscrollcommand=sb.set)

    main = tk.Frame(canvas, bg=bg)
    win = canvas.create_window((0,0), window=main, anchor="nw")

    def on_conf(e):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(win, width=canvas.winfo_width())
    main.bind("<Configure>", on_conf)
    canvas.bind("<Configure>", lambda e: canvas.itemconfig(win, width=e.width))

    def on_wheel(e):
        delta = getattr(e, 'delta', None)
        if delta: canvas.yview_scroll(int(-1*(delta/120)), "units")
        elif hasattr(e, 'num'):
            if e.num==5: canvas.yview_scroll(1,"units")
            elif e.num==4: canvas.yview_scroll(-1,"units")
    canvas.bind_all("<MouseWheel>", on_wheel)
    canvas.bind_all("<Button-4>", on_wheel); canvas.bind_all("<Button-5>", on_wheel)

    heads = ["", labels["Gesture"], labels["How to Show"], labels["Effect"]]
    hbg = "#ffefbc" if is_dark else "#ebe2ff"
    hfg = "#181028" if is_dark else "#5723a7"
    for c,t in enumerate(heads):
        tk.Label(main, text=t, bg=hbg, fg=hfg,
                 font=("Arial", fs+2,"bold"),
                 bd=1, relief="solid", width=22, pady=8, anchor="center").grid(row=0, column=c, sticky="nsew")
        main.grid_columnconfigure(c, weight=1, minsize=75)

    cb1 = "#271e38" if is_dark else "#faf6ff"
    cb2 = "#2c2645" if is_dark else "#f6f0fe"

    icon_font = ("Arial", fs+12, "bold") if is_dark else ("Arial", fs+12)
    for i,item in enumerate(dashboard_slides):
        G = labels.get(item["gesture"], item["gesture"])
        H = labels.get(item["how"], item["how"])
        M = labels.get(item["meaning"], item["meaning"])
        cell = cb1 if i%2==0 else cb2
        icon = get_icon(item["icon"], is_dark)
        # Responsive wrapping and padding
        tk.Label(main, text=icon, font=icon_font,
                 bg=cell, fg="#fff" if is_dark else "#181028",
                 width=3, anchor="center", pady=10).grid(row=i+1, column=0, sticky="nsew", padx=(4,2))
        tk.Label(main, text=G, font=("Arial",fs+2,"bold"),
                 bg=cell, wraplength=150, fg=fg, anchor="w", padx=8).grid(row=i+1, column=1, sticky="nsew", padx=(0,2))
        tk.Label(main, text=H, font=("Arial",fs+1),
                 bg=cell, wraplength=210, anchor="w", justify="left", fg=fg, padx=6).grid(row=i+1, column=2, sticky="nsew", padx=(0,2))
        tk.Label(main, text=M, font=("Arial",fs+1),
                 bg=cell, wraplength=180, anchor="w", justify="left", fg=fg, padx=4).grid(row=i+1, column=3, sticky="nsew")

    # Instructions section, which also wraps as the window shrinks
    tk.Label(main, text=labels["Instructions"],
             font=("Arial",fs+1,"italic"), bg=bg,
             fg="#ee9733" if is_dark else "#7f5ae6",
             justify="left",pady=10,wraplength=750, anchor="w").grid(
        row=len(dashboard_slides)+1, column=0, columnspan=4, padx=12, pady=(16,6), sticky="ew")

    def open_settings():
        def redraw():
            root.destroy(); show_onboarding_and_continue(callback)
        SettingsDialog(root, callback=redraw)
    settings_bg = "#dbfff0" if is_dark else "#ebe2ff"
    settings_fg = "#009671" if is_dark else "#582cff"
    tk.Button(main, text=labels["Accessibility & Settings"],
          font=("Arial", fs+1, "bold"), 
          bg="#dbfff0" if bg=="#181028" else "#ebe2ff",
          fg="#009671" if bg=="#181028" else "#582cff",
          width=12,  # Add this parameter to limit width
          command=open_settings).grid(
    row=len(dashboard_slides)+2, column=0, columnspan=4, pady=(3,10))


    def next_go():
     root.destroy()
     callback()

    btnf = tk.Frame(main, bg=bg)
    btnf.grid(row=len(dashboard_slides)+3, column=0, columnspan=4, pady=(13,20), sticky="ew")
    tk.Button(btnf, text=labels["Next"], font=("Arial",fs+2,"bold"),
              bg=btn_bg, fg=btn_fg, width=14, height=2, bd=0,
              activebackground="#17a364", activeforeground="white",
              command=next_go).pack()

    root.update(); canvas.configure(scrollregion=canvas.bbox("all"))
    root.minsize(450,300)
    root.mainloop()

if __name__=="__main__":
    show_onboarding_and_continue(lambda: None)
