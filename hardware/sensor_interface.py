import RPi.GPIO as GPIO
import time

# GPIO setup
SENSOR_PIN = 24  # GPIO pin connected to the proximity sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

def check_food_level():
    """
    Checks the food level using the proximity sensor.
    Returns True if food is detected, False otherwise.
    """
    try:
        food_detected = GPIO.input(SENSOR_PIN)
        if food_detected:
            print("Food level is sufficient.")
        else:
            print("Food level is low. Please refill.")
        return food_detected
    except Exception as e:
        print(f"Error reading sensor: {e}")
        return False

def cleanup():
    """
    Cleans up the GPIO pins.
    """
    GPIO.cleanup()
    print("GPIO cleanup complete.")

if __name__ == "__main__":
    try:
        while True:
            check_food_level()
            time.sleep(5)  # Check food level every 5 seconds
    except KeyboardInterrupt:
        print("Stopping sensor monitoring.")
    finally:
        cleanup()