import os

target_files = [
    "account.html",
    "accounting-documents.html",
    "analytics-production.html",
    "analytics-savings.html",
    "analytics-wages.html",
    "attendance copy.html",
    "attendance.html",
    "billing-national-health.html",
    "corporation.html",
    "deductions-settings.html",
    "expenses-record copy.html",
    "expenses-record.html",
    "index.html",
    "members.html",
    "office.html",
    "partners.html",
    "projects.html",
    "savings-settings.html",
    "schedule.html",
    "skills-evaluation.html",
    "skills-settings.html",
    "staff.html",
    "styleguide.html",
    "support-plans.html",
    "wages-evaluation.html",
    "wages-settings.html",
    "billing-customer.html",
    "payment-subcontractor.html",
    "billing-user-deduction.html"
]

base_dir = "/home/nomadlab/projects/p2508e"

new_links = """                        <li><a href="billing-customer.html">顧客請求</a></li>
                        <li><a href="payment-subcontractor.html">外注先支払</a></li>
                        <li><a href="billing-user-deduction.html">利用者控除請求・工賃支払</a></li>
"""

anchor_line = '<li><a href="billing-national-health.html">国保連請求</a></li>'

def process_file(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        print(f"Skipping {filename} (not found)")
        return

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # check if already added
    if any('href="billing-customer.html"' in line for line in lines):
        print(f"Skipping {filename} (links already exist)")
        return

    new_lines = []
    found = False
    
    for line in lines:
        new_lines.append(line)
        if anchor_line in line:
            new_lines.append(new_lines[-1].replace(line.strip(), "").replace("\n", "") + new_links) 
            # Logic: simplistic append. 
            # Better: Insert contents of new_links.
            # But the indentation is tricky.
            # Let's simple insert.
            found = True
            
    # Retry with safer logic to preserve indentation
    if not found:
        print(f"Anchor not found in {filename}")
        return

    final_lines = []
    for line in lines:
        final_lines.append(line)
        if anchor_line in line:
            # Detect indentation
            indent = line[:line.find('<')]
            final_lines.append(f'{indent}<li><a href="billing-customer.html">顧客請求</a></li>\n')
            final_lines.append(f'{indent}<li><a href="payment-subcontractor.html">外注先支払</a></li>\n')
            final_lines.append(f'{indent}<li><a href="billing-user-deduction.html">利用者控除請求・工賃支払</a></li>\n')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)
    print(f"Updated {filename}")

for f in target_files:
    process_file(f)
