import os
import re

def update_content(content, filename):
    original_content = content
    
    # 1. Update Links
    content = content.replace('href="production-balance.html"', 'href="analytics-production.html"')
    content = content.replace('href="savings-history.html"', 'href="analytics-savings.html"')
    
    # 2. Update Navigation Text
    # Attendance
    content = content.replace('>出欠情報</a>', '>出欠状況</a>')
    
    # Production Balance
    content = content.replace('>生産活動収支</a>', '>生産活動収支分析</a>')
    
    # Reserves History -> Analysis
    content = content.replace('>積立金履歴</a>', '>積立金分析</a>')
    
    # Average Wages (Ensure consistency, though user said "Average Wages Analysis" -> "Average Wages Analysis")
    # It might be "平均工賃分析" already, but let's check if there's any "平均工賃" standalone link that needs update?
    # The nav usually says "平均工賃分析".
    
    # 3. Update Titles and Headers (H1) for specific files
    if filename == 'attendance.html':
        content = re.sub(r'<title>Compath - 出欠情報</title>', '<title>Compath - 出欠状況</title>', content)
        content = re.sub(r'<h1(.*?)>出欠情報</h1>', r'<h1\1>出欠状況</h1>', content)
        
    if filename == 'analytics-production.html': # Was production-balance.html
        content = re.sub(r'<title>Compath - 生産活動収支</title>', '<title>Compath - 生産活動収支分析</title>', content)
        content = re.sub(r'<h1(.*?)>生産活動収支</h1>', r'<h1\1>生産活動収支分析</h1>', content)
        
    if filename == 'analytics-savings.html': # Was savings-history.html
        content = re.sub(r'<title>Compath - 積立金履歴</title>', '<title>Compath - 積立金分析</title>', content)
        content = re.sub(r'<h1(.*?)>積立金履歴</h1>', r'<h1\1>積立金分析</h1>', content)

    return content

def main():
    directory = '/home/megdisc/dev/p2508e'
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = update_content(content, filename)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
            else:
                print(f"No change needed for {filename}")

if __name__ == "__main__":
    main()
