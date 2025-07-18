# Air-Control-AI

An AI-powered hand gesture desktop application that lets you control music playback and interact with your computer using only your hands—no mouse or keyboard required!

---

## 🚀 Features

- 🎯 **Hand Gesture Recognition**  
  Use your hand to control different modes, such as finger counting, gesture recognition, sign language detection, and music control.

- 🎵 **Music Controller**  
  Play, pause, skip tracks, or go back using intuitive hand gestures.

- 🖥️ **Launcher GUI**  
  Easily switch between modes using an intuitive on-screen launcher.

- 🛠️ **Settings & Onboarding**  
  Change language, theme (light/dark), and font — with a walkthrough tutorial for first-time users.

- ✅ **Indian Sign Language (ISL) Support**  
  Detects common ISL letters and gestures for deaf-friendly accessibility.

- 🧠 **Powered By**:  
  Python, OpenCV, MediaPipe, and PyGame

---

## 🛠️ Installation Instructions

1. **Clone the Repository**
   ```
   git clone https://github.com/tashisharma0201/Air-Control-AI.git
   cd Air-Control-AI
   ```

2. **Create a Virtual Environment (Recommended)**
   ```
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Required Libraries**
   ```
   pip install -r requirements.txt
   ```

   If `requirements.txt` is missing, install manually:
   ```
   pip install opencv-python mediapipe pygame Pillow
   ```

---

## ▶️ Running the Application

1. Run the launcher to choose a mode:
   ```
   python launcher.py
   ```

2. Choose from:
   - **Finger Counting**
   - **Gesture Recognition**
   - **Music Controller**
   - **Sign Language (ISL)**

---

## 🎮 Modes & Controls

| Mode                | Description                            |
|---------------------|----------------------------------------|
| Finger Counting     | Counts number of raised fingers        |
| Gesture Recognition | Detects gestures like thumbs up/down, peace, OK sign |
| Music Controller    | Controls media playback using gestures |
| Sign Language (ISL) | Recognizes select ISL alphabet signs and phrases |

---

## ✋ Music Control Gestures

| Gesture           | Action        |
|------------------|---------------|
| Fist             | Play/Pause    |
| 5 Fingers        | Next Track    |
| 2 Fingers (V)    | Previous Track|

*These can be customized in code if needed.*

---

## 🤟 ISL Letter and Phrase Support

### ✅ Implemented ISL Alphabet Letters (Single-Hand):

| Letter | Description                        |
|--------|------------------------------------|
| A      | Fist, thumb outside                |
| B      | 4 fingers up, thumb inside         |
| C      | Curved hand forming a "C"          |
| L      | Thumb and index finger in an "L"   |
| V      | Index and middle fingers up        |
| W      | Index, middle, ring fingers up     |
| I      | Only the pinky up                  |

### ✅ Implemented ISL Phrases / Gestures:

| Phrase or Gesture | Description                                 |
|-------------------|---------------------------------------------|
| I Love You        | Thumb, index, pinky up                      |
| Rock/Good         | Index and pinky up, others down             |
| Yes               | All fingers down (fist)                     |
| No                | All fingers and thumb up (open palm)        |
| Hello             | Open palm, all fingers up (wave-like pose)  |

✍️ *These signs are chosen for strong visibility in the camera and ease of recognition using AI.*

---

## ⚙️ Customization

- Change language, font size, and color theme via:
  ```
  python settings.py
  ```

- Re-run onboarding tutorial anytime using the launcher.

---

## 📋 Requirements

- Python 3.8+
- Webcam (built-in or USB)
- Libraries:
  - `opencv-python`
  - `mediapipe`
  - `pygame`
  - `Pillow`

---

## 💡 Troubleshooting / FAQ

**Q:** My webcam doesn't open or flickers  
**A:** Make sure no other app is using the camera and all dependencies are installed.

**Q:** How do I exit any mode?  
**A:** Press `q` while the camera window is open.

---

## 🙌 Credits

- Created by **Tashi Sharma**
- Gesture and ISL interpretation powered by [MediaPipe](https://google.github.io/mediapipe/) and OpenCV
- ISL visuals/parallels inspired by DEF-ISL and Indian Sign Language resources

---

## 📜 License

MIT License

---

## 🔗 Links

🔗 [GitHub Repository](https://github.com/tashisharma0201/Air-Control-AI)  
Made with ❤️ for sign language inclusion and gesture-powered control.
