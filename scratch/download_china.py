import urllib.request
import json
import os

# Let's try longwosion's master/china.json
url = "https://raw.githubusercontent.com/longwosion/geojson-map-china/master/china.json"
dest = "../china_provinces.geojson"

print(f"Downloading China provinces GeoJSON from {url}...")
try:
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        
    features = data.get("features", [])
    print(f"Successfully downloaded! Found {len(features)} territories.")
    
    # Print properties of the first feature to see keys
    if features:
        print("First feature properties:", features[0].get("properties"))
        
    # Save the file
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    print(f"Saved to {os.path.abspath(dest)}.")
except Exception as e:
    print(f"Error downloading: {e}")
