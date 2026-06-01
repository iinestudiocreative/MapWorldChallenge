def check_css(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    stack = []
    lines = content.split("\n")
    
    for r_num, line in enumerate(lines, 1):
        # Strip comments
        # CSS comments are /* ... */
        # (This is a simplified check, assuming no complex multiline comment parsing needed, 
        # but let's do a basic parser)
        pass

    # Better simple character parser
    i = 0
    in_comment = False
    in_string = False
    string_char = ""
    
    while i < len(content):
        ch = content[i]
        
        if in_comment:
            if ch == '*' and i + 1 < len(content) and content[i+1] == '/':
                in_comment = False
                i += 2
                continue
            i += 1
            continue
            
        if not in_comment:
            if ch == '/' and i + 1 < len(content) and content[i+1] == '*':
                in_comment = True
                i += 2
                continue
                
        if in_string:
            if ch == string_char:
                in_string = False
            i += 1
            continue
            
        if ch in ('"', "'"):
            in_string = True
            string_char = ch
            i += 1
            continue
            
        if ch == '{':
            # find line number
            line_num = content[:i].count("\n") + 1
            stack.append(('{', line_num))
        elif ch == '}':
            line_num = content[:i].count("\n") + 1
            if not stack:
                print(f"Extra closing brace '}}' at line {line_num}")
                return False
            stack.pop()
        i += 1
        
    if stack:
        print(f"Unclosed braces found! Total: {len(stack)}")
        for ch, line in stack:
            print(f"  Unclosed '{ch}' opened at line {line}")
        return False
        
    print("CSS braces are perfectly balanced!")
    return True

if __name__ == "__main__":
    check_css("styles.css")
