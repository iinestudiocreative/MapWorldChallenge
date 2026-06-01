import urllib.request
import json
import os

url = "https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_20m.json"
dest = "../usa_states.geojson"

print(f"Downloading US states GeoJSON from {url}...")
try:
    # Set a user-agent to avoid blockages
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        
    # Check features count
    features = data.get("features", [])
    print(f"Successfully downloaded! Found {len(features)} territories.")
    
    # Save the file
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    print(f"Saved to {os.path.abspath(dest)}.")
except Exception as e:
    print(f"Error downloading: {e}")
