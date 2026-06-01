import urllib.request
import json
import os

def download_file(url, out_path):
    print(f"Downloading {url} -> {out_path}...")
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Successfully downloaded {len(data.get('features', []))} features to {out_path}!")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

download_file(
    "https://raw.githubusercontent.com/rowanhogan/australian-states/master/states.geojson",
    "australia_states.geojson"
)
download_file(
    "https://raw.githubusercontent.com/geohacker/india/master/state/india_state.geojson",
    "india_states.geojson"
)
