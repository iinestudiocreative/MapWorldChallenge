import json
import re

transcript_path = "/Users/willkyandi/.gemini/antigravity/brain/5e626fdf-f35b-47d0-b188-0454ba00e265/.system_generated/logs/transcript.jsonl"

lines_dict = {}

with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            step = json.loads(line)
            # Scan all string fields in the step
            for key, val in step.items():
                if isinstance(val, str):
                    for part in val.split("\n"):
                        match = re.match(r"^(\d+):\s?(.*)$", part)
                        if match:
                            line_num = int(match.group(1))
                            line_content = match.group(2)
                            # Ensure we don't accidentally get other files' lines if any
                            # We know update_app.py starts with imports and app_js_content
                            if line_num == 1 and "import os" not in line_content:
                                continue
                            if line_num not in lines_dict or len(line_content) > len(lines_dict[line_num]):
                                lines_dict[line_num] = line_content
        except Exception as e:
            pass

print(f"Total distinct lines recovered: {len(lines_dict)}")
max_line = max(lines_dict.keys()) if lines_dict else 0
print(f"Max line number: {max_line}")

# Check for missing lines
missing = []
for i in range(1, max_line + 1):
    if i not in lines_dict:
        missing.append(i)

if missing:
    print(f"Missing lines count: {len(missing)}")
    print(f"First few missing lines: {missing[:20]}")
    # Let's write whatever we recovered to see
    with open("update_app_partial.py", "w", encoding="utf-8") as f:
        for i in range(1, max_line + 1):
            if i in lines_dict:
                f.write(f"{i}: {lines_dict[i]}\n")
            else:
                f.write(f"{i}: MISSING\n")
else:
    print("No missing lines! Reconstructing update_app.py...")
    with open("update_app_restored.py", "w", encoding="utf-8") as f:
        for i in range(1, max_line + 1):
            f.write(lines_dict[i] + "\n")
    print("Reconstructed update_app_restored.py successfully!")



