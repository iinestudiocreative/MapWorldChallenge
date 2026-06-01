import json

with open("../korea_provinces.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)
    
features = data.get("features", [])
print(f"Total features: {len(features)}")
provinces = []
for feat in features:
    props = feat.get("properties", {})
    provinces.append({
        "id": props.get("ID_1"),
        "name": props.get("NAME_1"),
        "engtype": props.get("ENGTYPE_1")
    })

# Sort by id
provinces.sort(key=lambda x: x["id"] or 0)
for p in provinces:
    print(f"'{p['id']}': '{p['name']}' ({p['engtype']})")
