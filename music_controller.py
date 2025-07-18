import sys, os, cv2, mediapipe as mp, pygame, numpy as np
from PIL import ImageFont, ImageDraw, Image

# Initialize pygame and MediaPipe
pygame.mixer.init()
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5,
    max_num_hands=2
)
drawing_styles = mp_drawing.DrawingSpec(thickness=2, circle_radius=2)

cap = cv2.VideoCapture(0)

WINDOW = "Music Controller"
cv2.namedWindow(WINDOW, cv2.WINDOW_NORMAL)
cv2.resizeWindow(WINDOW, 960, 720)

# Load playlist
music_path = sys.argv[1] if len(sys.argv) > 1 else None
is_folder = (len(sys.argv) > 2 and sys.argv[2] == "folder")
playlist, current = [], 0

if music_path:
    if is_folder:
        for f in os.listdir(music_path):
            if f.lower().endswith(('.mp3', '.wav', '.aac', '.m4a')):
                playlist.append(os.path.join(music_path, f))
    else:
        playlist.append(music_path)

if not playlist:
    print("No music files found.")
    sys.exit()

pygame.mixer.music.load(playlist[current])
pygame.mixer.music.play()

# ========== Helper Functions ==========

def put_text(img, text, pos, font_size=32, color=(0, 255, 0), font_path=None):
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    try:
        font = ImageFont.truetype(font_path or "arial.ttf", font_size)
    except Exception:
        font = ImageFont.load_default()
    draw.text(pos, text, font=font, fill=color)
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

def count_fingers(lmks, hand_label, shape):
    h, w = shape[:2]
    lm = [(lm.x * w, lm.y * h) for lm in lmks.landmark]
    thumb = lm[4][0] > lm[3][0] if hand_label == "Right" else lm[4][0] < lm[3][0]
    state = [thumb] + [lm[tip][1] < lm[tip - 2][1] for tip in [8, 12, 16, 20]]
    return sum(state)

def detect_gesture(count):
    # Change these thresholds/logic as needed for gestures
    if count == 0:
        return "play"
    elif count == 5:
        return "next"
    elif count == 2:
        return "prev"
    else:
        return None

# ========== Main Loop with Debounce ==========

last_gesture = None
trigger_ready = True

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    gesture = None

    if results.multi_hand_landmarks and results.multi_handedness:
        # Assume single hand for gesture
        hand_landmarks = results.multi_hand_landmarks[0]
        hand_label = results.multi_handedness[0].classification[0].label
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS, drawing_styles, drawing_styles)

        # Determine finger count and gesture
        count = count_fingers(hand_landmarks, hand_label, frame.shape)
        gesture = detect_gesture(count)
    else:
        gesture = None

    # Debounce: Only trigger when gesture changes from None to something
    if gesture != last_gesture and gesture is not None and trigger_ready:
        if gesture == "play":
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
        elif gesture == "next":
            current = (current + 1) % len(playlist)
            pygame.mixer.music.load(playlist[current])
            pygame.mixer.music.play()
        elif gesture == "prev":
            current = (current - 1) % len(playlist)
            pygame.mixer.music.load(playlist[current])
            pygame.mixer.music.play()
        trigger_ready = False  # Prevent repeated trigger

    # Reset trigger when hand is removed or gesture changes back to None
    if gesture is None:
        trigger_ready = True

    last_gesture = gesture

    # Overlay song name
    name = os.path.basename(playlist[current])
    frame = put_text(frame, f"Now Playing: {name}", (10, 20))

    # Gesture overlay
    if gesture:
        text = {'play': 'Play/Pause', 'next': 'Next Track', 'prev': 'Previous Track'}.get(gesture, gesture)
        h, w = frame.shape[:2]
        frame = put_text(frame, text, (w - 300, h - 50))

    # Resize to window
    try:
        _, _, win_w, win_h = cv2.getWindowImageRect(WINDOW)
    except:
        win_h, win_w = frame.shape[:2]
    frame = cv2.resize(frame, (win_w, win_h), interpolation=cv2.INTER_LINEAR)

    cv2.imshow(WINDOW, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()
