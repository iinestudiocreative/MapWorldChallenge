def check_braces(filename):
    with open(filename, "r", encoding="utf-8") as f:
        code = f.read()
    
    # Strip comments to prevent false positives
    # Remove single line comments
    code = re.sub(r"//.*", "", code)
    # Remove multi-line comments
    code = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)
    
    # Track brackets
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    lines = code.split("\n")
    for line_num, line in enumerate(lines, 1):
        # We need to ignore characters inside strings
        in_string = False
        string_char = None
        escaped = False
        
        for char_idx, char in enumerate(line):
            if escaped:
                escaped = False
                continue
            if char == '\\':
                escaped = True
                continue
            
            if char in ["'", '"', '`']:
                if not in_string:
                    in_string = True
                    string_char = char
                elif string_char == char:
                    in_string = False
                    string_char = None
                continue
            
            if in_string:
                continue
            
            if char in brackets.values():
                stack.append((char, line_num, char_idx, line))
            elif char in brackets.keys():
                if not stack:
                    print(f"Unmatched closing bracket '{char}' at line {line_num}:{char_idx}")
                    print("Line content:", line)
                    return False
                top_char, top_line, top_idx, top_line_content = stack.pop()
                if top_char != brackets[char]:
                    print(f"Mismatch: '{char}' at line {line_num}:{char_idx} does not match '{top_char}' from line {top_line}:{top_idx}")
                    print("Opening line:", top_line_content)
                    print("Closing line:", line)
                    return False
                    
    if stack:
        print(f"Unmatched opening brackets remaining: {len(stack)}")
        for char, line_num, char_idx, line in stack[:5]:
            print(f"  '{char}' at line {line_num}:{char_idx}")
            print("  Line:", line)
        return False
        
    print("All brackets match perfectly!")
    return True

import re
check_braces("app.js")
