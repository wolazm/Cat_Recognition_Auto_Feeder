import RPi.GPIO as GPIO
import time

# GPIO setup
MOTOR_PIN = 18  # GPIO pin connected to the servo motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN, GPIO.OUT)

# Initialize PWM for the servo motor
pwm = GPIO.PWM(MOTOR_PIN, 50)  # 50 Hz frequency
pwm.start(0)  # Start with 0% duty cycle

def dispense_food():
    """
    Activates the servo motor to dispense food.
    """
    print("Dispensing food...")
    try:
        # Rotate the servo to dispense food
        pwm.ChangeDutyCycle(7.5)  # 7.5% duty cycle (90 degrees)
        time.sleep(2)  # Wait for 2 seconds
        pwm.ChangeDutyCycle(2.5)  # 2.5% duty cycle (0 degrees)
        time.sleep(1)  # Wait for 1 second
    except Exception as e:
        print(f"Error controlling motor: {e}")
    finally:
        pwm.ChangeDutyCycle(0)  # Stop the motor
        print("Food dispensed.")

def cleanup():
    """
    Cleans up the GPIO pins.
    """
    pwm.stop()
    GPIO.cleanup()
    print("GPIO cleanup complete.")

if __name__ == "__main__":
    try:
        dispense_food()
    finally:
        cleanup()