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
    "billing-user-payment.html"
]

base_dir = "/home/nomadlab/projects/p2508e"

old_link_fragment = 'href="billing-user-deduction.html">利用者控除請求・工賃支払</a>'
new_link_fragment = 'href="billing-user-payment.html">利用者支払・請求</a>'

def process_file(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        print(f"Skipping {filename} (not found)")
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_link_fragment in content:
        new_content = content.replace(old_link_fragment, new_link_fragment)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        # Check if already updated to avoid false positive "not found"
        if new_link_fragment in content:
            print(f"Skipping {filename} (already updated)")
        else:
            print(f"Link not found in {filename}")

for f in target_files:
    process_file(f)
