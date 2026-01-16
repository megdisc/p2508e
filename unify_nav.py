import os
import re

TARGET_DIR = "/home/nomadlab/projects/p2508e"
INDEX_FILE = os.path.join(TARGET_DIR, "index.html")

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

def get_master_nav():
    try:
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to find the sidebar-nav block
        pattern = re.compile(r'(<nav class="sidebar-nav">.*?</nav>)', re.DOTALL)
        match = pattern.search(content)
        if match:
            return match.group(1)
        else:
            print("Error: Could not find sidebar-nav in index.html")
            return None
    except Exception as e:
        print(f"Error reading index.html: {e}")
        return None

def update_file(filepath, master_nav):
    print(f"Processing {filepath}...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    # Regex to find the sidebar-nav block
    pattern = re.compile(r'<nav class="sidebar-nav">.*?</nav>', re.DOTALL)
    
    new_content = content
    if pattern.search(content):
        new_content = pattern.sub(master_nav, content)
    else:
        print(f"Warning: Could not find sidebar-nav in {filepath}")
        
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
    master_nav = get_master_nav()
    if not master_nav:
        return

    for filename in os.listdir(TARGET_DIR):
        if filename.endswith(".html") and filename != "index.html" and not filename.startswith("k_"):
            filepath = os.path.join(TARGET_DIR, filename)
            update_file(filepath, master_nav)

if __name__ == "__main__":
    main()
