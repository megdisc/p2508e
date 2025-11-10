/**
 * constants.js (静的HTML・モックアップ用)
 * グローバル変数 window.APP_CONSTANTS に定数を定義します。
 */

window.APP_CONSTANTS = {
    // --- アプリケーション基本情報 ---
    APP_NAME: "p2508e",

    // --- ページキー (HTMLの data-page-key と一致させる) ---
    PAGE_KEYS: {
        TOP: "TOP",
        CORPORATION: "CORPORATION",
        OFFICES: "OFFICES",
        STAFF: "STAFF",
        PLACEMENT: "PLACEMENT",
        PARTNERS: "PARTNERS",
        MEMBERS: "MEMBERS",
        ATTENDANCE: "ATTENDANCE",
        PROJECTS: "PROJECTS",
        PROGRESS: "PROGRESS",
    },

    // --- 画面名・ページタイトル ---
    PAGE_TITLES: {
        TOP: "トップ",
        CORPORATION: "法人情報",
        OFFICES: "事業所一覧",
        STAFF: "職員一覧",
        PLACEMENT: "人員配置",
        PARTNERS: "取引先情報",
        MEMBERS: "利用者情報",
        ATTENDANCE: "出欠管理",
        PROJECTS: "案件一覧",
        PROGRESS: "進捗記録",
        // (以下、未作成のページ)
        SKILL_CONFIG: "スキル設定",
        SKILL_EVAL: "スキル評価",
        WAGE_CONFIG: "工賃設定",
        DEDUCTION_CONFIG: "控除設定",
        WAGE_LEVEL_EVAL: "工賃レベル評価",
        SAVINGS: "積立金情報",
        ISP: "個別支援計画",
        ACCOUNTING_MONTHLY: "月次会計",
        ACCOUNTING_ANNUAL: "年次会計",
        DASHBOARD: "分析ダッシュボード",
        USER_ACCOUNTS: "ユーザーアカウント",
    },

    // --- ナビゲーション (HTMLの href と一致させる) ---
    NAV_ITEMS: {
        // (カテゴリ)
        CAT_BASIC_INFO: "基本情報",
        CAT_ACTIVITY_LOG: "活動記録",
        CAT_AGGREGATION: "集計・分析",
        CAT_SETTINGS: "設定",
        // (アコーディオン)
        ACC_FACILITY_INFO: "施設情報",
        ACC_SKILL_INFO: "スキル情報",
        ACC_WAGE_INFO: "工賃・控除情報",
        ACC_PROJECT_MANAGEMENT: "案件管理",
        ACC_WELFARE_ACTIVITY: "福祉事業活動",
        ACC_ACCOUNTING: "会計",
        ACC_ANALYSIS: "分析",
    },

    // (以下、ダミーデータ用の定義)
    DUMMY_USER: {
        name: "山田太郎",
        role: "管理者",
    }
};
