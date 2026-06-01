import json
import math

def simplify_polygon(poly, tolerance):
    if not poly:
        return []
    simplified = [poly[0]]
    for pt in poly[1:]:
        d = math.hypot(pt[0] - simplified[-1][0], pt[1] - simplified[-1][1])
        if d >= tolerance:
            simplified.append(pt)
    if len(simplified) > 1 and simplified[-1] != poly[-1]:
        simplified.append(poly[-1])
    return simplified

def main():
    with open("prefectures.geojson", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    all_polys = []
    # Extract all polygons from multipolygons
    for feat in data.get("features", []):
        geom = feat.get("geometry", {})
        gtype = geom.get("type")
        coords = geom.get("coordinates", [])
        
        if gtype == "Polygon":
            if coords:
                all_polys.append(coords[0])
        elif gtype == "MultiPolygon":
            for poly in coords:
                if poly:
                    all_polys.append(poly[0])

    # Filter out extremely small islands to keep the silhouette clean and fast to load
    filtered_polys = []
    for poly in all_polys:
        if len(poly) < 3:
            continue
        xs = [p[0] for p in poly]
        ys = [p[1] for p in poly]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        area_bbox = (max_x - min_x) * (max_y - min_y)
        # Skip tiny islands but keep Okinawa and main islands
        if area_bbox > 0.05 or (max_x < 130 and max_y < 27 and area_bbox > 0.005): # Keep Okinawa!
            filtered_polys.append(poly)

    # Simplify all polygons
    tolerance = 0.16  # Perfect balance for high-res silhouette
    simplified_polys = []
    total_points = 0
    for poly in filtered_polys:
        sim = simplify_polygon(poly, tolerance)
        if len(sim) >= 3:
            simplified_polys.append(sim)
            total_points += len(sim)

    # Convert all lons and lats to projected coords
    def lat_to_merc(lat):
        lat_rad = math.radians(lat)
        return math.log(math.tan(lat_rad / 2.0 + math.pi / 4.0))

    projected_polys = []
    for poly in simplified_polys:
        proj_poly = []
        for pt in poly:
            lon = pt[0]
            lat = pt[1]
            x_proj = lon
            y_proj = lat_to_merc(lat)
            proj_poly.append((x_proj, y_proj))
        projected_polys.append(proj_poly)

    # Find bbox of projected coords
    proj_xs = [pt[0] for poly in projected_polys for pt in poly]
    proj_ys = [pt[1] for poly in projected_polys for pt in poly]
    
    p_min_x, p_max_x = min(proj_xs), max(proj_xs)
    p_min_y, p_max_y = min(proj_ys), max(proj_ys)
    
    p_w = p_max_x - p_min_x
    p_h = p_max_y - p_min_y
    
    # Scale factor preserving aspect ratio
    padding = 6
    box_size = 100 - 2 * padding
    scale = min(box_size / p_w, box_size / p_h)
    
    # Centering
    x_offset = padding + (box_size - p_w * scale) / 2
    y_offset = padding + (box_size - p_h * scale) / 2
    
    # Convert to SVG path commands
    path_cmds = []
    for poly in projected_polys:
        cmds = []
        for i, pt in enumerate(poly):
            # Scale and translate
            x = x_offset + (pt[0] - p_min_x) * scale
            # Invert Y because SVG Y increases downwards, but Mercator Y increases upwards
            y = 100 - (y_offset + (pt[1] - p_min_y) * scale)
            
            cmd_char = "M" if i == 0 else "L"
            cmds.append(f"{cmd_char} {x:.1f} {y:.1f}")
        cmds.append("Z")
        path_cmds.append(" ".join(cmds))
        
    svg_path_d = " ".join(path_cmds)
    
    with open("scratch/japan_path.txt", "w", encoding="utf-8") as out:
        out.write(svg_path_d)

if __name__ == "__main__":
    main()
