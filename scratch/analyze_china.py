import json

with open("../china_provinces.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)
    
features = data.get("features", [])
print(f"Total features: {len(features)}")
provinces = []
for feat in features:
    props = feat.get("properties", {})
    provinces.append({
        "id": props.get("id"),
        "name": props.get("name"),
        "cp": props.get("cp")
    })

# Sort by id
provinces.sort(key=lambda x: x["id"] or "")
for p in provinces:
    print(f"'{p['id']}': '{p['name']}', cp: {p['cp']}")
