import re

def main():
    # ─── PART 1: Update update_app.py ───────────────────────────
    with open("update_app.py", "r", encoding="utf-8") as f:
        content_app = f.read()

    # Find the Flag block in updateUITranslations() and simplify it to always use the Earth emoji
    # The block looks like:
    #   // Flag
    #   const cardFlag = document.getElementById("card-flag");
    #   if (cardFlag) {
    #     if (state.currentMap === "jp") {
    #       cardFlag.innerHTML = '<svg ...></svg>';
    #     } else if (state.currentMap === "fr") {
    #       cardFlag.innerHTML = '<svg ...></svg>';
    #     } else {
    #       cardFlag.textContent = "🌍";
    #     }
    #   }
    
    old_flag_block_pattern = r"  // Flag\s+const cardFlag = document\.getElementById\(\"card-flag\"\);\s+if \(cardFlag\) \{\s+if \(state\.currentMap === \"jp\"\) \{\s+cardFlag\.innerHTML = '<svg[^>]+>.*?</svg>';\s+\} else if \(state\.currentMap === \"fr\"\) \{\s+cardFlag\.innerHTML = '<svg[^>]+>.*?</svg>';\s+\} else \{\s+cardFlag\.textContent = \"🌍\";\s+\}\s+\}"
    
    new_flag_block = """  // Flag
  const cardFlag = document.getElementById("card-flag");
  if (cardFlag) {
    cardFlag.textContent = "🌍";
  }"""

    # Let's perform a direct search-replace by locating the exact lines since regex on massive svg string can be tricky
    start_flag_marker = '  // Flag\n  const cardFlag = document.getElementById("card-flag");\n  if (cardFlag) {'
    idx = content_app.find(start_flag_marker)
    if idx != -1:
        # Find the closing brace of the "if (cardFlag) {" block
        # We know the block ends with "    }\n  }" or similar.
        # Let's search for "  // Export button" or "cardFlag.textContent = \"🌍\";\n    }\n  }"
        end_marker = '  // Export button'
        end_idx = content_app.find(end_marker, idx)
        if end_idx != -1:
            # We replace everything from idx to end_idx with our new simplified block + "\n\n  "
            old_block = content_app[idx:end_idx]
            content_app = content_app.replace(old_block, new_flag_block + "\n\n")
            print("Success: update_app.py Flag block simplified in memory!")
        else:
            print("Error: Could not find end marker in update_app.py")
    else:
        print("Error: Could not find flag block in update_app.py")

    with open("update_app.py", "w", encoding="utf-8") as f:
        f.write(content_app)

    # ─── PART 2: Update styles.css ──────────────────────────────
    with open("styles.css", "r", encoding="utf-8") as f:
        content_css = f.read()

    # Change `#tutorial-overlay.hidden` to `display: none !important;`
    old_hidden_tuto = """#tutorial-overlay.hidden {
  opacity: 0;
  pointer-events: none;
}"""

    new_hidden_tuto = """#tutorial-overlay.hidden {
  display: none !important;
}"""

    if old_hidden_tuto in content_css:
        content_css = content_css.replace(old_hidden_tuto, new_hidden_tuto)
        print("Success: styles.css tutorial-overlay.hidden updated!")
    else:
        # Try finding with any whitespace
        content_css = re.sub(
            r"#tutorial-overlay\.hidden\s*\{\s*opacity:\s*0;\s*pointer-events:\s*none;\s*\}",
            new_hidden_tuto,
            content_css
        )
        print("Success: styles.css tutorial-overlay.hidden updated via regex!")

    with open("styles.css", "w", encoding="utf-8") as f:
        f.write(content_css)

    # ─── PART 3: Update index.html ──────────────────────────────
    with open("index.html", "r", encoding="utf-8") as f:
        content_html = f.read()

    # Change `<span id="card-flag">🗾</span>` to `<span id="card-flag">🌍</span>`
    old_flag_html = '<span id="card-flag">🗾</span>'
    new_flag_html = '<span id="card-flag">🌍</span>'
    if old_flag_html in content_html:
        content_html = content_html.replace(old_flag_html, new_flag_html)
        print("Success: index.html card-flag emoji updated!")
    else:
        print("Warning: index.html card-flag emoji match not found.")

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content_html)

if __name__ == "__main__":
    main()
