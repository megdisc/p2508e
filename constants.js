/**
 * constants.js
 * アプリケーション全体で使用する定数を定義します。
 * (Next.js/TypeScript 環境への移行を前提とし、ES Module 形式でエクスポートします)
 */

// --- アプリケーション基本情報 ---

export const APP_NAME = "p2508e";

// --- 画面名・ページタイトル ---

export const PAGE_TITLES = {
    // トップ
    TOP: "トップ",

    // 基本情報
    CORPORATION: "法人情報",
    OFFICES: "事業所一覧",
    STAFF: "職員一覧",
    PLACEMENT: "人員配置",
    PARTNERS: "取引先情報",
    MEMBERS: "利用者情報",
    
    SKILL_CONFIG: "スキル設定",
    SKILL_EVAL: "スキル評価",
    WAGE_CONFIG: "工賃設定",
    DEDUCTION_CONFIG: "控除設定",
    WAGE_LEVEL_EVAL: "工賃レベル評価",
    SAVINGS: "積立金情報",

    // 活動記録
    ATTENDANCE: "出欠管理",
    PROJECTS: "案件一覧",
    PROGRESS: "進捗記録",
    ISP: "個別支援計画",

    // 集計・分析
    ACCOUNTING_MONTHLY: "月次会計",
    ACCOUNTING_ANNUAL: "年次会計",
    DASHBOARD: "分析ダッシュボード",
    
    // 設定
    USER_ACCOUNTS: "ユーザーアカウント",
};

// --- グローバルナビゲーション カテゴリ名 ---

export const NAV_CATEGORIES = {
    BASIC_INFO: "基本情報",
    ACTIVITY_LOG: "活動記録",
    AGGREGATION: "集計・分析",
    SETTINGS: "設定",
};

// --- グローバルナビゲーション アコーディオン名 ---

export const NAV_ACCORDIONS = {
    FACILITY_INFO: "施設情報",
    SKILL_INFO: "スキル情報",
    WAGE_INFO: "工賃・控除情報",
    PROJECT_MANAGEMENT: "案件管理",
    WELFARE_ACTIVITY: "福祉事業活動",
    ACCOUNTING: "会計",
    ANALYSIS: "分析",
};


// --- 汎用ステータス定義 ---

/**
 * 案件ステータス (projects.html)
 * CSSクラス名も定義し、ビューとの結合度を下げます。
 */
export const PROJECT_STATUS = {
    NOT_STARTED: { text: "未着手", class: "status-not-started" },
    ACTIVE: { text: "進行中", class: "status-active" },
    COMPLETED: { text: "完了", class: "status-completed" },
    CANCELLED: { text: "中止", class: "status-cancelled" },
};

/**
 * 出欠ステータス (attendance.html)
 */
export const ATTENDANCE_STATUS = {
    ATTENDED: "通所",
    REMOTE: "在宅",
    REST: "休",
    ABSENT: "欠席",
};

/**
 * 案件種別 (projects.html)
 */
export const PROJECT_TYPE = {
    OUTSOURCED: "外部受託",
    IN_HOUSE: "自主事業",
};

/**
 * 案件頻度 (projects.html)
 */
export const PROJECT_FREQUENCY = {
    ONGOING: "継続",
    ONE_TIME: "単発",
};

/**
 * 担当者種別 (projects.html)
 */
export const ASSIGNEE_TYPE = {
    MEMBER: "利用者",
    STAFF: "職員",
    EXTERNAL: "外注先",
};

