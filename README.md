# Driver_Drowsiness_Detection
# Overview  
Hey Reader! This project is a real-time driver drowsiness detection system that uses a webcam to monitor the driver’s facial features. It tracks eye movement and detects fatigue by calculating the Eye Aspect Ratio (EAR). When drowsiness is detected, the system gives a visual warning (red bounding box) and sounds an alert buzzer. It aims to reduce road accidents caused by driver fatigue.
# Features 
- Face and Eye Detection: Uses MediaPipe to identify facial landmarks  
- Eye Aspect Ratio (EAR): Calculates EAR to detect drowsy eye closures  
- Red/Green Bounding Box: Red when drowsy, green when good  
- Buzzer Alert: Plays a buzzer sound when drowsiness is detected  
- Real-Time Monitoring: Continuously evaluates driver state from webcam feed  
- Clean Interface: Simple visual output using OpenCV  
- No Cloud Dependency: Runs completely offline for privacy and speed  
# Installation  
Ensure you have Python installed (recommended: Python 3.9+). You’ll also need some essential libraries for image processing, facial landmark detection, and sound playback. The recommended way to install them is using the commands below.
# Required Libraries
opencv-python – For video capture and drawing overlays<br>
(pip install opencv-python)<br>
mediapipe – For facial landmark detection<br>
(pip install mediapipe)<br>
numpy – For numerical operations<br>
(pip install numpy)<br>
scipy – For calculating distances (used in EAR formula)<br>
(pip install scipy)<br>
winsound – For playing buzzer sound (no install needed, built-in for Windows)<br>
# How It Works  
- Starts webcam feed and detects face and eye landmarks  
- Calculates Eye Aspect Ratio (EAR) every frame  
- If EAR drops below a defined threshold i.e. 0.25, triggers drowsiness alert  
- Draws a red bounding box and plays a continuous buzzer sound until eyes reopen  
# File Requirements  
- (sound.wav): A short buzzer ".wav" file placed in the same folder as the script  
- (main.py): Your driver drowsiness detection script  
# Conclusion  
Hope this project helps you understand and build intelligent real-time computer vision systems. It's a small step toward safer driving. Contributions and feedback are always welcome!
