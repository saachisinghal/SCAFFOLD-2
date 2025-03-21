from machine import Pin, PWM
import neopixel
import time

# Setup Servo on GPIO23 with 50Hz frequency
servo = PWM(Pin(23), freq=50)

# Setup NeoPixel on GPIO22 with 16 LEDs
n = 16  # Number of LEDs
np = neopixel.NeoPixel(Pin(22), n)

def set_angle(angle):
    """Move SG90 servo to a specific angle (0-180°)"""
    min_duty = 2000  # Duty cycle for 0°
    max_duty = 8000  # Duty cycle for 180°

    # Convert angle (0-180) to duty cycle
    duty = int((angle / 180) * (max_duty - min_duty) + min_duty)

    servo.duty_u16(duty)  # Move servo
    time.sleep(0.1)  # Wait for movement

while True:
    set_angle(0)   # Move servo to 0°
    np.fill((0, 0, 0))  # Turn off NeoPixels
    np.write()
    time.sleep(0.5)

    set_angle(120)  # Move servo to 120°
    np.fill((0, 255, 0))  # Turn NeoPixels Green after 120°
    np.write()

    time.sleep(4)
    set_angle(0)

      # Move back to 0°
    time.sleep(4)
