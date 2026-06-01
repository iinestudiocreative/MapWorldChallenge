import urllib.request
import json

url = "https://raw.githubusercontent.com/geohacker/india/master/state/india_state.geojson"
print(f"Downloading {url}...")
try:
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        print("Downloaded content length:", len(content))
        data = json.loads(content)
        print("Number of features:", len(data.get("features", [])))
        with open("india_states.geojson", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Saved successfully!")
except Exception as e:
    print("Error:", e)
