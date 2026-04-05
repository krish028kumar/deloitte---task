import json
from datetime import datetime

def convert_timestamp(ts):
    if isinstance(ts, int):
        return datetime.utcfromtimestamp(ts / 1000).isoformat()
    return ts

def normalize(data):
    result = []
    for item in data:
        device_id = item.get("deviceId") or item.get("id") or item.get("device_id")
        timestamp = item.get("timestamp") or item.get("time") or item.get("ts")
        timestamp = convert_timestamp(timestamp)
        value = item.get("value") or item.get("reading") or item.get("val")

        result.append({
            "device_id": device_id,
            "timestamp": timestamp,
            "value": value
        })
    return result

def main():
    with open("data-1.json") as f:
        data1 = json.load(f)

    with open("data-2.json") as f:
        data2 = json.load(f)

    final_data = normalize(data1) + normalize(data2)
    final_data.sort(key=lambda x: x["timestamp"])

    with open("data-result.json", "w") as f:
        json.dump(final_data, f, indent=4)

    print("Done ✅")

main()
