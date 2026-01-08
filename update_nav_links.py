import os
import re

TARGET_DIR = '/home/megdisc/dev/p2508e'

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    filename = os.path.basename(filepath)
    new_lines = []
    
    # Flags
    skip_next = False
    
    for line in lines:
        if skip_next:
            skip_next = False
            continue

        # 1. Look for 'account.html' link
        if 'href="account.html"' in line:
            new_lines.append(line)
            
            # Insert Accounting Documents Link
            active_class = ' class="active"' if filename == 'accounting-documents.html' else ''
            new_lines.append(f'                <a href="accounting-documents.html" class="nav-link"{active_class}>会計書類</a>\n')
            
            # Check if 'styleguide.html' or 'accounting-documents.html' was already next (to avoid dupes)
            # We assume the file structure is relatively clean or we are overwriting
            # But let's be safe: If the *next* line is already accounting or styleguide, we might want to skip it?
            # Actually, let's just proceed. The user said "Insert between User Account and Style Guide".
            # The simplest way is to output Account -> Accounting.
            # Then if we meet Styleguide later, we output it.
            # But if we meet Accounting later (from a previous run), we should SKIP it.
            continue

        # 2. Skip existing 'accounting-documents.html' link if found (to prevent duplication)
        if 'href="accounting-documents.html"' in line:
            continue

        # 3. Handle Styleguide (it should come after accounting, which we inserted above)
        # Just ensure it's there? No, we just need to preserve it if it exists, or insert it if missing?
        # The previous script logic was simpler. Let's just output it as is.
        
        # 4. Handle other cleanups from original script if needed
        # (Assuming original script cleanups are done or not needed anymore)
        
        new_lines.append(line)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Updated {filename}")

def main():
    if not os.path.exists(TARGET_DIR):
        print(f"Directory not found: {TARGET_DIR}")
        return

    for filename in os.listdir(TARGET_DIR):
        if filename.endswith('.html'):
            update_file(os.path.join(TARGET_DIR, filename))

if __name__ == '__main__':
    main()
