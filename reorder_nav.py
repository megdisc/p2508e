import os
import re

def reorder_nav_items(content):
    # Find the Production Activity accordion
    # We look for <summary>生産活動</summary> followed by <ul> containing the items
    pattern = r'(<summary>生産活動</summary>\s*<ul>)(.*?)(</ul>)'
    
    def replace_callback(match):
        header = match.group(1)
        body = match.group(2)
        footer = match.group(3)
        
        # Extract list items
        # We assume each li is on its own line or clearly separated
        # Let's split by </li> and reconstruct, or just find all <li>...</li>
        
        # Regex to find full <li>...</li> blocks, including newlines
        li_pattern = r'(<li><a href="[^"]+".*?</a></li>)'
        items = re.findall(li_pattern, body, re.DOTALL)
        
        if not items:
            return match.group(0)
            
        # Map items by their href key
        item_map = {}
        for item in items:
            if 'projects.html' in item:
                item_map['projects'] = item
            elif 'actuals.html' in item:
                item_map['actuals'] = item
            elif 'schedule.html' in item:
                item_map['schedule'] = item
            else:
                # Keep other items if any (though unlikely based on request)
                pass
        
        # Define new order: projects, schedule, actuals
        new_order = []
        if 'projects' in item_map: new_order.append(item_map['projects'])
        if 'schedule' in item_map: new_order.append(item_map['schedule'])
        if 'actuals' in item_map: new_order.append(item_map['actuals'])
        
        # Reconstruct the body with proper indentation
        # We'll assume standard indentation of 24 spaces based on previous file views, 
        # or just use the indentation found in the original string if possible.
        # For simplicity, we'll join with the whitespace that was likely there.
        
        # A simple join with newlines and indentation
        indent = "\n                        "
        new_body = indent + indent.join(new_order) + "\n                    "
        
        return f"{header}{new_body}{footer}"

    return re.sub(pattern, replace_callback, content, flags=re.DOTALL)

def main():
    directory = '/home/megdisc/dev/p2508e'
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = reorder_nav_items(content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
            else:
                print(f"No change needed for {filename}")

if __name__ == "__main__":
    main()
