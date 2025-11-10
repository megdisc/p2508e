/**
 * layout.js (静的HTML・モックアップ用)
 * constants.js の値を参照し、ページの共通レイアウト（ロゴ、H1、ナビ）を動的に構築します。
 */

// document.addEventListener("DOMContentLoaded", () => { // ← この行を削除

    // 0. 定義ファイルが読み込まれているか確認
    if (typeof window.APP_CONSTANTS === 'undefined') {
        console.error("constants.js が読み込まれていません。");
        // return; // ← return も削除 (または適切なエラー処理)
    } else {
        const CONST = window.APP_CONSTANTS;

        // 1. 現在のページキーを <body> の data-page-key 属性から取得
        const currentPageKey = document.body.dataset.pageKey;
        if (!currentPageKey) {
            console.warn("<body> に data-page-key が設定されていません。");
        }

        // 2. ロゴ（アプリ名）を定数から設定
        const logoElement = document.querySelector(".logo");
        if (logoElement) {
            logoElement.textContent = CONST.APP_NAME;
        }

        // 3. H1（ページタイトル）を定数から設定
        const titleElement = document.querySelector("h1");
        if (titleElement) {
            // PAGE_TITLES から現在のページキーに一致するタイトルを取得
            const title = CONST.PAGE_TITLES[currentPageKey] || "（タイトル未設定）";
            titleElement.textContent = title;
        }
        
        // 4. フッターのユーザー情報を定数（ダミーデータ）から設定
        const userNameElement = document.querySelector(".user-name");
        const userRoleElement = document.querySelector(".user-role");
        if (userNameElement) {
            userNameElement.textContent = CONST.DUMMY_USER.name;
        }
        if (userRoleElement) {
            userRoleElement.textContent = CONST.DUMMY_USER.role;
        }

        // 5. ナビゲーションの動的生成
        // (中略 ... layout.js の既存のロジックはそのまま)
        
        // ページキーとナビゲーションの href のマッピング
        const navLinks = {
            [CONST.PAGE_KEYS.TOP]: 'index.html',
            [CONST.PAGE_KEYS.CORPORATION]: 'corporation.html',
            [CONST.PAGE_KEYS.OFFICES]: 'offices.html',
            [CONST.PAGE_KEYS.STAFF]: 'staff.html',
            [CONST.PAGE_KEYS.PLACEMENT]: 'placement.html',
            [CONST.PAGE_KEYS.PARTNERS]: 'partners.html',
            [CONST.PAGE_KEYS.MEMBERS]: 'members.html',
            [CONST.PAGE_KEYS.ATTENDANCE]: 'attendance.html',
            [CONST.PAGE_KEYS.PROJECTS]: 'projects.html',
            [CONST.PAGE_KEYS.PROGRESS]: 'progress.html',
        };
        
        // アコーディオンのキー
        const facilityInfoKeys = [
            CONST.PAGE_KEYS.CORPORATION, 
            CONST.PAGE_KEYS.OFFICES, 
            CONST.PAGE_KEYS.STAFF, 
            CONST.PAGE_KEYS.PLACEMENT
        ];
        const projectManagementKeys = [
            CONST.PAGE_KEYS.PROJECTS,
            CONST.PAGE_KEYS.PROGRESS
        ];

        // アコーディオンを開くかどうかの判定
        const shouldOpenFacility = facilityInfoKeys.includes(currentPageKey);
        const shouldOpenProject = projectManagementKeys.includes(currentPageKey);

        // ナビゲーションのHTMLを定数から生成
        const navHtml = `
            <ul>
                <li class="nav-item">
                    <a href="index.html" class="${currentPageKey === CONST.PAGE_KEYS.TOP ? 'active' : ''}">
                        ${CONST.PAGE_TITLES.TOP}
                    </a>
                </li>
                
                <li class="nav-category">${CONST.NAV_ITEMS.CAT_BASIC_INFO}</li>
                
                <li class="nav-accordion">
                    <details ${shouldOpenFacility ? 'open' : ''}>
                        <summary>${CONST.NAV_ITEMS.ACC_FACILITY_INFO}</summary>
                        <ul class="nav-accordion-menu">
                            <li>
                                <a href="corporation.html" class="${currentPageKey === CONST.PAGE_KEYS.CORPORATION ? 'active' : ''}">
                                    ${CONST.PAGE_TITLES.CORPORATION}
                                </a>
                            </li>
                            <li>
                                <a href="offices.html" class="${currentPageKey === CONST.PAGE_KEYS.OFFICES ? 'active' : ''}">
                                    ${CONST.PAGE_TITLES.OFFICES}
                                </a>
                            </li>
                            <li>
                                <a href="staff.html" class="${currentPageKey === CONST.PAGE_KEYS.STAFF ? 'active' : ''}">
                                    ${CONST.PAGE_TITLES.STAFF}
                                </a>
                            </li>
                            <li>
                                <a href="placement.html" class="${currentPageKey === CONST.PAGE_KEYS.PLACEMENT ? 'active' : ''}">
                                    ${CONST.PAGE_TITLES.PLACEMENT}
                                </a>
                            </li>
                        </ul>
                    </details>
                </li>

                <li class="nav-item">
                    <a href="partners.html" class="${currentPageKey === CONST.PAGE_KEYS.PARTNERS ? 'active' : ''}">
                        ${CONST.PAGE_TITLES.PARTNERS}
                    </a>
                </li>
                <li class="nav-item">
                    <a href="members.html" class="${currentPageKey === CONST.PAGE_KEYS.MEMBERS ? 'active' : ''}">
                        ${CONST.PAGE_TITLES.MEMBERS}
                    </a>
                </li>
                
                <li class="nav-accordion">
                    <details><summary>${CONST.NAV_ITEMS.ACC_SKILL_INFO}</summary>
                        <ul class="nav-accordion-menu">
                            <li><a href="#">${CONST.PAGE_TITLES.SKILL_CONFIG}</a></li>
                            <li><a href="#">${CONST.PAGE_TITLES.SKILL_EVAL}</a></li>
                        </ul>
                    </details>
                </li>
                <li class="nav-accordion">
                    <details><summary>${CONST.NAV_ITEMS.ACC_WAGE_INFO}</summary>
                        <ul class="nav-accordion-menu">
                            <li><a href="#">${CONST.PAGE_TITLES.WAGE_CONFIG}</a></li>
                            <li><a href="#">${CONST.PAGE_TITLES.DEDUCTION_CONFIG}</a></li>
                            <li><a href="#">${CONST.PAGE_TITLES.WAGE_LEVEL_EVAL}</a></li>
                        </ul>
                    </details>
                </li>
                <li class="nav-item"><a href="#">${CONST.PAGE_TITLES.SAVINGS}</a></li>

                <li class="nav-category">${CONST.NAV_ITEMS.CAT_ACTIVITY_LOG}</li>
                <li class="nav-item">
                    <a href="attendance.html" class="${currentPageKey === CONST.PAGE_KEYS.ATTENDANCE ? 'active' : ''}">
                        ${CONST.PAGE_TITLES.ATTENDANCE}
                    </a>
                </li>
                
                <li class="nav-accordion">
                    <details ${shouldOpenProject ? 'open' : ''}> <summary>${CONST.NAV_ITEMS.ACC_PROJECT_MANAGEMENT}</summary>
                        <ul class="nav-accordion-menu">
                            <li>
                                <a href="projects.html" class="${currentPageKey === CONST.PAGE_KEYS.PROJECTS ? 'active' : ''}">
                                    ${CONST.PAGE_TITLES.PROJECTS}
                                </a>
                            </li>
                            <li>
                                <a href="progress.html" class="${currentPageKey === CONST.PAGE_KEYS.PROGRESS ? 'active' : ''}">
                                    ${CONST.PAGE_TITLES.PROGRESS}
                                </a>
                            </li>
                        </ul>
                    </details>
                </li>
                <li class="nav-accordion">
                    <details><summary>${CONST.NAV_ITEMS.ACC_WELFARE_ACTIVITY}</summary>
                        <ul class="nav-accordion-menu">
                            <li><a href="#">${CONST.PAGE_TITLES.ISP}</a></li>
                            <li><a href="#">(その他...)</a></li>
                        </ul>
                    </details>
                </li>

                <li class="nav-category">${CONST.NAV_ITEMS.CAT_AGGREGATION}</li>
                <li class="nav-accordion">
                    <details><summary>${CONST.NAV_ITEMS.ACC_ACCOUNTING}</summary>
                        <ul class="nav-accordion-menu">
                            <li><a href="#">${CONST.PAGE_TITLES.ACCOUNTING_MONTHLY}</a></li>
                            <li><a href="#">${CONST.PAGE_TITLES.ACCOUNTING_ANNUAL}</a></li>
                        </ul>
                    </details>
                </li>
                <li class="nav-accordion">
                    <details><summary>${CONST.NAV_ITEMS.ACC_ANALYSIS}</summary>
                        <ul class="nav-accordion-menu">
                            <li><a href="#">(${CONST.PAGE_TITLES.DASHBOARD})</a></li>
                        </ul>
                    </details>
                </li>
                
                <li class="nav-category">${CONST.NAV_ITEMS.CAT_SETTINGS}</li>
                <li class="nav-item"><a href="#">${CONST.PAGE_TITLES.USER_ACCOUNTS}</a></li>
                <li class="nav-item"><a href="#">（その他設定）</a></li>

            </ul>
        `;

        // 6. 生成したHTMLをナビゲーションエリアに挿入
        const navElement = document.querySelector(".global-nav");
        if (navElement) {
            navElement.innerHTML = navHtml;
        }
    }

// }); // ← この行を削除