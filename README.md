# Deloitte Forage Task - Data Integration

## 📌 Overview
This project is part of the Deloitte Forage virtual experience program.

The objective is to integrate telemetry data from two different JSON sources with different formats and produce a unified output.

---

## ⚙️ Problem Statement
- Two datasets (`data-1.json` and `data-2.json`) contain telemetry data
- Each dataset has a different structure and timestamp format
- The goal is to:
  - Normalize the data
  - Convert timestamps into ISO format
  - Merge both datasets
  - Sort the data by timestamp
  - Output the final result into `data-result.json`

---

## 🛠️ Approach
1. Load both JSON files  
2. Handle different key names dynamically  
3. Convert timestamps:
   - Milliseconds → ISO format  
   - ISO → unchanged  
4. Normalize fields into:
   - `device_id`
   - `timestamp`
   - `value`
5. Merge both datasets  
6. Sort by timestamp  
7. Save the output  

---

## ▶️ How to Run
```bash
python main.py
