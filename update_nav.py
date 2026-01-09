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
    "wages-settings.html"
]

base_dir = "/home/nomadlab/projects/p2508e"
link_line_content = '<a href="accounting-documents.html" class="nav-link">会計書類</a>'

def process_file(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        print(f"Skipping {filename} (not found)")
        return

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 1. Find and remove the line
    removed_line = None
    new_lines = []
    
    # We need to be careful not to remove it if we already established order (idempotency), 
    # but for now let's just find and pop it.
    
    link_found = False
    for line in lines:
        if link_line_content in line:
            removed_line = line
            link_found = True
            continue # Skip adding this line
        new_lines.append(line)
        
    if not link_found:
        print(f"Link not found in {filename}, skipping move.")
        return

    # 2. Find insertion point
    # We want to insert AFTER the </details> that closes the "請求・支払" accordion.
    # Logic: Find <summary>請求・支払</summary>, then find the first </details> after it.
    
    insertion_index = -1
    billing_summary_found = False
    
    for i, line in enumerate(new_lines):
        if "<summary>請求・支払</summary>" in line:
            billing_summary_found = True
        
        if billing_summary_found:
            if "</details>" in line:
                insertion_index = i + 1 # Insert after this line
                break
    
    if insertion_index != -1:
        # Check if we are inserting right before Analytics (optional check but good for verification)
        # But simply inserting after the Billing details is sufficient per requirement.
        
        # Ensure correct indentation (same as the removed line or standardized)
        # We use the removed_line's content which includes indentation/newline
        new_lines.insert(insertion_index, removed_line)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Updated {filename}")
    else:
        print(f"Could not find insertion point in {filename}")

for f in target_files:
    process_file(f)
