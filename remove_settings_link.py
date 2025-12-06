import os
import re

def remove_settings_link(content):
    # Pattern to match the settings link, handling potential whitespace
    # <a href="settings.html" class="nav-link">（その他設定）</a>
    pattern = r'\s*<a href="settings\.html" class="nav-link">（その他設定）</a>'
    
    if re.search(pattern, content):
        return re.sub(pattern, '', content)
    return content

def main():
    directory = '/home/megdisc/dev/p2508e'
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = remove_settings_link(content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
            else:
                print(f"No change needed for {filename}")

if __name__ == "__main__":
    main()
