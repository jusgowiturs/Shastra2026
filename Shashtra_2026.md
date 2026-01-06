C:\Users\NPTEL\.ssh\known_hosts



GPIO
URLLIB.REQUEST
TIME
GPIO MODE
BCM
BOARD
API key generation


Online cloud
THinkspeak
https://thingspeak.mathworks.com/


To Write
# ThingSpeak API – Write & Read Operations

---

## 📤 Write Data to ThingSpeak

### ✅ URL

GET https://api.thingspeak.com/update?api_key=OBM1LYSTL8NMQS40&field1=0

To Read 

### 🔍 Explanation
- `update` → Used to upload data
- `api_key` → **Write API Key**
- `field1=0` → Value sent to Field 1

### 📌 Notes
- Uploads one data entry
- Minimum **15 seconds** delay between updates
- Returns an **entry ID** if successful

---

## 📥 Read Data from ThingSpeak

---

### 1️⃣ Read All Fields (Latest Entries)

### ✅ URL

GET https://api.thingspeak.com/channels/2802390/feeds.json?api_key=4QTWQ1O3US1YYRA8&results=2


### 🔍 Explanation
- `fields/1.json` → Fetches only Field 1 data
- `results=2` → Last 2 values

### 📌 Output
- JSON format
- Only Field 1 values returned

---

GET https://api.thingspeak.com/channels/2802390/fields/1.json?api_key=4QTWQ1O3US1YYRA8&results=2

---

### 🔍 URL Breakdown

| Component | Description |
|---------|-------------|
| `GET` | HTTP method used to request data |
| `api.thingspeak.com` | ThingSpeak server (host) |
| `channels/2802390` | Unique **Channel ID** |
| `fields/1.json` | Requests data from **Field 1** only |
| `api_key` | **Read API Key** (authentication) |
| `results=2` | Returns the **last 2 entries** |

---

### 📌 What This Request Does

- Retrieves the **latest 2 values** from **Field 1**
- Data is returned in **JSON format**
- Includes:
  - Field values
  - Entry IDs
  - Timestamps

---

### 📊 Output Format (JSON)

```json
{
  "channel": {
    "id": 2802390,
    "field1": "Temperature"
  },
  "feeds": [
    {
      "created_at": "2026-01-01T10:00:00Z",
      "entry_id": 10,
      "field1": "25"
    },
    {
      "created_at": "2026-01-01T09:59:45Z",
      "entry_id": 9,
      "field1": "24"
    }
  ]
}

### 3️⃣ Read Channel Status

### ✅ URL

GET https://api.thingspeak.com/channels/2802390/status.json?api_key=4QTWQ1O3US1YYRA8


### 🔍 Explanation
- `status.json` → Channel status information
- `api_key` → **Read API Key**

### 📌 Output
- Channel status message
- Metadata (if configured)

---

## 🔑 API Key Usage

| Operation | URL Endpoint | API Key Type |
|----------|--------------|--------------|
| Write data | `/update` | Write API Key |
| Read all fields | `/feeds.json` | Read API Key |
| Read single field | `/fields/1.json` | Read API Key |
| Read channel status | `/status.json` | Read API Key |

---

## ⚠️ Important Rules

- Use **Write API Key** only for uploading data
- Use **Read API Key** only for reading data
- Minimum **15 seconds** interval between updates
- Data is returned in **JSON format**

---

## 🧠 Exam-Oriented Summary

> ThingSpeak uses HTTP GET requests where the Write API key uploads sensor data using the update endpoint, and the Read API key retrieves channel data in JSON format.

---
