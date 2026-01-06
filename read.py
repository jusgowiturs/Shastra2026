 cat read.py
# ====================================================
# ThingSpeak Data Reader – Python Example
# Reads numeric data from Field 1 of a ThingSpeak channel
# ====================================================

# Step 1: Import required libraries
import urllib.request  # Used to make HTTP requests
import json            # Used to parse JSON responses

# Step 2: Define the ThingSpeak API URL
# Replace with your channel ID and Read API Key
# 'results=5' fetches the last 5 entries
# THINGSPEAK_URL = "https://api.thingspeak.com/channels/2802390/fields/1.json?api_key=4QTWQ1O3US1YYRA8&results=5"
THINGSPEAK_URL = "<YOUR_THINGSPEAK_URL_HERE>"
# Step 3: Fetch data from ThingSpeak
# urllib.request.urlopen sends a GET request to the URL
response = urllib.request.urlopen(THINGSPEAK_URL)

# Step 4: Parse the JSON response into a Python dictionary
data = json.loads(response.read())

# Step 5: Extract the 'feeds' list which contains all entries
feeds = data.get('feeds', [])

# Step 6: Loop through each entry and print timestamp and value
print("Latest ThingSpeak Field 1 Data:")
print("-" * 40)
for entry in feeds:
    created_at = entry.get('created_at')  # Timestamp of the entry
    field1_value = entry.get('field1')    # Value stored in Field 1
    print(f"Time: {created_at} | Field 1 Value: {field1_value}")

# Step 7: Optional – Store all numeric values in a list for further analysis
# Converts field values to float, ignores None entries
values = [float(entry['field1']) for entry in feeds if entry['field1'] is not None]

# Step 8: Print the list of values
print("\nField 1 values as a list:", values)

# Step 9: Optional – Simple analysis
if values:
    avg_value = sum(values) / len(values)
    max_value = max(values)
    min_value = min(values)
    print(f"\nAverage: {avg_value}, Max: {max_value}, Min: {min_value}")