def main():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # Update styles.css and app.js version parameters to today's timestamp to bypass browser caching
    content = content.replace("styles.css?v=20260525-100", "styles.css?v=20260526-1150")
    content = content.replace("app.js?v=20260525-100", "app.js?v=20260526-1150")
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Cache buster version updated successfully in index.html!")

if __name__ == "__main__":
    main()
