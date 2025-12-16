import os
import re

TARGET_DIR = '/home/nomadlab/projects/p2508e'

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    filename = os.path.basename(filepath)
    new_lines = []
    
    # Flags to track context if needed, but line-by-line might suffice for simple replacements
    
    for line in lines:
        # 1. REMOVE from Production Activity Section (if present)
        if 'href="production-balance.html"' in line and '生産活動収支状況' in line:
            continue # Remove old link location

        # 2. INSERT into Billing Section (after National Health Billing)
        if 'href="billing-national-health.html"' in line:
            new_lines.append(line)
            active_class = ' class="active"' if filename == 'production-balance.html' else ''
            new_lines.append(f'                        <li><a href="production-balance.html"{active_class}>生産活動収支状況</a></li>\n')
            continue

        # 3. Clean up old actuals links if any remain (just in case)
        if 'href="actuals.html"' in line:
             continue # Just remove it now as we have a new home

        # 4. Remove Claims/Payment Links (Cleanup from previous pass, just in case)
        if 'href="billing-wage-payment.html"' in line:
            continue 
        if 'href="billing-production-activity.html"' in line:
            continue 
            
        new_lines.append(line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Updated {filename}")

def main():
    for filename in os.listdir(TARGET_DIR):
        if filename.endswith('.html'):
            update_file(os.path.join(TARGET_DIR, filename))

if __name__ == '__main__':
    main()
