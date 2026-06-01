import re

def main():
    # 1. Read the new optimized Japan SVG path
    with open("scratch/japan_path.txt", "r", encoding="utf-8") as f:
        new_jp_path = f.read().strip()
    
    # 2. Read update_app.py
    with open("update_app.py", "r", encoding="utf-8") as f:
        content = f.read()

    # ─── PART 1: Replace Japan Silhouette SVG ───────────────────
    # We look for cardFlag.innerHTML = '<svg ...><path d="[OLD_PATH]" /></svg>';
    # Old path starts with M 48.0 18.4 L 49.5 9.3 ... and ends with L 7.9 75.2 L 9.9 74.3 L 7.9 75.2 Z
    old_flag_pattern = r"cardFlag\.innerHTML = '<svg[^>]*><path d=\"M 48\.0 18\.4[^\"]+\" /></svg>';"
    replacement_flag = f"cardFlag.innerHTML = '<svg width=\"1em\" height=\"1em\" viewBox=\"0 0 100 100\" style=\"vertical-align: middle; fill: #ffffff; display: inline-block; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.25));\"><path d=\"{new_jp_path}\" /></svg>';"
    
    if re.search(old_flag_pattern, content):
        content = re.sub(old_flag_pattern, replacement_flag, content)
        print("Success: Japan flag SVG replacement injected in memory!")
    else:
        # Let's try a simpler regex or direct replacement if it varies slightly
        print("Warning: Flag SVG pattern not matched exactly by regex.")
        # Fallback search
        fallback_str = 'cardFlag.innerHTML = \'<svg width="1em" height="1em" viewBox="0 0 100 100" style="vertical-align: middle; fill: #ffffff; display: inline-block; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.25));\"><path d="M 48.0 18.4'
        idx = content.find(fallback_str)
        if idx != -1:
            # find end of line
            end_idx = content.find("';", idx)
            if end_idx != -1:
                old_line = content[idx:end_idx+2]
                content = content.replace(old_line, replacement_flag)
                print("Success: Japan flag SVG replacement injected via fallback!")
            else:
                print("Error: Could not find end of flag line.")
        else:
            print("Error: Could not find flag line at all.")

    # ─── PART 2: Move Okinawa Inset Click Helper to be LAST ─────
    # We want to change:
    #   if (okinawaFeature) {
    #     const gOk = svg.append("g")
    #       .attr("class", "cell-group")
    #       .attr("data-code", "47")
    #       .style("cursor", "pointer")
    #       .on("click", (event) => {
    #         if (event.defaultPrevented) return;
    #         openModal("47");
    #       });
    #
    #     // Transparent click helper covering the entire inset box for easy tapping
    #     gOk.append("rect")
    #       .attr("x", OX)
    #       .attr("y", OY)
    #       .attr("width", OW)
    #       .attr("height", OH)
    #       .attr("fill", "rgba(0,0,0,0)")
    #       .style("cursor", "pointer");
    #
    #     const localProjection = d3.geoIdentity()
    #       .fitExtent([[OX + 6, OY + 6], [OX + OW - 6, OY + OH - 20]], okinawaFeature);
    #
    #     const localPath = d3.geoPath().projection(localProjection);
    #
    #     gOk.append("path")
    #       .attr("class", "cell-path")
    #       .attr("data-code", "47")
    #       .attr("d", localPath(okinawaFeature))
    #       .attr("fill", COLORS[state.levels["47"] || 0])
    #       .attr("stroke", "#ffffff")
    #       .attr("stroke-width", 0.7);
    #   }
    #
    # TO:
    #   if (okinawaFeature) {
    #     const gOk = svg.append("g")
    #       .attr("class", "cell-group")
    #       .attr("data-code", "47")
    #       .style("cursor", "pointer")
    #       .on("click", (event) => {
    #         if (event.defaultPrevented) return;
    #         openModal("47");
    #       });
    #
    #     const localProjection = d3.geoIdentity()
    #       .fitExtent([[OX + 6, OY + 6], [OX + OW - 6, OY + OH - 20]], okinawaFeature);
    #
    #     const localPath = d3.geoPath().projection(localProjection);
    #
    #     gOk.append("path")
    #       .attr("class", "cell-path")
    #       .attr("data-code", "47")
    #       .attr("d", localPath(okinawaFeature))
    #       .attr("fill", COLORS[state.levels["47"] || 0])
    #       .attr("stroke", "#ffffff")
    #       .attr("stroke-width", 0.7);
    #
    #     // Transparent click helper covering the entire inset box for easy tapping, placed last to be on top!
    #     gOk.append("rect")
    #       .attr("x", OX)
    #       .attr("y", OY)
    #       .attr("width", OW)
    #       .attr("height", OH)
    #       .attr("fill", "rgba(0,0,0,0)")
    #       .attr("pointer-events", "all")
    #       .style("cursor", "pointer");
    #   }

    old_okinawa_block = """    // Transparent click helper covering the entire inset box for easy tapping
    gOk.append("rect")
      .attr("x", OX)
      .attr("y", OY)
      .attr("width", OW)
      .attr("height", OH)
      .attr("fill", "rgba(0,0,0,0)")
      .style("cursor", "pointer");

    const localProjection = d3.geoIdentity()
      .fitExtent([[OX + 6, OY + 6], [OX + OW - 6, OY + OH - 20]], okinawaFeature);

    const localPath = d3.geoPath().projection(localProjection);

    gOk.append("path")
      .attr("class", "cell-path")
      .attr("data-code", "47")
      .attr("d", localPath(okinawaFeature))
      .attr("fill", COLORS[state.levels["47"] || 0])
      .attr("stroke", "#ffffff")
      .attr("stroke-width", 0.7);"""

    new_okinawa_block = """    const localProjection = d3.geoIdentity()
      .fitExtent([[OX + 6, OY + 6], [OX + OW - 6, OY + OH - 20]], okinawaFeature);

    const localPath = d3.geoPath().projection(localProjection);

    gOk.append("path")
      .attr("class", "cell-path")
      .attr("data-code", "47")
      .attr("d", localPath(okinawaFeature))
      .attr("fill", COLORS[state.levels["47"] || 0])
      .attr("stroke", "#ffffff")
      .attr("stroke-width", 0.7);

    // Transparent click helper covering the entire inset box for easy tapping, placed last to be on top!
    gOk.append("rect")
      .attr("x", OX)
      .attr("y", OY)
      .attr("width", OW)
      .attr("height", OH)
      .attr("fill", "rgba(0,0,0,0)")
      .attr("pointer-events", "all")
      .style("cursor", "pointer");"""

    if old_okinawa_block in content:
        content = content.replace(old_okinawa_block, new_okinawa_block)
        print("Success: Okinawa block updated in memory!")
    else:
        # Check standard normalized whitespace matching
        print("Warning: Okinawa block exact string not found. Trying flexible spacing match.")
        # Let's search by lines
        normalized_content = content.replace("\r\n", "\n")
        # We can find sections
        if "gOk.append(\"rect\")" in normalized_content and "d3.geoIdentity()" in normalized_content:
            print("Found identifiers, will attempt replace manually in file.")

    # ─── PART 3: Add click helper rect to French DOM-TOMs ────────
    # We want to change:
    #       gInset.append("path")
    #         .attr("class", "cell-path")
    #         .attr("data-code", dt.code)
    #         .attr("d", localPath(feature))
    #         .attr("fill", COLORS[state.levels[dt.code] || 0])
    #         .attr("stroke", "#ffffff")
    #         .attr("stroke-width", 0.7);
    #
    # TO:
    #       gInset.append("path")
    #         .attr("class", "cell-path")
    #         .attr("data-code", dt.code)
    #         .attr("d", localPath(feature))
    #         .attr("fill", COLORS[state.levels[dt.code] || 0])
    #         .attr("stroke", "#ffffff")
    #         .attr("stroke-width", 0.7);
    #
    #       // Transparent click helper covering the entire inset box for easy tapping, placed last to be on top!
    #       gInset.append("rect")
    #         .attr("x", OX)
    #         .attr("y", OY)
    #         .attr("width", OW)
    #         .attr("height", OH)
    #         .attr("fill", "rgba(0,0,0,0)")
    #         .attr("pointer-events", "all")
    #         .style("cursor", "pointer");

    old_domtom_block = """      gInset.append("path")
        .attr("class", "cell-path")
        .attr("data-code", dt.code)
        .attr("d", localPath(feature))
        .attr("fill", COLORS[state.levels[dt.code] || 0])
        .attr("stroke", "#ffffff")
        .attr("stroke-width", 0.7);"""

    new_domtom_block = """      gInset.append("path")
        .attr("class", "cell-path")
        .attr("data-code", dt.code)
        .attr("d", localPath(feature))
        .attr("fill", COLORS[state.levels[dt.code] || 0])
        .attr("stroke", "#ffffff")
        .attr("stroke-width", 0.7);

      // Transparent click helper covering the entire inset box for easy tapping, placed last to be on top!
      gInset.append("rect")
        .attr("x", OX)
        .attr("y", OY)
        .attr("width", OW)
        .attr("height", OH)
        .attr("fill", "rgba(0,0,0,0)")
        .attr("pointer-events", "all")
        .style("cursor", "pointer");"""

    if old_domtom_block in content:
        content = content.replace(old_domtom_block, new_domtom_block)
        print("Success: France DOM-TOM block updated in memory!")
    else:
        print("Warning: France DOM-TOM block exact string not found.")

    # Write changes back to update_app.py
    with open("update_app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Success: update_app.py successfully written!")

if __name__ == "__main__":
    main()
