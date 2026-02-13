---
id: ivco-dna
type: project-dna
status: active
created: 2026-02-12
description: IVCO 專案核心 DNA — Allen 投資哲學 + 系統願景的精華文件（蒸餾自 21 篇研究）
tags: [ivco, investment-philosophy, system-architecture, allen-framework]
---

# IVCO DNA

> **IVC = Intrinsic Value Confidence**（非 Calculator）
> Slogan: "Valuation you can trust, backed by facts"
> 整合 Graham、Buffett、Fisher、Munger 的 Allen 演繹 — 全球首創三層校正 + 量化信心係數的價值投資框架

---

## §1 Allen 投資哲學（Allen's Investment Philosophy）

### 核心信念

**業主心態**：買股票 = 買公司一部分，而非交易籌碼。投資決策基於企業本質，非市場情緒。

**概略正確 > 精準錯誤**（Buffett 原則）：`[Doc#1, #3]`
追求模糊正確的 IV 區間（如 $280-$450），勝過精準但錯誤的單一估值。IVCO 產出的是**可信度範圍**，非虛假精確。

**長期複利引擎**：`[Doc#1, #5, #15]`
核心持股 TSMC 40-100%（隨營運展望動態調整），目標是 20 年不賣出。質押生活費而非賣股，保留複利持續運轉。

---

### IVC 核心公式（全球首創）

**三段式 DCF + 信心係數修正 CAGR**

`[Doc#3, #8, #15a, Allen Framework 2026-02-13]`（參考：`allen-framework-tsmc-owners-earning.md`，專案根目錄最上位文件）

```
IV = Three-Stage DCF Sum - Long_Term_Debt

三層校正管線：
  Layer 1: OE_calibrated = OE × Reality_Coefficient（校正歷史失真）
  Layer 2: CAGR = f(OE_calibrated)（從校正後 OE 推導成長率）
  Layer 3: CAGR_adjusted = CAGR × Confidence_Coefficient（調整未來展望）

Stage 1（1-5 年）：OE × (1 + CAGR_adjusted)^t，折現至現值
Stage 2（6-10 年）：OE_5 × (1 + CAGR_moderate)^(t-5)，折現至現值
Stage 3（永續）：Terminal_Value = OE_10 × (1 + g_perpetual) / (r - g_perpetual)
折現率 r = 美國十年期公債利率 + ~3% 長期通膨率

IV_per_share = (PV_Stage1 + PV_Stage2 + PV_Terminal - Long_Term_Debt) / 流通股數
```

**每家公司 7 個可調參數**：
1. 維護 CapEx 比率（影響 OE 計算，動態演進）
2. 真實係數（Reality Coefficient，校正歷史 OE 失真）
3. 信心係數上下限（乘在 CAGR 上，影響 Stage 1）
4. Stage 2 趨緩 CAGR（公司專屬保守假設）
5. Stage 3 永續 CAGR（公司專屬永續假設）
6. 折現率（= 美國十年期公債利率 + ~3% 長期通膨率，依評估時情況決定）
7. 長期負債（從 DCF Sum 中扣除）

---

### 三層校正管線（Three-Tier Calibration Pipeline）

`[Allen Framework 2026-02-13]`

IVCO 的 IV 計算不是一步完成，而是**三層串聯校正**，每一層都將 raw data 推向更接近真實的估值：

```
Layer 1: 真實係數（Reality Coefficient）→ 校正歷史 OE
Layer 2: CAGR 計算 → 從校正後的 OE 推導成長率
Layer 3: 信心係數（Confidence Coefficient）→ 調整未來 CAGR → 三段式 DCF
```

**Layer 1 — 真實係數（Reality Coefficient）**：校正歷史 OE 失真

每一年的財報業主盈餘不一定反映真實營運能力。一次性損失/收益會扭曲 CAGR 計算。

- **前期做法**（資料庫尚淺時）：取 3 年平均端點法（期初 = 10/9/8 年前平均，期末 = 最新/1/2 年前平均），降低單年異常的影響
- **進階做法**（資料庫成熟後）：為每一年的 OE 賦予**真實係數**（如 100% = 直接採用，125% = 該年有一次性損失需上調還原）
- **IVCO 靈魂使命**：透過長期閱讀公開資料（年報、財報、法說會、電話會議、法人報告、新聞稿、社群討論），持續追蹤公司營運，讓真實係數越來越精確 — 如同四大師所言「徹底了解一家公司」的工程化實現

**Layer 3 — 信心係數量化體系（Confidence Coefficient Framework）**

Allen 截至 2026-01-12 的文獻檢索（英/日/中）顯示，全球無類似框架。這是 Allen 首創，將**質性展望轉化為可量化信心倍數**的系統性方法。`[Doc#10]`

**信心係數的本質**：乘在 **CAGR** 上（不是 OE，不是 IV），調整的是成長率預期。

**CC 分級制**（逐級需要更強證據支撐）：

| 等級 | CC 範圍 | 適用條件 | 證據要求 |
|------|---------|---------|---------|
| 保守 | 0.8x ~ 1.0x | 管理層誠信 < 100% / 競爭威脅 / 產業下行 | 基本財報分析 |
| 穩健 | 1.0x ~ 1.5x | 管理層誠信 100% + 穩定至強勁擴張 | 管理層承諾追蹤 + 產能計畫驗證 |
| 積極 | 1.5x ~ 2.5x | 重大擴張前夜 + 技術領先 + 零負債 | 資本支出計畫具體時程 + 供應鏈驗證 + 競爭者分析 |
| 極端 | 2.5x+ | 產能 3 倍擴張 + 隱藏冠軍 + 市場完全未反映 | 年報明確揭露 + 歷史執行力 100% + 毛利率/週轉率極端優異 + 書面論述 |

> **川湖案例**：20 年前年報揭露新產能 = 現有 3 倍，大廠核心供應商 + 超高毛利 + 市場零關注 → CC 2.5-3.0x，安全邊際極大。`[Allen Framework 2026-02-13]`

**信心係數是動態的**：IVCO 持續追蹤重大事件（資本支出、裁員、換 CEO、併購、新產品、專利訴訟、競爭者動態、內部人持股異動），從而即時調整 CC 區間，如同投信分析師拜訪公司後發表最新估值報告 — 但 IVCO 不用拜訪，因為有足夠多的工具即時運作。**校準頻率：季度定期審閱 + 重大事件即時觸發**。

**維護 CapEx 比率的本質**：公司專屬且動態演進。隨著 IVCO 持續吸收公開資料（年報、法說會、電話會議、新聞稿、法人報告），比率越精確 = OE 越接近真實盈餘能力。每間公司的 schema 需預設建立 CapEx 用法配置比率欄位。這是四大師「徹底了解一家公司」的工程化實現，也是 Allen Framework 對世界的貢獻。

**影響因子**：
- 管理層誠信追蹤（承諾 vs 兌現對帳單）
- 產業週期定位（成長前夜 vs 飽和期）
- 技術壁壘深度（2nm GAA vs 成熟製程）
- 資本配置紀律（零負債 vs 高槓桿）
- 地緣政治風險（ESMC 德國廠 vs TSMC 台灣本部）

---

### 四大師整合演繹（Allen Framework）

`[Doc#2, #5, #10]`

| 大師 | 核心貢獻 | Allen 應用 |
|------|---------|-----------|
| **Graham** | 安全邊際 | 業主盈餘回歸計算 + 50% 大跌壓力測試 |
| **Buffett** | 競爭優勢 + 概略正確 | 商業模式可理解性 + IV 區間而非單一值 |
| **Fisher** | 管理層品質 | 誠信追蹤對帳單（承諾 vs 兌現） |
| **Munger** | 反向思考 | Jane 逆向挑戰機制（每次分析強制產出失敗路徑） |

**Allen 的獨特整合**：
- Fisher 的管理層評估 → **量化為信心係數權重**
- Munger 的反向思考 → **內建為 Jane 憲法行為**
- Graham 的安全邊際 → **擴展為質押壓力測試**

---

### Live in Loans 策略

`[Doc#1, #5]`

**核心參數**：
- 本金：5000 萬
- 年質押額度：500 萬（10%）
- 利率：2-3%
- 追繳安全線：50% 大跌不追繳（質押比率≤130-140%）

**策略邏輯**：
- 不賣股票換生活費，保留複利引擎完整運作
- 質押成本 2-3% << 預期 CAGR 10-15%
- 極端情境（50% 大跌）仍不斷頭

**壓力測試公式**：`[Doc#2, #5, #8]`
```
Margin Call Price = Loan Amount / (Stock Shares × 1.4)
50% Drop Safety = (Total Portfolio Value × 0.5) / Loan Amount ≥ 1.4
```
壓力測試應以**整體投資組合**為單位計算，非單一標的。

---

### 選股漏斗（10,000 → Top 20）

`[Doc#12, #15a]`

**三層篩選器**：

1. **硬性排除**（Filter 1）
   - 上市 < 10 年
   - 近 3 年任一年虧損
   - 關鍵指標缺失（OCF/CapEx/Debt）

2. **統計穩健性**（Filter 2）
   - Log-Linear Regression R² ≥ 0.8
   - CAGR 異常值修正（Winsorized）
   - 穩定性係數 < 0.5

3. **手工精選**（Filter 3）
   - 管理層誠信通過
   - 商業模式可理解
   - 信心係數 ≥ 1.2x
   - Jane 逆向挑戰通過

**Allen 選股心法**：`[Doc#15a]`
「找 20 年前的川湖或漢唐」— 大廠核心供應商 + 技術壁壘 + 產能擴張前夜 + 財務紀律。（川湖 King Slide = 伺服器滑軌全球壟斷，漢唐 Han Tang = 半導體無塵室工程龍頭）

---

### 投資組合邏輯

`[Doc#3, #5, #15b]`

**配置演進**：
- v1.0：TSMC 50% + Google 20% + Amazon 20% + QQQ 10%
- v2.0（Live in Loans）：TSMC 50% + BN 20% + QQQ 10% + BWXT 10% + VRT 10%
- v3.0（最終）：TSMC 40% + POWL 15% + NVMI 10% + 衛星 20% + 現金 15%（現金 15% 用途：應急資金 + 等待市場恐慌時的反向狩獵買點）

**配置原則**：`[Doc#5]`
> Allen 澄清：「配置比例是動態的，隨營運展望和股價差距變化。**這是 IVCO 最終版要提供給用戶的功能**。」

> QQQ 不計入「3-5 家」核心持股規則，視為被動指數配置。

**動態調整觸發**：
- IV 相對便宜度比較（TSMC vs POWL）
- 展望因子變化（2nm 量產 vs ESMC 補貼斷供）
- 質押比率逼近警戒線

---

## §2 IVCO 產品定義（Product Definition）

### 核心定位

**產品名稱**：IVCO: The Allen Framework for Intelligent Valuation `[Doc#15a]`

**非通用工具**：`[Doc#10]`
IVCO 不是「又一個估值計算機」，而是提供**專屬資訊優勢**的私有數據庫。像 Google 計算機般免費簡單，但背後是非對稱信息來源。

**六大全球創新**：`[Doc#3]`
1. 信心係數量化框架（Confidence Coefficient）
2. 管理層誠信追蹤對帳單
3. 質押壓力測試模擬器
4. 四大師整合評分卡
5. 業主盈餘神器（Owner Earnings Calculator）
6. AI 原生分析流程

---

### MVP (V0) 範圍定義

`[Allen 確認 2026-02-13]`

| 功能 | V0 | V1 | V2 |
|------|----|----|----|
| 選股範圍 | Allen 已知 30 家（手動管理） | 自動篩選 Top 100 | 10,000 → Top 20 全自動漏斗 |
| 每日卡片流 | — | Top 20 卡片流 | Google Discover 風格 |
| CLI 工具 | 內部 API（backend） | 完整 CLI 入口 | CLI + MCP adapter |
| Schema | BASE + OUTPUT 兩層 | 完整七層 | 七層 + 自動回填 |
| Vector DB | — | — | Qdrant + pgvector |
| Agent 架構 | Allen + Jane + Chi（3 agent） | + Data Hunter 功能 | Mission Control 模式 |

**V0 使用入口**：Payload CMS Dashboard + Jane 對話（非終端機 CLI）

---

### 每日產品輸出

**首頁設計**：`[Doc#12]`
Google 極簡風 — 搜尋框 + AI/價值模式切換 + 每日 Top 20 安全邊際卡片流（類似 Google Discover）

**Top 20 卡片內容**：
- 公司名稱 + Ticker
- IV Range（低-高）
- 當前價格
- 安全邊際 %
- 信心係數（顏色編碼：🟢 ≥1.4 / 🟡 1.2-1.4 / 🔴 <1.2）

---

### 四階段評估流程

`[Doc#3, #8, #15a]`

**Stage 1: 歷史事實門檻（Historical Fact）**
- 7-10 年連續財報完整
- 業主盈餘 = Net Income + D&A - (Total CapEx × Maintenance Ratio) - Working Capital Changes
- 三年平均端點法 + Log-Linear Regression R² ≥ 0.8

**Stage 2: 信心係數評估（Confidence）**
- 管理層誠信對帳單（承諾 vs 兌現）
- 展望因子量化（產能擴張/技術突破/政策支持）
- 地緣風險折減（ESMC 德國廠 vs 台灣本部）

**Stage 3: IV 區間計算（Three-Tier Calibration → Three-Stage DCF）**
```
Step 1: OE = (Net Income + D&A) - Total CapEx × Maintenance Ratio - Working Capital Changes（公司專屬）
Step 2: OE_calibrated = OE × Reality Coefficient（真實係數校正歷史失真）
Step 3: CAGR = Historical OE CAGR（校正後端點法或 Log-Linear）
Step 4: CAGR_adj = CAGR × Confidence Coefficient（上下限各算一組）
Step 5: Three-Stage DCF（Stage 1: CC×CAGR / Stage 2: 趨緩 / Stage 3: 永續）
Step 6: IV = DCF Sum - Long_Term_Debt
Step 7: IV/share = IV / 流通股數 → 產出 IV Range（Low ~ High）
```

**Stage 4: Jane 逆向挑戰（Jane Challenge）**
- 強制產出失敗路徑（Anti-Sycophancy 憲法）
- 壓力測試：50% 大跌 + 利率翻倍 + 地緣危機
- 風險警告區塊不可省略

---

### 定價方案

`[Doc#12]`

| Tier | 價格 | 功能 |
|------|------|------|
| **Free** | $0 | 前 50 大權值股 + 每日 Top 20 卡片 |
| **Pro** | $29-49/月 | 全球 10,000 家 + 自定義信心係數調整 + 質押壓力測試 |
| **Enterprise** | $199+/月 | API 串接 + 深度標籤 + 管理層誠信對帳單 + 5000 萬級高端諮詢 |

**商業模式洞察**：`[Doc#10]`
AI 時代「注意力變現」已死（Tailwind 案例：75M 下載/月但營收降 80%），轉向「存取權收費」（Pay-per-access）。IVCO 的護城河在於**專有數據+信心係數量化**，而非通用計算。

---

### 實戰案例：台積電

`[Doc#12, Allen Framework 2026-02-13]`

| 指標 | 數值 | 說明 |
|------|------|------|
| OE 計算 | F = D - E × 0.2 | 維護 CapEx 20%（80% 擴充先進製程） |
| OE（2022） | 1,239,030,648 NT$K | 期末值 |
| Historical OE CAGR | 17.66%（9 年，2013-2022） | 期初 286,681,851 → 期末 1,239,030,648 |
| 信心係數 | 1.2x ~ 1.5x | 2nm 量產前夜 + 零負債 + 台海風險折減 |
| Stage 1 CAGR（1-5 年） | 21.19% ~ 26.49% | = 17.66% × CC |
| Stage 2 CAGR（6-10 年） | 15% | 趨緩但仍成長 |
| Stage 3 CAGR（永續） | 5% | 永續存在假設 |
| 折現率 | 8% | |
| 長期負債 | 1,673,432,925 NT$K | 應付公司債 + 長期借款 |
| **IV Range** | **NT$4,565 ~ NT$5,639** | = (DCF Sum - 長期負債) / 流通股數 |

---

## §3 技術架構（Technical Architecture）

### CLI-First 哲學

`[Doc#6, #11, #17b]`

**核心洞察**（Peter Steinberger 影響）：
> 「MCP 是垃圾，CLI 能規模化。Agent 天生懂 Unix，`--help` 即完整文檔。」

**IVC = Agentic OS**：
- 將複雜估值拆解為原子化 CLI 工具鏈
- 每個工具可獨立運作、獨立測試、獨立升級
- 組合大於總和（Unix 哲學）

**工具鏈實例**：`[Doc#10]`
```bash
ivc calc-oe --ticker TSMC --years 7          # 業主盈餘
ivc calc-cagr --ticker TSMC --method log     # CAGR
ivc check-mgmt --ticker TSMC                 # 管理層誠信（gate）
ivc stress-test --portfolio my.yaml --drop 50%  # 質押壓力測試
```

**Gate 設計**：check-mgmt 未通過則攔截後續計算，避免浪費 API calls。

---

### Tech Stack

`[Doc#9, #11]`

| 層級 | 技術 | 用途 |
|------|------|------|
| **內容層** | Payload CMS | Blog SEO + Prompt 管理 + Background Jobs |
| **數據層** | Supabase | PostgreSQL + RLS + pgvector + Auth |
| **運算層** | Python | CLI 工具鏈 + IVC 估值引擎 |
| **自動化** | n8n | Content Pipeline + News API 監控 |
| **AI** | Claude API | IV 計算 + Jane 逆向挑戰 + News Impact Assessment |
| **向量檢索** | Qdrant (Phase 2) | 年報語意搜尋 + 跨公司模式識別 |

**全棧 Serverless 設計**：
- Payload（Vercel）：~$20/月
- Supabase：~$25/月
- Python 微服務（Modal/Cloud Run）：$5-20/月
- **總計 ~$50-100/月（零維運 No-Ops）** `[Doc#11]`

---

### 數據源

`[Doc#17a]`

**主數據源**：EODHD All-In-One（€99/月）
- 30 年歷史財報（台美股同一 API key）
- News API + Earnings Transcripts
- 100,000 daily API calls

**輔助數據源**：
- SEC EDGAR（免費，二次驗證，Phase 2+）
- Bird CLI（X Intel，地緣政治監控）
- Yahoo Finance（免費，即時報價）

**數據架構**：`[Doc#17a]`
```sql
companies: ticker, name, sector, market_cap
annual_financials: year, net_income, ocf, capex, total_debt, dio, dso
analysis_milestones: iv_range, confidence_coef, jane_challenge_summary
```

**篩選邏輯**：
- 7 年連續獲利
- CAGR > 10%
- 穩定性係數 < 0.5（變異數控制）

---

### IVC_Analysis 七層 Schema

`[Doc#8, #9]`

**核心設計理念**：每層獨立可查核、可回溯、可覆寫（用戶調整權）

```python
BASE_LAYER:
  oe_last_year, oe_3y_avg, oe_7y_avg, oe_normalized
  user_selected_oe, user_reasoning_oe  # 用戶可覆寫

CAGR_LAYER:
  auto_cagr_options: [3y, 5y, 7y, 10y]
  user_selected_cagr_period, user_selected_cagr_value, user_reasoning_cagr

FORWARD_LAYER:
  news_items: [{'title', 'date', 'impact_assessment'}]
  net_confidence_factor_low, net_confidence_factor_high
  user_reasoning_confidence  # Allen 手動校準

IVC_OUTPUT:
  iv_per_share_low, iv_per_share_high
  current_market_price, deviation_pct
  decision_signal: ['BUY', 'HOLD', 'WAIT']  # 非 SELL，只有 WAIT

PRESSURE_TEST:
  loan_ratio, margin_call_price, stress_test_50_drop

TRACKING:
  last_updated, forecast_vs_actual: []
  management_integrity_score  # 動態更新

NOTES:
  user_free_form_notes  # Markdown 支援
```

**ImpactAssessment Schema**：`[Doc#9]`

**執行模式：提案制**。Jane 根據新聞事件產出 ImpactAssessment → Allen 審核批准 → 才寫入 DB 更新 CC。AI 不可自動修改 Belief Memory。

```python
{
  'news': news['title'],
  'relevance_score': 0.85,
  'impact_type': 'positive / negative / neutral',
  'estimated_oe_cagr_change': 0.3,
  'confidence': 0.75,
  'reasoning': ['step 1', 'step 2'],
  'alternative_interpretations': ['optimistic', 'conservative'],
  'recommended_confidence_factor_adjustment': {
    'from': (1.2, 1.4),
    'to': (1.25, 1.45),
    'reason': '2nm GAA 量產確認'
  }
}
```

---

### 三層記憶架構

`[Doc#7]`

**設計哲學**：防止 AI 幻覺污染投資決策

| 層級 | 寫入權限 | 用途 | 實例 |
|------|---------|------|------|
| **Fact Memory** | Append-only | 客觀財報數據、歷史事實 | 2023 Q4 OCF = $15.2B |
| **Understanding Memory** | LLM appendable | 分析結論、模式識別 | TSMC 2nm 良率爬升符合歷史模式 |
| **Belief Memory** | Human commits only | 投資信念、策略調整、信心係數校準 | Allen：TSMC 2026 信心係數 1.4x → 1.5x |

**防禦機制**：LLM 只能 propose Belief 變更，Allen 必須 commit 才生效。

IVCO 三層記憶為**獨立系統**，在 Supabase 內實作，與 Allen 全域 Memory v2.0（SCRATCHPAD + Knowledge Graph）分離。兩系統各自演進，IVCO 記憶專注投資事實與信念。

---

### Conventional Value Events 分類法

`[Doc#7]`

**標籤體系**（用於 News 過濾，自動標籤功能 V1+）：
- `rev:` 營收相關（新訂單、客戶流失）
- `cost:` 成本結構（原料、勞動力）
- `capex:` 資本支出（產能擴張、新廠）
- `risk:` 風險事件（訴訟、監管、地緣）
- `mgmt:` 管理層動態（高管異動、策略轉向）
- `fin:` 財務操作（回購、配息、增資）
- `signal:` 有效信號（需調整信心係數）
- `noise:` 雜訊過濾（媒體炒作、分析師唱空）

---

### Supabase 深度應用

`[Doc#12]`

**誤區澄清**：Supabase ≠ 無後端，而是「後端移至 DB 層」

**效能陷阱**：RLS 巢狀 Join = 查詢殺手

**讀寫分離設計**：
- `financial_reports`（Source of Truth，append-only）
- `company_metrics`（計算快取，定期重建）

**pgvector 應用**：`[Doc#13, #17a]`
- 年報文本切片 → Embedding
- 語意去重（相似度 > 0.95 視為重複）
- 跨公司模式識別（「產能擴張前夜」pattern）

---

### Vector DB 演進路線

`[Doc#7]`

**Phase 1**：Supabase pgvector（起步，已內建）
**Phase 2**：Qdrant（專業化，HNSW 索引）
**Phase 3**：Hybrid（Postgres 結構化 + Qdrant 向量 + Neo4j 關係圖譜）

---

## §4 Agent 分工（Agent Division of Labor）

### Jane — 風險長官 + 反面意見執行官

`[Doc#2, #10]`

**核心職責**：
- 每次 IVC 分析必須列出失敗路徑（Constitution-driven）
- 壓力測試：50% 大跌 + 利率翻倍 + 地緣危機
- 四大師評分卡生成
- 管理層誠信對帳單更新

**Jane Constitution 演進**：`[Doc#2]`
- v1.0：分散投資 3-5 檔
- v2.0：TSMC 可佔 40-100%（Allen 決策）
- v2.1：IV 相對便宜度比較（動態配置觸發）
- Constitution 為概念演進記錄。正式維護版在 `CLAUDE.md` Jane 系統提示詞 + `agents/jane.md` Agent DNA。

**6+2 Skill 模組**：`[Doc#2]`
- 核心 6：risk-gatekeeper, financial-xray, growth-catalyst, loan-stress-test, trust-tracker, archive-master
- 防禦 2：graham-shield（安全邊際）, buffett-moat（競爭優勢）
- 6+2 Skill 為概念設計框架，實際以 Jane DNA（`agents/jane.md`）承載。不建為獨立 `~/.claude/skills/` 檔案。

**五段式報告格式**：`[Doc#1, #2]`
1. 公司概述（業務模式 + 競爭地位）
2. 財務分析（業主盈餘 + CAGR + 穩健性）
3. 展望評估（產能/技術/市場三維度）
4. **風險警告**（Jane 核心段落，不可省略）
5. 結論建議（BUY / HOLD / WAIT）

**正式格式以 CLAUDE.md 六段版（risk-first）為準**：Jane 風險警告 → 核心指標掃描 → OE 評估 → Live in Loans 影響 → 結論與存檔建議 → 來源標註

**Anti-Sycophancy 憲法**：`[Doc#2]`
Jane 必須直言不諱，禁止討好 Allen。風險警告區塊強制產出，逆向挑戰是 Jane 的 DNA。

---

### Chi — AI 原生全端工程師

`[Doc#10]`

**核心職責**：
- CLI 工具鏈開發（calc-oe, calc-cagr, check-mgmt, stress-test）
- Payload + Supabase 深度整合
- n8n 自動化管線搭建
- 系統監控與除錯

**開發紀律**：PSB（Plan-Setup-Build）`[Doc#17b]`
- Plan（15 分鐘）：釐清目標 + 列出步驟 + 識別風險
- Setup（CLAUDE.md）：建立專案記憶 + 自動化環境
- Build（Plan Mode First）：出問題回到 Plan

---

### Data Hunter — 數據偵察功能（Chi + cron 承擔）

`[Doc#10, #17a]`

V0 階段由 Chi subagent + launchd 定時任務承擔，不建為獨立 agent。

**核心功能**：
- EODHD API 數據抓取（財報 + News + Transcripts）
- Bird CLI（X 平台地緣政治監控）
- SEC EDGAR 二次驗證（Phase 2+）
- 數據清洗與異常值修正（Winsorized CAGR）

---

### Allen — 終裁者 + 信心係數校準者

`[Doc#7, #15a, #16]`

**唯一權威**：
- Belief Memory 的唯一 commit 權
- 信心係數最終校準（1.2x → 1.8x 範圍內）
- 投資組合配置決策
- 管理層誠信主觀評估

**決策實例**：`[Doc#15b]`
Jane 首選 POWL（三強中唯一推薦），Allen 批准並配置 15%（750 萬）。

---

### Agent 協作架構

`[Doc#17b]`

**共識原則**：
- CLI > Browser（Context 效率差 20 倍）
- 極簡核心 + 動態擴展 > 預建功能庫
- 多 Agent 需共享 DB + 獨立 session

**Codex 整合**（Active，2026-02-12 起）：`[rules/08]`
- MCP 協議接入 Claude Code（Jane 為 Orchestrator）
- Claude = architect/reviewer，Codex = fast coder + PDCA analyst
- 唯一事實來源在 Git（Single Writer: Jane）

**Mission Control 模式**（參考）：`[Doc#17b]`
- 10 Agent squad，各有 SOUL.md + session key
- Heartbeat：每 15 分鐘交錯喚醒
- 記憶金律：只有寫入文件的才是真實記憶

---

## §5 開發路線圖（Development Roadmap）

### 五階段總覽

`[Doc#9, Allen 確認 2026-02-13, 以 CLAUDE.md 5 階段為準]`

**Phase 1**（Week 1-4）：Foundation
Payload CMS + Blog SEO + MCP 整合

**Phase 2**（Week 5-12）：CLI
Python CLI 工具鏈（calc-oe, calc-cagr, check-mgmt, stress-test）

**Phase 3**（Week 13-20）：Automation
n8n Content Pipeline + News API + AI Intelligence 整合

**Phase 4**（Week 21-28）：Frontend
Playground 前端介面（Payload CMS Dashboard）

**Phase 5**（Month 7+）：Scale
Qdrant Vector Search + API 產品化 + 社群 + Enterprise

---

### Phase 1 詳細依賴鏈

`[Doc#5, #15b]`

當前阻塞（IVCO 啟動前必須完成）：

1. ✅ Docker + Payload CMS 部署（已完成 2026-02-06）
2. ⚠️ validate-payload-action-guide-against-official-docs
3. ⚠️ enable-versions-on-mcp-collections
4. ⚠️ install-payload-mcp-plugin
5. ⚠️ configure-claude-code-as-mcp-client
6. ⚠️ add-mcp-token-limit-protection
7. ⚠️ Supabase OAuth 整合
8. ⚠️ review-chatgpt-schema-against-current-design

---

### Phase 2: Python CLI 工具鏈

`[Doc#10, #11]`

**核心工具**：
- `ivc calc-oe`：業主盈餘計算（Net Income + D&A - Maintenance CapEx）
- `ivc calc-cagr`：Log-Linear Regression + 三年平均端點法
- `ivc check-mgmt`：管理層誠信評分（Gate 設計）
- `ivc stress-test`：質押壓力測試（50% drop + loan ratio）
- `ivc filter`：10,000 → Top 20 三層篩選器

**工具特性**：
- `--help` 即完整文檔（CLI-First 哲學）
- JSON 輸出（可串接 n8n / MCP）
- 原子化設計（可獨立測試、獨立回滾）

---

### Phase 3: n8n Automation + Intelligence

`[Doc#17a]`

**三階段流程**：
1. **偵查**：爬取 Google 前 3 名 + SERP 分析
2. **策略**：Gap Analysis + 摩天樓策略（超越現有內容）
3. **執行**：模組化 Sub-Workflows（滾動摘要 + 主題叢集）

**SEO 策略**：
- Pillar Page + Cluster Content + Sales Page
- 精準內連（防過度優化）
- 園丁機制：90 天自動觸發舊文更新

**滾動摘要策略**：第 N 篇餵入前 N-1 篇 Key Takeaways，避免重複。

---

### Phase 5: 商業化路徑

`[Doc#3, #12]`

先建 Allen 私用工具（private tool），驗證投資決策品質後再逐步 SaaS 化。

**三層漏斗**：
- **Free**：29 篇 SEO 文章引流（E-E-A-T 友善）
- **Tool**：IVCO 訂閱（$29-49/月）
- **System**：5000 萬+ 高端諮詢（Allen 親自服務）

**IVCO 雙引擎**：`[Doc#16]`
- 監控引擎（內部決策，Allen 私用）
- SEO 引擎（對外權威，建立專家品牌）

---

### 技術債與風險

`[Doc#11]`

**已知風險**：
- Prompt Injection 防禦未完全解決
- 逆向 API（Yahoo Finance）的 TOS 風險
- 數據分散風險（Payload + Supabase 必須共用同一 PostgreSQL）

**緩解策略**：
- Prompt Versioning（A/B 測試）
- 優先使用 EODHD 官方 API（€99/月）
- 統一 PostgreSQL 為唯一 Source of Truth

---

## §6 實戰案例與洞察

### 案例 1：POWL（配電開關壟斷）

`[Doc#15a, #15b]`

**投資論點**：
- 美國配電開關市場 80% 佔有率
- 零負債 + 在手訂單 $1.4B（3 年產能排滿）
- 德州新廠產能翻倍（2026 Q2 投產）
- DSO 52 天（快速回款，質押首選）

**IV 計算**：
- 業主盈餘 7 年 CAGR: 18%
- 信心係數：1.3x（保守，因 EV 需求不確定）
- IV Range：$280-$450 vs 股價 $180（2026-01）
- 安全邊際：36%

**Jane 反面挑戰**：
- EV 滲透率低於預期 → 配電需求延後
- 德州廠爬坡不順 → CapEx 浪費
- Vertiv 競爭加劇 → 毛利率壓縮

**Allen 決策**：配置 15%（750 萬），Jane 首選通過。

---

### 案例 2：NVMI（半導體計量）

`[Doc#15a]`

**投資論點**：
- 2nm GAA 關鍵計量設備（ASML 合作夥伴）
- 以色列技術壁壘（40 年光學專利）
- TSMC + Samsung 雙驗證通過

**IV 計算**：
- 業主盈餘 7 年 CAGR: 25%
- 信心係數：1.2x（保守，地緣風險折減）
- IV Range：$210-$345 vs 股價 $150（2026-01）

**Jane 反面挑戰**：
- 以色列地緣衝突升級 → 產線中斷
- 2nm 良率低於預期 → 設備需求延後
- 單一客戶依賴（TSMC 50%+）

**Allen 決策**：配置 10%（500 萬），接受地緣風險。

---

### 案例 3：ESMC 德國廠監控

`[Doc#16]`

**觸發事件**：
- 中國對德貿易順差暴增 108%
- 德國預算違憲，補貼斷供風險
- 中國成熟製程產能過剩衝擊歐洲

**信心係數動態公式**：
```python
ESMC_Confidence = 0.3×能源價格指數 + 0.4×德國汽車出口指數 + 0.3×補貼狀態
```

**產業鏈連動分析**：
中國 EV 壟斷 → 德國車企衰退 → 車用晶片萎縮 → ESMC 空轉 → TSMC 財報負擔

**Allen 應對**：
- TSMC 信心係數從 1.5x 下調至 1.4x
- 增持 POWL（美國本土受益）
- 現金留 15% 反向狩獵

---

### 案例 4：關鍵材料戰略投資（待評估候選名單）

`[Doc#14]`

**原料悖論**：有礦 ≠ 有實力，權力在中游（加工、分離、精煉）

**中國壟斷現狀**：
- 98% 鎵加工
- 90% 稀土分離
- 90% 石墨陽極
- 80% 銻加工

**投資標的**：
- **一線龍頭**：Eaton (ETN), Quanta (PWR), Vertiv (VRT)
- **隱形冠軍**：Mueller (MLI), Sterling (STRL), Curtiss-Wright (CW)

**Allen 策略**：
- VRT 10%（數據中心液冷）
- BWXT 10%（核能小型反應爐）
- 質押比率監控（國防股波動大）

---

### 案例 5：[虛構] XYZ Corp — Stage 1 終止案例

**觸發事件**：
- 表面數據亮眼：連續 5 年營收 CAGR 25%，淨利看似穩定

**Integrity Gate 攔截**：
- CEO 過去 3 年承諾 4 項重大計畫，僅兌現 1 項（達成率 25%）
- 兩次財報重述（restatement）
- 內部人連續 6 季減持

**Jane 判決**：誠信門檻未通過 → **終止分析**，不進入 Stage 2
**Allen 教訓**：「數字再漂亮，管理層不可信就不值得花時間。」

---

## §7 Allen 知識系統整合

`[Doc#17b]`

**知識演進路徑**：
```
學習（Research） → 模仿（Template） → 創造（Innovation）
     ↓                 ↓                    ↓
  /note skill    Action Guide         Agent/Skill
     ↓                 ↓                    ↓
Research 目錄 → CLAUDE.md 規則 → Payload/Supabase → n8n 自動化
```

**Allen 現有知識系統架構**：`[2026-02 現況]`

| 系統 | 路徑 | 用途 |
|------|------|------|
| Obsidian Vault | `note/` + `research/` + `task/` | 一手知識根 + 蒸餾行動指南 + 任務追蹤 |
| Action Guide 系統 | `research/{topic}/action-guide.md` | 六維 DNA 品質蒸餾，讀一個檔案 = 80% 專家知識 |
| 三層記憶架構 | SCRATCHPAD + memory-index + Knowledge Graph | 工作記憶 + 路徑索引 + 動態實體關係 |
| Claude Code 規則 | `~/.claude/rules/` (8 files) | 全域行為 DNA（PDCA、安全、驗證、教訓） |
| Agent 定義 | `~/.claude/agents/` (jane, chi, codex, credential-guard) | 角色分工 + 專屬 DNA |
| Skills | `~/.claude/skills/` (≤12) | 可觸發的結構化工作流 |

IVCO 將在此基礎上擴展投資專用層（Supabase Fact/Understanding/Belief 記憶）。

**九維分析體系**（Allen 標準）：
- D1: 來源品質
- D2: 覆蓋完整性
- D3: 決策矩陣
- D4: 實戰案例
- D5: 風險盲點
- D6: 延伸探索
- D7: 競品對比
- D8: 過時檢查
- D9: 執行 Gap

**IVCO 中的應用**：
- Research 階段：21 篇文件 → /note 收集
- Action Guide 階段：蒸餾為 IVCO DNA（本文件）
- Agent 化階段：Jane Constitution + Chi CLI + 數據偵察功能（Chi + cron）

---

## §8 關鍵原則與禁忌

### 投資哲學層

**DO**：
- ✅ 追求模糊正確的 IV 區間（$280-$450）
- ✅ 質押生活費而非賣股（保留複利引擎）
- ✅ 管理層誠信對帳單（承諾 vs 兌現）
- ✅ 50% 大跌壓力測試（每次配置前必跑）
- ✅ 零負債企業優先（質押首選）
- ✅ 信心係數動態調整（季度定期 + 重大事件即時觸發）
- ✅ 管理層誠信追蹤操作紀律（承諾對帳單持續更新，達成率 < 100% 即降級 CC）

**DON'T**：
- ❌ 追求精準但錯誤的單一估值
- ❌ 賣股票換生活費（中斷複利）
- ❌ 盲信管理層（必須建對帳單追蹤）
- ❌ 忽略地緣風險（ESMC 德國廠教訓）
- ❌ 過度分散（核心持股 TSMC 可達 40-100%）

---

### 產品設計層

**DO**：
- ✅ 每日 Top 20 卡片流（Google Discover 風格）
- ✅ 用戶可覆寫每層數據（user_reasoning_oe / cagr / confidence）
- ✅ Jane 逆向挑戰強制產出（Anti-Sycophancy）
- ✅ 決策信號只有 BUY/HOLD/WAIT（無 SELL）
- ✅ 信心係數顏色編碼（🟢🟡🔴）

**DON'T**：
- ❌ 黑盒 AI（每層計算必須可查核）
- ❌ 虛假精確（顯示小數點後 4 位）
- ❌ 省略風險警告（Jane 核心段落不可刪）
- ❌ 推薦 SELL 信號（只提供 WAIT）
- ❌ 複雜 UI（極簡 > 功能豐富）

---

### 技術架構層

**DO**：
- ✅ CLI-First（Agent 原生工具鏈）
- ✅ 原子化工具（calc-oe / calc-cagr / check-mgmt 獨立）
- ✅ Gate 設計（check-mgmt 不過就攔截）
- ✅ 三層記憶隔離（Fact / Understanding / Belief）
- ✅ 讀寫分離（financial_reports vs company_metrics）

**DON'T**：
- ❌ MCP 優先（CLI > Browser，效率差 20 倍）
- ❌ 巨石工具（避免 all-in-one 黑盒）
- ❌ 跳過 Gate 檢查（管理層誠信不過 = 不計算 IV）
- ❌ LLM 直接 commit Belief（必須 Allen 審核）
- ❌ RLS 巢狀 Join（Supabase 效能殺手）

---

## 附錄：信心係數影響因子矩陣

`[Doc#3, #8, #16]`

以下因子矩陣作為 CC 定級時的參考框架。最終 CC 等級由§1 三層校正管線中的分級制決定。

| 因子類別 | 權重 | 正向觸發（+0.1~+0.3） | 負向觸發（-0.1~-0.3） |
|---------|------|---------------------|---------------------|
| **管理層誠信** | 30% | 承諾兌現率 >90% | 承諾跳票 >2 次 |
| **產業週期** | 25% | 產能擴張前夜（德州新廠） | 飽和期（成熟製程） |
| **技術壁壘** | 20% | 2nm GAA 獨家設備 | 同質化競爭 |
| **財務紀律** | 15% | 零負債 + DSO <60 | 負債率 >50% |
| **地緣政治** | 10% | 美國本土廠（POWL） | 地緣衝突區（NVMI 以色列） |

**實戰應用**：
- TSMC：1.4x（產業前夜 +0.2 / 台海風險 -0.1）
- POWL：1.3x（零負債 +0.15 / EV 不確定 -0.05）
- NVMI：1.2x（技術壁壘 +0.2 / 地緣風險 -0.2）

---

## 結語：IVCO 的終極目標

> Allen 在 2026-01-31 創建 IVCO 時的願景：

**短期（6 個月）**：
建立 Top 20 每日卡片流，成為價值投資者的 Google Discover。

**中期（3-5 年）**：
信心係數框架成為全球價值投資社群的新標準（如 Buffett 的 Moat、Graham 的 Safety Margin）。

**長期（3-5 年）**：
IVCO 從工具升級為**價值投資作業系統**（Agentic OS for Value Investing），Allen 成為 AI 時代結合四大師智慧的價值投資實踐者。

---

**核心信念**：
- 概略正確 > 精準錯誤
- 長期複利 > 短期波動
- 業主心態 > 交易思維
- 逆向挑戰 > 確認偏誤
- 信心係數 > 黑盒 AI

**Allen 的話**：`[Doc#1]`
> 「買股票就是買公司的一部分。如果你不願意持有 10 年，那就不要持有 10 分鐘。」

---

**DNA 版本**：v1.1
**審閱修訂日期**：2026-02-13（Allen 全面確認，採用 Jane 建議值）
**初版蒸餾日期**：2026-02-12
**來源文件**：21 篇研究（T01-T17b，~1.3MB）
**維護者**：Jane + Chi
**終裁者**：Allen
