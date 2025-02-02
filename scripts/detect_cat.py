import cv2
import tensorflow as tf
from hardware.motor_control import dispense_food
import time
import pandas as pd
from datetime import datetime

# Load the trained model
model = tf.keras.models.load_model('../models/cat_recognition_model.h5')

# Initialize camera
cap = cv2.VideoCapture(0)

# Ensure the logs directory exists
os.makedirs('../logs', exist_ok=True)

# Log file path
log_file = '../logs/feeding_logs.csv'

# Function to log feeding events
def log_feeding(cat_detected):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = {'timestamp': timestamp, 'cat_detected': cat_detected}
    df = pd.DataFrame([log_entry])
    df.to_csv(log_file, mode='a', header=not os.path.exists(log_file), index=False)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image.")
            break

        # Preprocess the frame for the model
        resized_frame = cv2.resize(frame, (150, 150))
        normalized_frame = resized_frame / 255.0
        input_frame = tf.expand_dims(normalized_frame, axis=0)

        # Predict
        prediction = model.predict(input_frame)
        cat_detected = prediction > 0.5

        if cat_detected:
            print("Cat detected! Dispensing food.")
            dispense_food()
            log_feeding(True)
        else:
            print("No cat detected.")
            log_feeding(False)

        # Display the frame
        cv2.imshow('Cat Detection', frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()