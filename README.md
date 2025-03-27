Vision Assistant

# Imprtant ADD YOUR GEMINI API OCR.py

Vision Assistant is a real-time object detection and OCR (Optical Character Recognition) system designed to assist visually impaired users or anyone needing visual context. It uses WebRTC for video streaming, YOLO for object detection, and Google's Gemini API for OCR, with a client-server architecture.
Features

    Object Detection: Identifies priority objects (e.g., people, cars, stop signs) with position and distance estimation using YOLOv10.
    OCR: Extracts text from video frames using Google's Gemini API.
    Real-Time Streaming: Streams video from a sender (e.g., mobile device) to a receiver for processing via WebRTC.
    Voice Feedback: Provides audio descriptions of detected objects or text.
    Mode Switching: Toggle between object detection and OCR modes dynamically.

Project Structure
text
vision-assistant/
├── public/
│   ├── sender.html      # Client-side interface for video capture
│   └── receiver.html    # Server-side interface for video processing
├── detector.py          # Object detection backend (YOLO)
├── ocr.py               # OCR backend (Gemini API)
├── server.js            # Node.js server for WebRTC signaling and proxying
├── requirements.txt     # Python dependencies
├── package.json         # Node.js dependencies
└── README.md            # Project documentation
Prerequisites

    Python 3.8+: For running detector.py and ocr.py.
    Node.js 18+: For running server.js.
    Google API Key: For OCR functionality (Gemini API).
    YOLO Model: Download yolov10x.pt (or another YOLO model) from Ultralytics.

Installation
1. Clone the Repository
bash
git clone https://github.com/Beastop33/Nexvision.git
cd NexVision
2. Set Up Python Environment

Install Python dependencies:
bash
pip install -r requirements.txt

    Place your YOLO model file (e.g., yolov10x.pt) in the project root or update the path in detector.py.
    Replace the GOOGLE_API_KEY placeholder in ocr.py with your actual Google API key.

3. Set Up Node.js Environment

Install Node.js dependencies:
bash
npm install
4. Directory Setup

Ensure the public folder contains sender.html and receiver.html.
Running the Application

    Start the Object Detection Server:
    bash

python detector.py

    Runs on http://localhost:5000.

Start the OCR Server:
bash
python ocr.py

    Runs on http://localhost:5001.

Start the Node.js Server:
bash

    node server.js
        Runs on http://localhost:3000.
    Access the Interfaces:
        Sender: Open http://localhost:3000/sender in a browser (e.g., on a mobile device) to capture and send video.
        Receiver: Open http://localhost:3000/receiver in another browser to process and display results.

Usage

    Sender Interface:
        Grant camera access when prompted.
        Use the "Switch to OCR Mode" button to toggle between object detection and OCR.
        In OCR mode, use "Restart OCR" to clear previous results.
        Audio feedback will describe detected objects or text.
    Receiver Interface:
        Displays the video stream and processing status (Signaling, ICE, Track).
        Shows real-time detection results or extracted text.

How It Works

    The sender captures video using the browser's camera and streams it to the receiver via WebRTC.
    The receiver processes each frame:
        For object detection, it sends frames to detector.py (port 5000).
        For OCR, it sends frames to ocr.py (port 5001).
    Results are sent back to the sender via a WebRTC data channel and spoken aloud.

Dependencies
Python

    opencv-python: Image processing.
    torch, ultralytics: YOLO model for object detection.
    fastapi, uvicorn: API servers.
    google-generativeai: OCR via Gemini API.
    See requirements.txt for full list.

Node.js

    express, socket.io: Web server and WebRTC signaling.
    http-proxy-middleware: Proxy requests to Python backends.
    See package.json for full list.

Troubleshooting

    Camera Access Denied: Ensure browser permissions are granted.
    Connection Issues: Check that all servers are running and ports (3000, 5000, 5001) are not blocked.
    Gemini API Errors: Verify your API key and network connectivity.
    YOLO Model Missing: Download the model file and update the path in detector.py.

Contributing

    Fork the repository.
    Create a feature branch (git checkout -b feature-name).
    Commit changes (git commit -m "Add feature").
    Push to the branch (git push origin feature-name).
    Open a pull request.

License

This project is licensed under the MIT License - see the  file for details (create one if needed).
Acknowledgments

    Ultralytics YOLO for object detection.
    Google Gemini API for OCR capabilities.
    Socket.IO and WebRTC for real-time communication.

Notes:

    Replace username in the clone URL with your GitHub username.
    If you want to add a license, create a LICENSE file with the MIT License text (or your preferred license).
    Adjust any paths or details (e.g., YOLO model name) based on your specific setup.

Let me know if you'd like to tweak this further!
