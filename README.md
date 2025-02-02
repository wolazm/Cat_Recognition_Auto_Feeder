# Cat Recognition Auto-Feeder

An embedded system to recognize individual cats and dispense food automatically. This project uses a Raspberry Pi, OpenCV, and a custom-trained machine learning model to identify cats and control a food dispenser.

## Features
- **Real-Time Cat Recognition**: Uses OpenCV and a trained ML model to identify cats.
- **Automatic Food Dispensing**: Controls motors and sensors to dispense food.
- **Usage Dashboard**: Tracks feeding times and usage statistics via a web-based UI.
- **Low-Power Optimization**: Designed for consistent performance on a Raspberry Pi.

## Technologies
- **Machine Learning**: TensorFlow/Keras for cat recognition.
- **Computer Vision**: OpenCV for real-time image processing.
- **Hardware**: Raspberry Pi, servo motors, and proximity sensors.
- **Web Dashboard**: Flask for the UI and logging.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cat-recognition-auto-feeder.git
   cd cat-recognition-auto-feeder
