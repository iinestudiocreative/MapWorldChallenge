def main():
    # ─── PART 1: Update update_app.py ───────────────────────────
    with open("update_app.py", "r", encoding="utf-8") as f:
        content_app = f.read()

    # 1. Update English tutorial title
    content_app = content_app.replace(
        'title: "Welcome to Ride the world! 🌍",',
        'title: "Welcome ! 🌍",'
    )
    
    # 2. Update Japanese tutorial title
    content_app = content_app.replace(
        'title: "Ride the world へようこそ！ 🌍",',
        'title: "ようこそ！ 🌍",'
    )
    
    # 3. Update French tutorial title
    content_app = content_app.replace(
        'title: "Bienvenue sur Ride the world ! 🌍",',
        'title: "Bienvenue ! 🌍",'
    )

    with open("update_app.py", "w", encoding="utf-8") as f:
        f.write(content_app)
    print("Success: update_app.py tutorial titles shortened!")

    # ─── PART 2: Update styles.css ──────────────────────────────
    with open("styles.css", "a", encoding="utf-8") as f:
        # Append smaller font-size style for #tuto-title
        f.write("\n#tuto-title {\n  font-size: 1.15rem;\n  white-space: nowrap;\n}\n")
    print("Success: styles.css safety font-size override appended!")

    # ─── PART 3: Update index.html Cache Buster ─────────────────
    with open("index.html", "r", encoding="utf-8") as f:
        content_html = f.read()

    content_html = content_html.replace("20260526-1152", "20260526-1154")
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content_html)
    print("Success: index.html cache buster incremented to 1154!")

if __name__ == "__main__":
    main()
