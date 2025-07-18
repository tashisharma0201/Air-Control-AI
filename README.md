# Air-Control-AI

An AI-powered hand gesture desktop application that lets you control music playback and interact with your computer using only your hands—no mouse or keyboard required!

## 🚀 Features

- **Hand Gesture Recognition:** Use your hand to control different modes (finger counting, gesture recognition, music control).
- **Music Controller:** Play, pause, skip tracks, or go back using simple hand gestures.
- **Launcher GUI:** Choose between multiple modes via a friendly on-screen interface.
- **Onboarding & Settings:** Customizable language, theme, and tutorial/onboarding dashboard.
- **Powered By:** Python, OpenCV, MediaPipe, PyGame.

## 🛠️ Installation Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/tashisharma0201/Air-Control-AI.git
cd Air-Control-AI
```

### 2. (Recommended) Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
# Or
source venv/bin/activate    # On macOS/Linux
```

### 3. Install All Required Libraries

```bash
pip install -r requirements.txt
```

If there is no `requirements.txt`, install the modules manually:

```bash
pip install opencv-python mediapipe pygame Pillow
```

## ▶️ Running the Application

Navigate to your project folder and run:

```bash
python launcher.py
```

This will open the main application window. Select your desired mode and follow any on-screen instructions.

## 🎮 Modes and Usage

| Mode Name            | Description                                              | How to Launch                    |
|----------------------|---------------------------------------------------------|-----------------------------------|
| Finger Counting      | Detects how many fingers you show to the camera         | Select "Finger Counting" in launcher |
| Gesture Recognition  | Recognizes hand gestures for general control            | Select "Gesture Recognition"      |
| Music Controller     | Music play/pause and navigation with hand gestures      | Select "Music Controller"         |

### 🎵 Music Controller – Hand Gesture Commands

| Gesture / Fingers Held | Action             |
|-----------------------|--------------------|
| Fist / No fingers     | Play/Pause toggle  |
| Five fingers          | Next track         |
| Two fingers           | Previous track     |

*(You can customize finger mapping in code if preferred.)*

### 👋 Common Controls

- **Exit Camera View / Stop a Mode:**  
  In any camera mode window, press the `q` key on your keyboard to exit and return to the launcher or close.

## ⚙️ Settings & Customization

- Access the settings window from the launcher to change:
    - **Language**
    - **Theme (dark/light)**
    - **Font size**
- Re-run onboarding tutorial any time via the dedicated launcher button.

## 📋 Requirements

- **Python 3.8+**
- **Working Webcam**
- **Libraries:**  
    - OpenCV (`opencv-python`)
    - MediaPipe
    - PyGame
    - Pillow

## 📝 Additional Tips

- For best performance, ensure good lighting and sit around 1-2 feet from your camera.
- Some features may require data/model files—ensure `user_data/` and any `.binarypb` models exist in your project directory.
- If you see errors about missing model files (e.g., with MediaPipe), follow instructions to bundle them or install with pip.

## 💡 FAQ

**Q: My camera window doesn't open or flickers. What should I do?**  
A: Make sure your webcam is not in use by other apps and that you've installed all dependencies. Run scripts via terminal to see error details.

**Q: How do I exit any mode and go back?**  
A: Press the `q` key while in the camera window.

## 🙌 Credits

Created by Tashi Sharma.  

## 📜 License

MIT

## 🔗 Project Links

- [GitHub Repository](https://github.com/tashisharma0201/Air-Control-AI)

**Enjoy gesture-powered control on your desktop!**  
For help, bug reports, or contributions, please open an issue or pull request on GitHub.
