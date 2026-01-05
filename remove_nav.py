import glob
import os

print("Starting nav removal...")
count = 0

# Target HTML snippet to remove
# We will look for line containing 'href="production-balance.html"'
TARGET_SUBSTRING = 'href="production-balance.html"'

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    modified = False
    
    for line in lines:
        if TARGET_SUBSTRING in line:
            # Skip this line (remove it)
            modified = True
            continue
        new_lines.append(line)
        
    if modified:
        with open(filepath, 'w') as f:
            f.writelines(new_lines)
        print(f"cleaned: {filepath}")
        count += 1

print(f"Completed. Cleaned {count} files.")
