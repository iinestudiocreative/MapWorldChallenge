def check_brackets(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    stack = []
    lines = content.split("\n")
    
    # Simple brace/bracket/parentheses match check
    mapping = {')': '(', '}': '{', ']': '['}
    for r_num, line in enumerate(lines, 1):
        # Strip comments
        line_clean = ""
        in_string = False
        string_char = ""
        escaped = False
        
        i = 0
        while i < len(line):
            ch = line[i]
            if escaped:
                escaped = False
                i += 1
                continue
            if ch == '\\':
                escaped = True
                i += 1
                continue
            if in_string:
                if ch == string_char:
                    in_string = False
            else:
                if ch in ('"', "'", '`'):
                    in_string = True
                    string_char = ch
                elif ch == '/' and i + 1 < len(line) and line[i+1] == '/':
                    break  # Comment rest of the line
                elif ch in ('(', '{', '['):
                    stack.append((ch, r_num, i))
                elif ch in (')', '}', ']'):
                    if not stack:
                        print(f"Extra closing {ch} at line {r_num}, char {i}")
                        return False
                    last_ch, last_line, last_char = stack.pop()
                    if mapping[ch] != last_ch:
                        print(f"Mismatch: opened {last_ch} at line {last_line} but closed with {ch} at line {r_num}")
                        return False
            i += 1
            
    if stack:
        print(f"Unclosed structures: {len(stack)}")
        for ch, line, char in stack[-5:]:
            print(f"  Unclosed {ch} opened at line {line}")
        return False
        
    print("Brackets are perfectly balanced!")
    return True

if __name__ == "__main__":
    check_brackets("app.js")
