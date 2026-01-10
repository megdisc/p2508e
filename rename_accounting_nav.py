import glob

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    
    # 1. Rename "請求・支払" to "月次会計"
    if "<summary>請求・支払</summary>" in new_content:
        new_content = new_content.replace("<summary>請求・支払</summary>", "<summary>月次会計</summary>")
        
    # 2. Rename "会計書類" to "年次会計"
    # Target the link text specifically to avoid changing headings or other text if present (though "会計書類" might be the page title too)
    # The user specifically said "The item 'Accounting Documents'". This usually implies the nav menu item.
    # However, replacing it everywhere in the nav context is key. 
    # Let's replace the link text.
    if 'class="nav-link">会計書類</a>' in new_content:
        new_content = new_content.replace('class="nav-link">会計書類</a>', 'class="nav-link">年次会計</a>')
    
    # Also check if it's inside a list item without class (unlikely based on previous file views, but good for safety)
    # The `accounting-documents.html` is the target link.
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {path}")

html_files = glob.glob("*.html")
for html_file in html_files:
    process_file(html_file)
