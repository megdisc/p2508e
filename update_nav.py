import os

directory = '/home/megdisc/dev/p2508e'

replacements = [
    ('accounting-monthly.html', 'billing-national-health.html'),
    ('accounting-annual.html', 'billing-wage-payment.html'),
    ('<summary>会計</summary>', '<summary>請求・支払</summary>'),
    ('>月次会計<', '>国保連請求<'),
    ('>年次会計<', '>工賃支払・控除請求<'),
    ('月次会計', '国保連請求'), # Replace in titles/headers as well
    ('年次会計', '工賃支払・控除請求') # Replace in titles/headers as well
]

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        for old, new in replacements:
            new_content = new_content.replace(old, new)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
