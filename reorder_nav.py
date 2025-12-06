import os
import re

def restructure_nav(content):
    # 1. Remove the "Reserves Information" accordion
    # Pattern: <details class="nav-accordion"[^>]*>\s*<summary>積立金情報</summary>.*?</ul>\s*</details>
    reserves_accordion_pattern = r'(<details class="nav-accordion"[^>]*>\s*<summary>積立金情報</summary>.*?</ul>\s*</details>)'
    
    # Check if the block exists
    match = re.search(reserves_accordion_pattern, content, re.DOTALL)
    if not match:
        # If not found, maybe it's already removed or format is different.
        # But we still need to add the links if they are missing (though this script assumes a one-time migration).
        # Let's proceed assuming we might need to insert things even if removal fails (or if already removed).
        pass
    else:
        # Remove it
        content = content.replace(match.group(1), '')

    # 2. Insert "Reserves Settings" link after "Wages/Deductions Information" accordion
    # Find the end of Wages/Deductions accordion
    # It usually ends with </details> followed by a newline and maybe spaces.
    # We look for the specific accordion content to be sure.
    wages_accordion_end_pattern = r'(<summary>工賃・控除情報</summary>.*?</ul>\s*</details>)'
    
    def insert_settings_link(match):
        block = match.group(1)
        # Check if link already exists to avoid duplication
        if 'href="savings-settings.html"' in content:
            return block
        
        # Determine active class
        active_class = ' class="nav-link active"' if 'savings-settings.html" class="nav-link active"' in content or 'savings-settings.html" class="active"' in content else ' class="nav-link"'
        # Actually, since we are processing the file content, we can check if this file IS savings-settings.html by context, 
        # but the simple way is to check if the original link had 'active'.
        # However, we just removed the original link. So we should have captured that state.
        
        # Let's refine: We should capture the active state BEFORE removing the original block.
        return block + '\n\n                <a href="savings-settings.html" class="nav-link">積立金設定</a>'

    # We need to handle the active state correctly.
    # Let's restart the logic slightly.
    
    is_settings_active = 'href="savings-settings.html" class="nav-link active"' in content or 'href="savings-settings.html" class="active"' in content
    is_history_active = 'href="savings-history.html" class="nav-link active"' in content or 'href="savings-history.html" class="active"' in content # Though history is usually in li > a
    
    # Remove the old block
    content = re.sub(reserves_accordion_pattern, '', content, flags=re.DOTALL)
    
    # Insert Settings Link
    settings_link = '<a href="savings-settings.html" class="nav-link' + (' active' if is_settings_active else '') + '">積立金設定</a>'
    
    # Regex to find the Wages accordion and append the link
    # We use a lookbehind or just match the whole block and append
    content = re.sub(
        r'(<details class="nav-accordion"[^>]*>\s*<summary>工賃・控除情報</summary>.*?</ul>\s*</details>)', 
        lambda m: m.group(1) + '\n\n                ' + settings_link, 
        content, 
        flags=re.DOTALL
    )

    # 3. Insert "Reserves History" into "Analytics" accordion
    # Find the list inside Analytics accordion
    analytics_list_pattern = r'(<summary>分析</summary>\s*<ul>)(.*?)(</ul>)'
    
    def insert_history_link(match):
        header = match.group(1)
        body = match.group(2)
        footer = match.group(3)
        
        if 'savings-history.html' in body:
            return match.group(0)
            
        # Append to the end of the list
        history_item = '<li><a href="savings-history.html">積立金履歴</a></li>'
        # If active, we might need to add class to a? usually li>a doesn't have class in this design, or does it?
        # Checking other files: <li><a href="production-balance.html">生産活動収支</a></li>
        # So no class on a tag usually for these lists, unless active?
        # Let's check sidebar-nav ul a styles.
        # If we need to mark it active:
        if is_history_active:
             history_item = '<li><a href="savings-history.html" class="active">積立金履歴</a></li>' # Assuming class active works here or we need to check css
        
        # Add indentation
        new_item = '\n                        ' + history_item
        return f"{header}{body}{new_item}{footer}"

    content = re.sub(analytics_list_pattern, insert_history_link, content, flags=re.DOTALL)
    
    # Clean up extra newlines if any
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

    return content

def main():
    directory = '/home/megdisc/dev/p2508e'
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = restructure_nav(content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
            else:
                print(f"No change needed for {filename}")

if __name__ == "__main__":
    main()
