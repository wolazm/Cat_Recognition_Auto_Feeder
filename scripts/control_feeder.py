import RPi.GPIO as GPIO
import time

# GPIO setup
MOTOR_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN, GPIO.OUT)

def dispense_food():
    """Activates the motor to dispense food."""
    print("Dispensing food...")
    GPIO.output(MOTOR_PIN, GPIO.HIGH)
    time.sleep(2)  # Dispense food for 2 seconds
    GPIO.output(MOTOR_PIN, GPIO.LOW)
    print("Food dispensed.")

if __name__ == '__main__':
    try:
        dispense_food()
    finally:
        GPIO.cleanup()