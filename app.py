try:
    import cv2
    import mediapipe as mp
    import numpy as np
except ModuleNotFoundError:
    print("Error: Required module not found.")
    print("Make sure you have installed the required modules using:")
    print("pip install opencv-python mediapipe numpy")
    exit()

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, 
                       max_num_hands=2, 
                       min_detection_confidence=0.85, 
                       min_tracking_confidence=0.85)

# Finger tip landmarks (index in MediaPipe Hands)
FINGER_TIPS = [4, 8, 12, 16, 20]

# Start capturing video
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

print("Press 'q' to quit the program.")

frame_counter = 0  # Used to skip frames for optimization

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame from the camera.")
        break

    # Skip frames for optimization
    frame_counter += 1
    if frame_counter % 2 != 0:
        continue

    # Flip the frame horizontally for a mirrored view
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    # Draw landmarks and count fingers if hands are detected
    if results.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            # Draw hand landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmark positions
            landmarks = hand_landmarks.landmark

            # Count fingers
            fingers_up = 0
            for tip_index in FINGER_TIPS:
                if tip_index != 4:  # Check fingers (except thumb)
                    if landmarks[tip_index].y < landmarks[tip_index - 2].y:  # Tip above lower joint
                        fingers_up += 1
                else:  # Check thumb (consider orientation)
                    wrist_x = landmarks[0].x
                    thumb_tip_x = landmarks[tip_index].x
                    if thumb_tip_x < wrist_x:  # Adjust threshold dynamically
                        fingers_up += 1

            # Determine finger count text
            hand_label = "Left Hand" if idx == 0 else "Right Hand"
            finger_text = f"{hand_label}: {fingers_up} fingers"
            
            # Display finger count
            cv2.putText(frame, finger_text, (10, 50 + idx * 30), cv2.FONT_HERSHEY_SIMPLEX, 
                        1, (0, 255, 0), 2)

            # Draw bounding box around the hand for better visibility
            h, w, _ = frame.shape
            x_min = int(min([lm.x for lm in landmarks]) * w)
            y_min = int(min([lm.y for lm in landmarks]) * h)
            x_max = int(max([lm.x for lm in landmarks]) * w)
            y_max = int(max([lm.y for lm in landmarks]) * h)
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 255), 2)

    # Display the frame
    cv2.imshow('Hand Gesture Recognition', frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
