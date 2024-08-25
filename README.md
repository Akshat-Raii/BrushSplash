# Brush Splash 🖐️✍️

Welcome to the Brush Splash! This project utilizes hand tracking technology to create an interactive drawing app where you can draw and select colors using hand gestures.

## Features 🎨

- **Draw on Canvas**: Use your fingers to draw on the screen.
- **Color Selection**: Change colors by pointing at the color palette.
- **Eraser**: Switch to eraser mode by using specific gestures.

## Requirements 📦

Ensure you have the following libraries installed:

- `opencv-python` for video processing.
- `mediapipe` for hand tracking.
- `numpy` for handling arrays.
- `os` for file operations.

You can install the required libraries using the `requirements.txt` file provided.

## Installation 📥

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

## Usage 🚀

1.**Run the Brush Splash Application:**
  ```bash
  python brushSplash.py
  ```
This will open a window where you can use your hand gestures to draw, select colors, and erase.

## Code Overview 🧩
handTrackingModule.py
This module contains the handDetector class for detecting and tracking hand gestures using MediaPipe.

brushSplash.py
This script utilizes the handDetector class to create an interactive drawing application where users can draw, select colors, and erase based on hand gestures.

## Key Functions 🔍
1.**findHands(img, draw=True)**: Detects hands in the given image. <br><br>
2.**findPosition(img, handNo=0, draw=True)**: Finds the positions of landmarks for a specific hand. <br><br>
3.**fingersUp()**: Returns a list indicating which fingers are up.<br><br>

## Troubleshooting 🛠️
1.Camera Access: Ensure your camera is working and accessible.<br><br>
2.Dependencies: Verify that all required libraries are installed.
