import json

def inspect_geojson(path):
    print(f"=== {path} ===")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    features = data.get("features", [])
    if not features:
        print("No features!")
        return
    print(f"Total features: {len(features)}")
    first_feat = features[0]
    print("Geometry type:", first_feat.get("geometry", {}).get("type"))
    print("Properties keys:", list(first_feat.get("properties", {}).keys()))
    print("First feature properties sample:", first_feat.get("properties", {}))

inspect_geojson("mexico_states.geojson")
inspect_geojson("turkey_provinces.geojson")
