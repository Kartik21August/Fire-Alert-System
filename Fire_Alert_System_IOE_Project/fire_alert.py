import time
import RPi.GPIO as GPIO
from twilio.rest import Client

flame_sensor_pin = 17
buzzer_pin = 18
led_pin = 23

account_sid = 'ACe83d72fcbe30e57bf65cb1fd9593bb11'
auth_token = 'af2be29f941e809de106f868e89fe0a8'
client = Client(account_sid, auth_token)

GPIO.setmode(GPIO.BCM)
GPIO.setup(flame_sensor_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

def detect_fire(channel):
    print("Fire detected!")
    GPIO.output(buzzer_pin, GPIO.HIGH)
    GPIO.output(led_pin, GPIO.HIGH)
    message = client.messages.create(
        from_='+12293634796',
        body='Fire detected at your place!',
        to='+918210747642'
    )
    print("SMS alert sent!")
    GPIO.output(buzzer_pin, GPIO.LOW)
    GPIO.output(led_pin, GPIO.LOW)

print("Initializing fire alarm...")
GPIO.add_event_detect(flame_sensor_pin, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(flame_sensor_pin, detect_fire)

while True:
    time.sleep(1)

13