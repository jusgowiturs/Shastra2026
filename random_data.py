
import urllib.request  # To make HTTP requests
import urllib.parse    # To encode URL parameters

# Step 1: Define the Write API Key and channel field
WRITE_API_KEY = "OBM1LYSTL8NMQS40"  # Replace with your Write API Key
FIELD_NUMBER = 1                     # Field you want to update

# Step 2: Ask user to input a value manually
value = input(f"Enter value to update Field {FIELD_NUMBER}: ")

# Step 3: Build the URL for ThingSpeak update
# Format: https://api.thingspeak.com/update?api_key=YOURKEY&field1=VALUE
url = f"https://api.thingspeak.com/update?api_key={WRITE_API_KEY}&field{FIELD_NUMBER}={urllib.parse.quote(value)}"

# Step 4: Send GET request to ThingSpeak
try:
    response = urllib.request.urlopen(url)
    result = response.read().decode()
    
    if result == "0":
        print("Update failed. Maybe too soon after last update (15 sec limit).")
    else:
        print(f"Successfully updated Field {FIELD_NUMBER} with value: {value}")
        print(f"Entry ID: {result}")
except Exception as e:
    print("Error updating ThingSpeak:", e)
