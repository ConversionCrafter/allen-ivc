# IVCO - TODO & Progress Tracker

> Last Updated: 2026-02-04 23:00
> Next Session: 2026-02-05 (明天開始)

---

## 🎯 立即開始（明天第一件事）

### ✅ TASK: Test Payload CMS & Add TSMC Data

**Context**:
- Payload CMS 專案已完成初始化
- Companies Collection 已實作完成
- Supabase 連接已配置
- 環境變量已設定

**Steps**:
```bash
# 1. 進入 CMS 目錄
cd /Users/allenchenmac/AI-Workspace/projects/allen-ivco/cms

# 2. 啟動開發服務器
npm run dev

# 3. 等待服務器啟動（約 10-30 秒）
# 輸出應包含：
# - "Payload Admin URL: http://localhost:3000/admin"
# - "Server is running on http://localhost:3000"

# 4. 瀏覽器開啟
open http://localhost:3000/admin
```

**Expected Outcome**:
1. 看到 Payload 註冊頁面
2. 建立第一個管理員帳號（email + password）
3. 登入後看到 Admin Panel
4. 左側選單有 "Companies" 和 "Users"

**Test Data: TSMC**
```
Basic Info:
- Ticker: TSM
- Company Name: Taiwan Semiconductor Manufacturing Company
- Company Name (ZH): 台灣積體電路製造股份有限公司
- Exchange: NYSE
- Sector: Semiconductors
- Country: Taiwan
- Currency: USD
- Total Shares: 25,900 (百萬股)

Stage 1: Integrity Gate
- Integrity Score: 100
- Has Integrity Red Flag: ❌ (不勾選)
- CEO Name: C.C. Wei
- CEO Tenure Years: 7
- Management Stability: 極穩定（10年+）

Stage 2: Historical Facts
- Latest Owner Earnings: 1,200,000 (百萬美元 = 1.2兆)
- Historical OE CAGR 7Y: 15.5 (%)
- Historical OE CAGR 10Y: 18.2 (%)

Moat & Competitive Advantage:
- Moat Type: 技術專利 + 規模經濟（選「複合型」）
- Moat Strength: 極強（台積電級別）
- Biological Advantage:
  "全球唯一純晶圓代工龍頭，擁有最先進的 3nm/2nm 製程技術。
  護城河來自三大優勢：
  1. 技術領先：領先三星、Intel 至少 2 年
  2. 規模經濟：市佔率 60%+，成本優勢明顯
  3. 客戶黏性：Apple、Nvidia、AMD 等核心客戶深度綁定

  生物學優勢：數十年如一日的精準執行，管理層誠信 100%。"

Valuation Status:
- Current Price: 193.50 (2026-02-04 收盤價，需實際查詢)
- Latest IV Low: 180.00 (假設值)
- Latest IV High: 220.00 (假設值)
- Valuation Status: 合理價格（持有）

Position Management:
- In Watchlist: ✅
- Is Core Holding: ✅
- Allocation Percentage: 40
```

**Success Criteria**:
- [ ] 服務器成功啟動，無錯誤訊息
- [ ] Supabase 連接成功（檢查終端無 DB 錯誤）
- [ ] 成功建立管理員帳號
- [ ] 成功新增 TSMC 資料
- [ ] 所有 Tab 的欄位都能正常輸入和儲存
- [ ] 在 Companies 列表看到 TSMC

**Debugging**:
如果遇到問題：
```bash
# 檢查 Supabase 連接
psql "postgresql://postgres:KU23MCfCAuQOb8kS@db.gacttxnlfigoltfjdjmt.supabase.co:5432/postgres" -c "\dt"

# 檢查環境變量
cat .env | grep DATABASE_URL

# 查看錯誤日誌
# 終端會顯示詳細的錯誤訊息
```

---

## 📊 Phase 1: Core Collections (本週目標)

### ✅ COMPLETED: Companies Collection
- [x] Schema 設計
- [x] TypeScript 實作
- [x] 整合到 payload.config.ts
- [x] 支援四階段分析流程
- [x] Tab 式 UI 設計
- [x] 時間戳自動更新

**Files**:
- `/cms/src/collections/Companies.ts` (475 lines)
- `/schemas/payload-cms-schema.md` (完整文檔)

---

### 🔲 TODO: Valuations Collection

**Priority**: P0 (高優先級)
**Estimated Time**: 2-3 hours
**Depends On**: Companies Collection ✅

**Context**:
估值記錄是 IVCO 的核心，記錄每次 IV 計算的完整過程。

**Schema Reference**:
參考 `/schemas/payload-cms-schema.md` 中的 "2. Valuations Collection"

**Key Fields**:
```typescript
{
  company: Relationship → companies (required)
  valuation_date: Date (required)

  // Stage 2: Historical Facts
  historical_oe: Number (required)
  historical_cagr: Number (required)
  total_shares: Number (required)

  // Stage 3: Confidence Coefficient
  confidence_coefficient_low: Number (1.1x - 1.2x)
  confidence_coefficient_high: Number (1.3x - 1.5x)
  confidence_rationale: RichText (必須詳述依據)

  // Calculation Results
  iv_total_low/high: Number (總市值)
  iv_per_share_low/high: Number ⭐ (每股價值 - 強制)

  // Stage 4: Real-time Navigation
  market_price_at_valuation: Number (required)
  deviation_percentage: Number
  recommendation: Select (強烈買入/買入/持有/觀望/避開)

  // Jane's Inverse Challenge
  risk_factors: RichText
  stress_test_result: RichText
}
```

**Steps**:
1. 創建 `/cms/src/collections/Valuations.ts`
2. 複製 Companies.ts 的基本結構
3. 實作上述欄位（參考 Schema 文檔）
4. 加入 payload.config.ts
5. 測試：為 TSMC 建立第一筆估值記錄

**Test Data: TSMC 估值範例**
```
Valuation Date: 2026-02-04
Historical OE: 1,200,000 (百萬)
Historical CAGR: 15.5 (%)
Total Shares: 25,900 (百萬股)

Confidence Coefficient Low: 1.2
Confidence Coefficient High: 1.4
Confidence Rationale:
"基於以下三點給予 1.2x-1.4x 信心係數：
1. AI 晶片需求強勁，2nm 製程 2025 量產
2. 美國亞利桑那廠 2025 投產，地緣風險降低
3. 管理層執行力 100%，過去 5 年承諾達成率 95%+"

IV Total Low: 4,668,000 (百萬 = 4.67兆)
IV Total High: 5,446,000 (百萬 = 5.45兆)
IV Per Share Low: 180.23
IV Per Share High: 210.27

Market Price at Valuation: 193.50
Deviation Percentage: -2.5% (略低於 IV 中值)
Recommendation: 買入

Risk Factors (Jane's Warning):
"1. 地緣政治風險：兩岸關係緊張
2. 競爭壓力：三星積極追趕 3nm 製程
3. 客戶集中：Apple 佔營收 25%，單一客戶風險"

Stress Test Result:
"若股價大跌 50% 至 $96.75：
- Allen 持股市值：從 $X 降至 $Y
- 質押比例 35%，維持率 130%
- 安全邊際：股價可再跌 45% 才觸及斷頭線
- 結論：✅ 質押安全"
```

**Success Criteria**:
- [ ] Valuations Collection 成功建立
- [ ] 與 Companies 的關聯正常運作
- [ ] 為 TSMC 建立第一筆估值記錄
- [ ] 所有計算欄位正確顯示
- [ ] 可以看到 IV 區間與市價對照

---

### 🔲 TODO: Financial_Data Collection

**Priority**: P0
**Estimated Time**: 2 hours
**Depends On**: Companies Collection ✅

**Context**:
儲存季度/年度財務數據，用於計算業主盈餘。

**Key Fields**:
```typescript
{
  company: Relationship
  period_type: Select (annual | quarterly)
  fiscal_year: Number
  fiscal_quarter: Select (Q1/Q2/Q3/Q4)

  // Income Statement
  revenue: Number
  net_income: Number
  depreciation_amortization: Number

  // Cash Flow
  operating_cash_flow: Number
  total_capex: Number
  maintenance_capex: Number ⭐
  growth_capex: Number
  working_capital_change: Number

  // Calculated: Owner Earnings
  owner_earnings: Number (自動計算或手動輸入)
  owner_earnings_per_share: Number

  // Other Metrics
  roic: Number
  fcf: Number
}
```

**Steps**:
1. 創建 `/cms/src/collections/FinancialData.ts`
2. 實作上述欄位
3. 加入 payload.config.ts
4. 測試：為 TSMC 輸入 2023 年財報數據

---

## 📅 Phase 2: Advanced Features (下週)

### 🔲 TODO: Events Collection
**Priority**: P1
**Estimated Time**: 2 hours

### 🔲 TODO: Commitments Collection
**Priority**: P1
**Estimated Time**: 2 hours
**Note**: 實作「預測對帳單」機制

### 🔲 TODO: Integrity_Scores Collection
**Priority**: P1
**Estimated Time**: 1 hour

---

## 🛠️ Phase 3: CLI Tools (並行開發)

### 🔲 TODO: ivco-calc CLI

**Priority**: P0 (與 Payload 並行)
**Language**: Python
**Estimated Time**: 4 hours

**Context**:
核心計算引擎，實作 IV 公式。

**Formula**:
```python
def calculate_iv(
    historical_oe: float,
    historical_cagr: float,
    confidence_low: float,
    confidence_high: float,
    total_shares: float
) -> dict:
    """
    計算 Intrinsic Value 區間

    Returns:
        {
            'iv_total_low': float,
            'iv_total_high': float,
            'iv_per_share_low': float,
            'iv_per_share_high': float
        }
    """
    # TODO: 實作計算邏輯
    pass
```

**Steps**:
1. 創建 `/cli/ivc_calc.py`
2. 實作核心計算函數
3. 加入 CLI 介面 (Click 或 Typer)
4. 測試：用 TSMC 數據驗證

**Usage**:
```bash
ivco-calc --oe 1200000 --cagr 15.5 --conf-low 1.2 --conf-high 1.4 --shares 25900
```

**Expected Output**:
```
IVCO Calculation Results
=======================
Input:
  Historical OE: $1,200,000M
  Historical CAGR: 15.5%
  Confidence Range: 1.2x - 1.4x
  Total Shares: 25,900M

Output:
  IV Total Range: $4,668M - $5,446M
  IV Per Share Range: $180.23 - $210.27

Recommendation:
  [Based on current price input]
```

---

### 🔲 TODO: ivco-fetch CLI

**Priority**: P1
**Language**: Python
**Estimated Time**: 6-8 hours

**Context**:
自動化財報數據抓取工具。

**Data Sources**:
- SEC EDGAR (10-K, 10-Q, 8-K)
- Yahoo Finance
- Financial Modeling Prep API

**Steps**:
1. 研究 SEC EDGAR API
2. 實作財報下載功能
3. 解析 XBRL 格式
4. 提取關鍵數據
5. 輸出為 JSON（與 Payload Schema 對齊）

---

## 🎨 Phase 4: Playground (後續)

### 🔲 TODO: Playground MVP

**Priority**: P2
**Tech**: HTML + JavaScript + Chart.js
**Estimated Time**: 4 hours

**Features**:
- 即時調整信心係數滑桿
- 即時顯示 IV 區間變化
- 市價對照視覺化
- 決策建議燈號

---

## 📝 Documentation Updates Needed

- [ ] 更新 `/CLAUDE.md` Decision Log（今日決策）
- [ ] 更新 Knowledge Graph（今日成果）
- [ ] 建立 `/docs/api-spec.md`（API 規格）
- [ ] 建立 `/docs/cli-guide.md`（CLI 工具指南）

---

## 🐛 Known Issues

目前無已知問題。

---

## 💡 Future Enhancements

- [ ] n8n 整合（自動化財報監控）
- [ ] Qdrant 向量搜尋（法說會逐字稿語義搜尋）
- [ ] 即時股價 API 整合
- [ ] Telegram/Slack 警報通知
- [ ] Mobile-responsive Admin Panel

---

## 📚 Reference Links

- Payload CMS Docs: https://payloadcms.com/docs
- Supabase Docs: https://supabase.com/docs
- SEC EDGAR: https://www.sec.gov/edgar
- IVC Framework 完整說明: `/allen-ivco/CLAUDE.md`
- Schema 設計文檔: `/allen-ivco/schemas/payload-cms-schema.md`
