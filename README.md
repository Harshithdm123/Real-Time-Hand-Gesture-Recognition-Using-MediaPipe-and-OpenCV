# Hand Gesture Recognition Using MediaPipe and OpenCV

This project implements a real-time hand gesture recognition system using MediaPipe's Hand module and OpenCV. It detects and tracks hand landmarks from a live video feed, counts the number of raised fingers, and provides a visual display with bounding boxes and hand annotations.
Features

    Real-time detection and tracking of hands.
    Counts the number of raised fingers for each detected hand.
    Displays bounding boxes and hand landmarks for better visualization.
    Optimized for performance using frame skipping.

## Requirements

Ensure you have the following installed on your system:

    Python 3.7+
    OpenCV
    MediaPipe
    NumPy

## Installation
Step 1: Clone the Repository

git clone https://github.com/Harshithdm123/hand-gesture-recognitio.git
cd hand-gesture-recognition

Step 2: Install Dependencies

pip install opencv-python mediapipe numpy
python3 app.py

## How to Run the Project

    Ensure your webcam is connected and accessible.
    Run the script using the command:

    python hand_gesture_recognition.py

    A window will open displaying the live feed with detected hand gestures.
    Press 'q' to quit the application.

## How It Works

    Hand Detection: The application uses MediaPipe to detect hand landmarks in real-time.
    Finger Counting: It checks the position of finger tips relative to other joints to count raised fingers.
    Visual Feedback: Hand landmarks, bounding boxes, and finger count text are overlaid on the video feed.

## Project Files

    hand_gesture_recognition.py: Main Python script for the project.
    README.md: Documentation for the project.

Example Output

## The application displays:

    Detected hand(s) labeled as "Left Hand" or "Right Hand."
    Number of fingers raised for each hand.
    Bounding boxes around the detected hands for clarity.

## Troubleshooting

    Camera Not Detected: Ensure the webcam is connected and accessible. Verify it with other applications.
    Module Errors: If dependencies are missing, ensure you’ve installed them using the command:

    pip install opencv-python mediapipe numpy

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software.
