import os
import re

# Master Nav Content from index.html
MASTER_NAV = """            <nav class="sidebar-nav">
                <a href="index.html" class="nav-link">トップ</a>
                <details class="nav-accordion">
                    <summary>施設情報</summary>
                    <ul>
                        <li><a href="corporation.html">法人情報</a></li>
                        <li><a href="office.html">事業所情報</a></li>
                    </ul>
                </details>
                <details class="nav-accordion">
                    <summary>職員・利用者情報</summary>
                    <ul>
                        <li><a href="staff.html">職員情報</a></li>
                        <li><a href="members.html">利用者情報</a></li>
                    </ul>
                </details>

                <a href="partners.html" class="nav-link">取引先情報</a>
                <details class="nav-accordion">
                    <summary>スキル情報</summary>
                    <ul>
                        <li><a href="skills-settings.html">スキル設定</a></li>
                        <li><a href="skills-evaluation.html">スキル評価</a></li>
                    </ul>
                </details>
                <details class="nav-accordion">
                    <summary>工賃・控除情報</summary>
                    <ul>
                        <li><a href="wages-settings.html">工賃設定</a></li>
                        <li><a href="deductions-settings.html">控除設定</a></li>
                        <li><a href="wages-evaluation.html">工賃レベル評価</a></li>
                    </ul>
                </details>

                <a href="savings-settings.html" class="nav-link">積立金設定</a>

                <a href="attendance.html" class="nav-link">出欠状況</a>
                <details class="nav-accordion">
                    <summary>福祉事業活動</summary>
                    <ul>
                        <li><a href="support-plans.html">個別支援計画</a></li>
                    </ul>
                </details>
                <details class="nav-accordion">
                    <summary>生産活動</summary>
                    <ul>
                        <li><a href="projects.html">案件情報</a></li>
                        <li><a href="schedule.html">進捗状況</a></li>
                        <li><a href="expenses-record.html">費用記録</a></li>
                    </ul>
                </details>
                <details class="nav-accordion">
                    <summary>月次会計</summary>
                    <ul>
                        <li><a href="billing-national-health.html">国保連請求</a></li>
                        <li><a href="billing-customer.html">顧客請求</a></li>
                        <li><a href="payment-subcontractor.html">外注先支払</a></li>
                        <li><a href="billing-user-payment.html">利用者支払・請求</a></li>
                    </ul>
                </details>
                <a href="accounting-documents.html" class="nav-link">年次会計</a>
                <details class="nav-accordion">
                    <summary>分析</summary>
                    <ul>
                        <li><a href="analytics-production.html">生産活動収支分析</a></li>
                        <li><a href="analytics-wages.html">平均工賃分析</a></li>

                        <li><a href="analytics-savings.html">積立金分析</a></li>
                    </ul>
                </details>
                <a href="account.html" class="nav-link">ユーザーアカウント</a>
                <a href="styleguide.html" class="nav-link">スタイルガイド</a>
            </nav>"""

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

TARGET_DIR = "/home/nomadlab/projects/p2508e"

def update_file(filepath):
    print(f"Processing {filepath}...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    # Regex to find the sidebar-nav block
    # capture everything from <nav class="sidebar-nav"> to </nav>
    # Use dotall to match newlines
    pattern = re.compile(r'<nav class="sidebar-nav">.*?</nav>', re.DOTALL)
    
    new_content = content
    if pattern.search(content):
        new_content = pattern.sub(MASTER_NAV, content)
    else:
        print(f"Warning: Could not find sidebar-nav in {filepath}")
        
    # Special handling for savings-settings.html to add JS
    if "savings-settings.html" in filepath:
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
    for filename in os.listdir(TARGET_DIR):
        if filename.endswith(".html") and filename != "index.html" and not filename.startswith("k_"):
            filepath = os.path.join(TARGET_DIR, filename)
            update_file(filepath)

if __name__ == "__main__":
    main()
