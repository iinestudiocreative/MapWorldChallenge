import re
import json

def extract_geojson(md_path, out_path):
    print(f"Extracting {md_path} -> {out_path}...")
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find the start of the JSON block
    match = re.search(r'^\s*\{', content, re.MULTILINE)
    if not match:
        raise ValueError("Could not find start of JSON in markdown file!")
    
    json_str = content[match.start():].strip()
    
    # Parse to validate
    data = json.loads(json_str)
    
    # Save as clean json
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Successfully extracted {len(data.get('features', []))} features to {out_path}!")

try:
    extract_geojson(
        "/Users/willkyandi/.gemini/antigravity/brain/5e626fdf-f35b-47d0-b188-0454ba00e265/.system_generated/steps/4771/content.md",
        "australia_states.geojson"
    )
    extract_geojson(
        "/Users/willkyandi/.gemini/antigravity/brain/5e626fdf-f35b-47d0-b188-0454ba00e265/.system_generated/steps/4783/content.md",
        "india_states.geojson"
    )
except Exception as e:
    print("Error during extraction:", e)
