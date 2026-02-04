import os
import re

TARGET_DIR = "/home/nomadlab/projects/p2508e"
INDEX_FILE = os.path.join(TARGET_DIR, "top.html")

# JS for Active State
ACTIVE_STATE_JS = """        // サイドバーの現在地連動（アコーディオン自動展開）
        document.addEventListener("DOMContentLoaded", () => {
            const currentFile = window.location.pathname.split("/").pop();
            document.querySelectorAll(".sidebar-nav a").forEach(link => {
                if (link.getAttribute("href") === currentFile) {
                    link.classList.add("active");
                    const details = link.closest("details");
                    if (details) details.open = true;
                }
            });
        });"""

def get_master_content():
    try:
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to find the sidebar-nav block
        nav_pattern = re.compile(r'(<nav class="sidebar-nav">.*?</nav>)', re.DOTALL)
        nav_match = nav_pattern.search(content)
        
        # Regex to find the sidebar-footer block
        footer_pattern = re.compile(r'(<div class="sidebar-footer">.*?</div>\s*</aside>)', re.DOTALL) 
        # Note: sidebar-footer is usually the last child of aside, so simplistic regex might catch valid /aside
        # Let's try explicit div matching or just sidebar-footer div.
        footer_pattern_simple = re.compile(r'(<div class="sidebar-footer">.*?</div>)', re.DOTALL)
        footer_match = footer_pattern_simple.search(content)

        if nav_match and footer_match:
            return nav_match.group(1), footer_match.group(1)
        else:
            print("Error: Could not find sidebar-nav or sidebar-footer in top.html")
            return None, None
    except Exception as e:
        print(f"Error reading top.html: {e}")
        return None, None

def update_file(filepath, master_nav, master_footer):
    print(f"Processing {filepath}...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    # Regex to find the blocks
    nav_pattern = re.compile(r'<nav class="sidebar-nav">.*?</nav>', re.DOTALL)
    footer_pattern = re.compile(r'<div class="sidebar-footer">.*?</div>', re.DOTALL)
    
    new_content = content
    
    if nav_pattern.search(content):
        new_content = nav_pattern.sub(master_nav, new_content)
    else:
        print(f"Warning: Could not find sidebar-nav in {filepath}")
        
    if footer_pattern.search(content):
        new_content = footer_pattern.sub(master_footer, new_content)
    else:
        print(f"Warning: Could not find sidebar-footer in {filepath}")
        
    # Special handling for savings-settings.html and expenses-record.html to add JS
    if any(x in filepath for x in ["savings-settings.html", "expenses-record.html"]):
        if "サイドバーの現在地連動" not in new_content:
            # Insert JS before </head>
            js_injection = f"""    <script>
{ACTIVE_STATE_JS}
    </script>
"""
            new_content = new_content.replace('</head>', f'{js_injection}</head>')
            print(f"  -> Injected JS")

    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  -> Updated")
    else:
        print(f"  -> No changes needed")

def main():
    master_nav, master_footer = get_master_content()
    if not master_nav:
        return

    for filename in os.listdir(TARGET_DIR):
        if filename.endswith(".html") and filename != "top.html" and filename != "index.html" and not filename.startswith("k_"):
            filepath = os.path.join(TARGET_DIR, filename)
            update_file(filepath, master_nav, master_footer)

if __name__ == "__main__":
    main()
