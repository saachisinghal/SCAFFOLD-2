from machine import Pin, PWM
import time

# Setup servo on GPIO15 with 50Hz frequency
servo = PWM(Pin(5), freq=50)

def set_angle(angle):
    """Move SG90 servo to a specific angle (0-180°)"""
    min_duty = 2000  # Duty cycle for 0°
    max_duty = 8000  # Duty cycle for 180°

    # Convert angle (0-180) to duty cycle
    duty = int((angle / 180) * (max_duty - min_duty) + min_duty)

    servo.duty_u16(duty)  # Move servo
    time.sleep(0.1)  # Wait for movement

while True:
    set_angle(30)   # Move to 0°
    time.sleep(0.5)
    set_angle(120)  # Move to 90°
    time.sleep(0.5)
    set_angle(30)   # Move back to 0°
    time.sleep(0.1)
