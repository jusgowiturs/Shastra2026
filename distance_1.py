import urllib.request
import urllib.parse
import json
import time
import RPi.GPIO as GPIO
import config

# ===============================
# ThingSpeak Configuration
# ===============================
CHANNEL_ID = "3220382"
FIELD_NUMBER = 2
WRITE_API_KEY = config.WRITE_API_KEY
READ_API_KEY = config.READ_API_KEY
RESULTS = 1

# ===============================
# GPIO Configuration
# ===============================
TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# ===============================
# Distance Function (Safe)
# ===============================
def get_distance():
    timeout = 1
    GPIO.output(TRIG, False)
    time.sleep(0.05)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start = time.time()

    while GPIO.input(ECHO) == 0:
        if time.time() - start > timeout:
            return None

    pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        if time.time() - pulse_start > timeout:
            return None

    pulse_end = time.time()
    distance = (pulse_end - pulse_start) * 17150
    return round(distance, 2)

# ===============================
# Push to ThingSpeak
# ===============================
def push_to_thingspeak(value):
    valueencoded = urllib.parse.quote(str(value))
    url = (
        f"https://api.thingspeak.com/update?"
        f"api_key={WRITE_API_KEY}&field{FIELD_NUMBER}={valueencoded}"
    )

    response = urllib.request.urlopen(url)
    result = response.read().decode()

    if result == "0":
        print("❌ Push failed (15 sec rate limit)")
    else:
        print(f"✅ Data pushed successfully | Entry ID: {result}")

# ===============================
# Read from ThingSpeak (VERIFY)
# ===============================
def read_from_thingspeak():
    url = (
        f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/"
        f"{FIELD_NUMBER}.json?api_key={READ_API_KEY}&results={RESULTS}"
    )

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    feeds = data.get("feeds", [])

    print("\n ThingSpeak Data Verification")
    print("-" * 45)

    if not feeds:
        print("No data found.")
        return

    for entry in feeds:
        print(
            f"Time: {entry.get('created_at')} | "
            f"Value: {entry.get(f'field{FIELD_NUMBER}')}"
        )

# ===============================
# MAIN
# ===============================
try:
    distance = get_distance()

    if distance is None:
        print(" Distance measurement failed")
    else:
        print(f" Distance = {distance} cm")
        push_to_thingspeak(distance)

    time.sleep(2)   # small delay before reading
    read_from_thingspeak()

finally:
    GPIO.cleanup()
