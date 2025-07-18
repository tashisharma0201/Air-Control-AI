import tkinter as tk
from tkinter import ttk

APP_SETTINGS = {
    "font_size": 8,
    "theme": "light",
    "language": "English"   # Default to English
}

LANGUAGES = {
    "English": {
        "Play / Pause": "Play / Pause",
        "Next Track": "Next Track",
        "Previous Track": "Previous Track",
        "Finger Counting": "Finger Counting",
        "Peace / Victory": "Peace / Victory",
        "OK": "OK",
        "Rock": "Rock",
        "Love (Heart)": "Love (Heart)",
        "Open hand (all 5 fingers up)": "Open hand (all 5 fingers up)",
        "Raise index & pinky only": "Raise index & pinky only",
        "Raise index & middle finger only": "Raise index & middle finger only",
        "Raise index & pinky only (Rock)": "Raise index & pinky only (Rock)",
        "Raise index & middle finger only (Peace)": "Raise index & middle finger only (Peace)",
        "Hold up any number of fingers": "Hold up any number of fingers",
        "Touch thumb & index to a circle": "Touch thumb & index to a circle",
        "Both hands form heart": "Both hands, fingertips together as heart",
        "Starts/stops your music": "Starts/stops your music",
        "Plays the next song": "Plays the next song",
        "Plays previous song": "Plays previous song",
        "Displays finger count": "Displays finger count",
        "Shows ‘Peace’ label": "Shows ‘Peace’ label",
        "Shows ‘OK’ label": "Shows ‘OK’ label",
        "Shows ‘Rock’ label": "Shows ‘Rock’ label",
        "Shows ‘Love (Heart)’": "Shows ‘Love (Heart)’ label",
        "Settings": "Settings",
        "Apply": "Apply",               # Added this key
        "Start": "Start",
        "Show Tutorial": "Show Tutorial",
        "Accessibility & Settings": "Settings",
        "Gesture Recognition": "Gesture Recognition",
        "Music Controller": "Music Controller",
        "Welcome": "Welcome to Air Control! Gesture Reference",
        "Select Your Mode": "Select Your Mode:",
        "How to Show": "How to Show",
        "Effect": "Effect",
        "Gesture": "Gesture",
        "Instructions": (
            "• Place your hand clearly in view of the webcam and use good lighting.\n"
            "• Raise ONLY the shown fingers for each gesture.\n"
            "• Try these with left or right hand.\n"
            "• In Finger Counting mode, just hold up any number of fingers!\n"
            "• After reading, press Next to continue."
        ),
        "Next": "Next ➔",
        "CloseApp": "Close window or press Ctrl+C to exit.",
        "Error": "Error",
        "Failed to start the selected mode": "Failed to start the selected mode"
    },
    "हिन्दी": {
        "Play / Pause": "प्ले / पॉज़",
        "Next Track": "अगला गाना",
        "Previous Track": "पिछला गाना",
        "Finger Counting": "उँगली गिनना",
        "Peace / Victory": "शांति / विजय",
        "OK": "ठीक है",
        "Rock": "रॉक",
        "Love (Heart)": "प्यार (दिल)",
        "Open hand (all 5 fingers up)": "सारे हाथ की उंगलियाँ खोलें",
        "Raise index & pinky only": "सिर्फ इंडेक्स और पिंकी उँगली ऊपर करें",
        "Raise index & middle finger only": "सिर्फ इंडेक्स और मिडिल उंगली ऊपर करें",
        "Raise index & pinky only (Rock)": "सिर्फ इंडेक्स और पिंकी उँगली ऊपर करें (रॉक)",
        "Raise index & middle finger only (Peace)": "सिर्फ इंडेक्स और मिडिल उँगली ऊपर करें (शांति)",
        "Hold up any number of fingers": "कोई भी ऊँगली/ऊँगलियाँ ऊपर करें",
        "Touch thumb & index to a circle": "अंगूठे और इंडेक्स से गोला बनाएँ",
        "Both hands form heart": "दोनों हाथों से दिल का आकार बनाएँ",
        "Starts/stops your music": "संगीत चालू या रोकें",
        "Plays the next song": "अगला गाना चलाएँ",
        "Plays previous song": "पिछला गाना चलाएँ",
        "Displays finger count": "उँगलियों की गिनती दिखेगी",
        "Shows ‘Peace’ label": "‘शांति’ लिखा आयेगा",
        "Shows ‘OK’ label": "‘ठीक है’ लिखा आयेगा",
        "Shows ‘Rock’ label": "‘रॉक’ लिखा आयेगा",
        "Shows ‘Love (Heart)’": "‘प्यार (दिल)’ लिखा आयेगा",
        "Settings": "सेटिंग्स",
        "Apply": "लागू करें",            # Added this key
        "Start": "शुरू करें",
        "Show Tutorial": "ट्यूटोरियल देखें",
        "Accessibility & Settings": "सेटिंग्स",
        "Gesture Recognition": "हावभाव मान्यता",
        "Music Controller": "संगीत नियंत्रक",
        "Welcome": "Air Control में आपका स्वागत है! हावभाव मार्गदर्शन",
        "Select Your Mode": "कृपया मोड चुनें:",
        "How to Show": "कैसे दिखाएँ",
        "Effect": "एप असर",
        "Gesture": "हावभाव",
        "Instructions": (
            "• कैमरा के सामने हाथ साफ व अच्छी रोशनी में रखें।\n"
            "• सिर्फ बताई गई उंगलियाँ ऊपर करें।\n"
            "• दोनों हाथों से भी कोशिश करें।\n"
            "• फिंगर काउंटिंग में सिर्फ उँगलियाँ ऊपर करें!\n"
            "• पढ़ने के बाद, आगे बढ़ें।"
        ),
        "Next": "आगे ➔",
        "CloseApp": "खिड़की बंद करें या Ctrl+C दबाएँ।",
        "Error": "त्रुटि",
        "Failed to start the selected mode": "मोड शुरू नहीं हो सका"
    }
}

THEMES = {
    "light": {"bg": "#f6f7fa", "fg": "#181028", "btn": "#1d7ef1", "btn_fg": "white"},
    "dark":  {"bg": "#181028", "fg": "#f6f7fa", "btn": "#f9dd18", "btn_fg": "#181028"}
}

class SettingsDialog(tk.Toplevel):
    def __init__(self, master, callback=None):
        super().__init__(master)
        self.title("Accessibility & Appearance")
        self.callback = callback
        self.geometry("340x330")
        self.resizable(False, False)
        theme = THEMES[APP_SETTINGS["theme"]]
        labels = LANGUAGES[APP_SETTINGS["language"]]
        self.configure(bg=theme["bg"])

        tk.Label(self, text=labels["Settings"],
                 font=("Arial", 13, "bold"),
                 bg=theme["bg"], fg=theme["fg"]).pack(pady=(8,1))

        tk.Label(self, text="Font Size", font=("Arial", 11),
                 bg=theme["bg"], fg=theme["fg"]).pack(pady=(14,0))
        self.font_slider = tk.Scale(
            self, from_=7, to=15, orient="horizontal", length=180,
            resolution=1, bg=theme["bg"], fg=theme["fg"]
        )
        self.font_slider.set(APP_SETTINGS["font_size"])
        self.font_slider.pack()

        tk.Label(self, text="Theme", font=("Arial", 11),
                 bg=theme["bg"], fg=theme["fg"]).pack(pady=(9,0))
        self.theme_var = tk.StringVar(value=APP_SETTINGS["theme"])
        ttk.Combobox(self, textvariable=self.theme_var,
                     values=list(THEMES.keys()), state="readonly",
                     width=14).pack()

        tk.Label(self, text="Language", font=("Arial", 11),
                 bg=theme["bg"], fg=theme["fg"]).pack(pady=(10,0))
        self.lang_var = tk.StringVar(value=APP_SETTINGS["language"])
        ttk.Combobox(self, textvariable=self.lang_var,
                     values=list(LANGUAGES.keys()), state="readonly",
                     width=14).pack()

        tk.Button(self, text=labels["Apply"],    # <-- Changed here
                  font=("Arial", 12, "bold"),
                  bg=theme["btn"], fg=theme["btn_fg"],
                  command=self.apply_settings).pack(pady=24)
        self.grab_set()

    def apply_settings(self):
        APP_SETTINGS["font_size"] = self.font_slider.get()
        APP_SETTINGS["theme"]     = self.theme_var.get()
        APP_SETTINGS["language"]  = self.lang_var.get()
        if self.callback:
            self.callback()
        self.destroy()
