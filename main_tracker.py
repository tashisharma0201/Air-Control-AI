import cv2
import mediapipe as mp
import sys
from math import dist

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5,
    max_num_hands=2
)
drawing_styles = mp_drawing.DrawingSpec(thickness=2, circle_radius=2)
cap = cv2.VideoCapture(0)

WINDOW = "Sign & Gesture Recognition"
cv2.namedWindow(WINDOW, cv2.WINDOW_NORMAL)
cv2.resizeWindow(WINDOW, 960, 720)

mode = sys.argv[1].lower() if len(sys.argv) > 1 else "count"
valid_modes = ["count", "gesture", "sign", "both"]
if mode not in valid_modes:
    print(f"Invalid mode '{mode}'. Choose from: {valid_modes}")
    sys.exit()

def count_fingers(hand_landmarks, handedness, frame_shape):
    h, w = frame_shape[:2]
    fingers = []
    landmarks = [(lm.x*w, lm.y*h) for lm in hand_landmarks.landmark]
    thumb_up = (landmarks[4][0] < landmarks[3][0]) if handedness=='Right' else (landmarks[4][0] > landmarks[3][0])
    fingers.append(thumb_up)
    for tip, pip in zip([8,12,16,20], [6,10,14,18]):
        fingers.append(landmarks[tip][1] < landmarks[pip][1])
    return fingers

def is_heart_shape_two_hands(h1, h2):
    TIPS = [4,8,12,16,20]
    pts1 = [(h1.landmark[i].x, h1.landmark[i].y) for i in TIPS]
    pts2 = [(h2.landmark[i].x, h2.landmark[i].y) for i in TIPS]
    thres = 0.09
    return (
        all(dist(pts1[i], pts2[i]) < thres for i in range(5))
        and abs(sum(y for _,y in pts1)/5 - sum(y for _,y in pts2)/5) < 0.13
    )

def detect_gesture(fingers, lm):
    thumb, idx, mid, ring, pinky = fingers
    if all(fingers):
        return "Raised Hand / Wave"
    if thumb and not any([idx,mid,ring,pinky]) and lm[4].y < lm[2].y:
        return "Thumbs Up"
    if thumb and not any([idx,mid,ring,pinky]) and lm[4].y > lm[2].y:
        return "Thumbs Down"
    if not thumb and idx and mid and not (ring or pinky):
        return "Peace"
    if dist((lm[4].x,lm[4].y),(lm[8].x,lm[8].y)) < 0.05 and all([mid,ring,pinky]):
        return "OK"
    if not thumb and idx and not mid and not ring and pinky:
        return "Rock"
    return "Unknown"

# ------- Updated Minimal, robust set for sign language mode ----------
def detect_easy_sign(fingers, lm):
    thumb, idx, mid, ring, pinky = fingers

    # A: fist, thumb outside
    if not any([idx, mid, ring, pinky]) and thumb:
        return "A"

    # B: all fingers (except thumb) up and together
    if all([idx, mid, ring, pinky]) and not thumb:
        return "B"
    
    # C: curved hand (approximate by some finger curl and spacing)
    if idx and mid and ring and pinky and thumb:
        tip_dist = dist((lm[4].x, lm[4].y), (lm[8].x, lm[8].y))
        if 0.1 < tip_dist < 0.25:
            return "C"

    # L: index up, thumb out
    if idx and not mid and not ring and not pinky and thumb:
        return "L"

    # V: index and middle up, rest down
    if idx and mid and not ring and not pinky and not thumb:
        return "V"

 # W: index, middle, ring up
    if idx and mid and ring and not pinky and not thumb:
        return "W"

    # I: pinky up only
    if pinky and not any([idx, mid, ring, thumb]):
        return "I"

    # I Love You: thumb, index, pinky up
    if thumb and idx and not mid and not ring and pinky:
        return "I Love You"

    # Yes: fist, all down
    if not any([thumb, idx, mid, ring, pinky]):
        return "Yes"

    # No: open palm without thumb
    if all([idx, mid, ring, pinky]) and not thumb:
        return "No"

    # Rock/Good: index and pinky up
    if idx and not mid and not ring and pinky and not thumb:
        return "Rock/Good"

    # Hello: all fingers including thumb up, and the palm is facing front (check thumb x position vs wrist to approximate direction)
    if all([thumb, idx, mid, ring, pinky]):
        return "Hello"

    # F: Thumb and index touching to form a circle
    if (dist((lm[4].x, lm[4].y), (lm[8].x, lm[8].y)) < 0.05) and mid and ring and pinky:
        return "F"

    # Thumb and pinky up – like “Call Me” gesture
    if thumb and not idx and not mid and not ring and pinky:
        return "Call Me"

    # Shaka: thumb and middle finger up
    if thumb and not idx and mid and not ring and not pinky:
        return "Shaka"

    return ""

last_sign = ""
last_time = 0
import time
DEBOUNCE_DELAY = 0.8

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)

    display_heart = False
    if res.multi_hand_landmarks and len(res.multi_hand_landmarks) == 2:
        if is_heart_shape_two_hands(*res.multi_hand_landmarks):
            display_heart = True

    total_count = 0
    now = time.time()
    # MAIN HAND LOOP
    for i, hand_landmarks in enumerate(res.multi_hand_landmarks or []):
        handed = res.multi_handedness[i].classification[0].label if res.multi_handedness else "Right"
        fingers = count_fingers(hand_landmarks, handed, frame.shape)
        lm = hand_landmarks.landmark

        if display_heart:
            gesture = "Love (Heart)"
        else:
            gesture = detect_gesture(fingers, lm)

        mp_drawing.draw_landmarks(
            frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
            drawing_styles, drawing_styles
        )

        wrist = (int(lm[0].x*frame.shape[1]), int(lm[0].y*frame.shape[0]))

        if mode in ("count", "both"):
            count = sum(fingers)
            total_count += count
            cv2.putText(frame, f'Count: {count}',
                        (wrist[0]-30, wrist[1]+40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 3)
        if mode in ("gesture", "both") and gesture != "Unknown":
            offset_y = wrist[1]+80 if mode=="both" else wrist[1]+40
            cv2.putText(frame, gesture,
                        (wrist[0]-30, offset_y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0,200,255), 3)
        if mode == "sign":
            # --- Minimal signs mode, with debounce
            detected = detect_easy_sign(fingers, lm)
          
            if detected and (detected != last_sign or (now - last_time > DEBOUNCE_DELAY)):
                last_sign = detected
                last_time = now
            label = last_sign if last_sign else "Not detected"
            cv2.putText(frame, f'Sign: {label}', (wrist[0]-30, wrist[1]+120),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255,240,40), 3)

    if mode in ("count", "both") and total_count > 0:
        cv2.putText(frame, f'Total: {total_count}',
                    (50,70),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 4)

    try:
        _, _, w, h = cv2.getWindowImageRect(WINDOW)
    except:
        h, w = frame.shape[:2]

    frame_resized = cv2.resize(frame, (w, h), interpolation=cv2.INTER_LINEAR)
    cv2.imshow(WINDOW, frame_resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
