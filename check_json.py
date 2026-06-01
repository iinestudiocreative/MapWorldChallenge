import json

try:
    with open("india_states.geojson", "r", encoding="utf-8") as f:
        data = json.load(f)
    features = data.get("features", [])
    for f in features:
        props = f.get("properties", {})
        print(f"ID_1: {props.get('ID_1')}, NAME_1: {props.get('NAME_1')}")
except Exception as e:
    print("Error:", e)




