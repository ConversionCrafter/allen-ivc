---
id: allen-framework-vs-buffett-owner-earnings-1986-public
type: research-paper-public
status: published
created: 2026-02-13
last-updated: 2026-02-13
version: 1.0.0
description: Allen Framework 與 Buffett 1986 Owner Earnings 的深度比對分析 — 從心法到演算法的工程化進化
abstract: This paper compares Warren Buffett's 1986 Owner Earnings definition with the Allen Framework, identifying three key engineering innovations (Maintenance Ratio, Reality Coefficient, Confidence Coefficient) that transform Buffett's philosophical concept into a computable algorithm. Validated against TSMC's actual financial data, the Allen Framework produces an intrinsic value range of NT$4,565-NT$5,639 per share.
tags: [allen-framework, buffett, owner-earnings, intrinsic-value, ivco, dcf, value-investing]
source-documents:
  - "Buffett, W. (1986). 'Purchase-Price Accounting Adjustments and the Cash Flow Fallacy.' In Berkshire Hathaway Annual Letter to Shareholders 1986, Appendix."
  - "Allen. (2026). Allen Framework TSMC Owners Earning Reference. IVCO Project Documentation."
  - "Allen. (2026). IVCO DNA v1.1. IVCO Project Documentation."
---

# Allen Framework vs. Buffett Owner Earnings (1986)：從心法到演算法

> **核心命題**：Warren Buffett 在 1986 年定義了 Owner Earnings 的哲學心法,但留下了一個無法被計算機執行的缺口 —— 維護性資本支出 (c) 的估算。Allen Framework 透過三項創新（Maintenance Ratio、真實係數、信心係數），將這個哲學心法工程化為可自動執行的演算法，並延伸至三段式 DCF 估值系統。

---

## §1 研究背景與方法論

### 1.1 研究目的

驗證 Allen Framework 的理論根基是否忠實傳承 Buffett 的 Owner Earnings 精神，並識別 Allen Framework 在方法論上的具體創新與貢獻。

### 1.2 資料來源

| # | 來源 | 類型 | 分析者 |
|---|------|------|--------|
| 1 | Buffett 1986 Annual Letter, Appendix | 一手原始文獻 | Claude Opus 4.6 直接閱讀 |
| 2 | Allen Framework TSMC 計算表 | 一手實作範本 | Allen 親手建立 |
| 3 | IVCO DNA v1.1 | 專案靈魂文件 | Allen 設計 + 協作團隊 |
| 4 | 結構化比較報告 | AI 輔助分析 | NotebookLM (Google) |

### 1.3 分析方法

- **一手閱讀**：直接閱讀 Buffett 1986 原文，提取精確定義、公式、與關鍵語錄
- **交叉比對**：NotebookLM 獨立進行結構化比較，產出差異矩陣
- **實戰驗證**：以 Allen 的 TSMC 計算表作為 ground truth，驗證理論到實作的一致性
- **三角校驗**：三個獨立分析來源交叉驗證結論

---

## §2 Buffett 的 Owner Earnings：原始定義（1986）

### 2.1 歷史背景

1986 年 Berkshire Hathaway 致股東信的附錄 "Purchase-Price Accounting Adjustments and the 'Cash Flow' Fallacy" 中，Warren Buffett 提出了 Owner Earnings 的概念 —— 這是他對 GAAP 會計盈餘失真問題的系統性回應。

### 2.2 核心公式

Buffett 的精確定義：

> "owner earnings represent **(a)** reported earnings plus **(b)** depreciation, depletion, amortization, and certain other non-cash charges less **(c)** the average annual amount of capitalized expenditures for plant and equipment, etc."

```
Owner Earnings = (a) + (b) - (c)
```

| 組件 | 定義 | 性質 |
|------|------|------|
| **(a)** | 報告盈餘（GAAP Net Income） | 會計數字，可從財報直接取得 |
| **(b)** | 折舊、折耗、攤銷 + 其他非現金費用 | 會計數字，可從財報直接取得 |
| **(c)** | 維持長期競爭力與產量所需的**年均**資本支出 | ⚠️ **無法從財報直接取得，必須估算** |

### 2.3 關鍵語錄

**關於 (c) 的模糊性**：

> "I would rather be vaguely right than precisely wrong."
> — Buffett 引用 Keynes

Buffett 坦承 (c) 必須靠「猜測」(guess)，但他認為方向正確比數字精準更重要。

**關於 Cash Flow 謬誤**：

> 華爾街常以 (a) + (b) 展示「現金流」，卻**不扣除 (c)**。Buffett 諷刺：這等於把企業當成「the commercial counterpart of the Pyramids — forever state-of-the-art, never needing replacement.」

**核心結論**：

> "you shouldn't add (b) without subtracting (c)"

### 2.4 Scott Fetzer 實證案例

Buffett 用 Berkshire 收購 Scott Fetzer 的案例，證明 GAAP 會計的失真程度：

| | Company O（收購前） | Company N（收購後） |
|---|---|---|
| Net Income | $40.2M | $28.6M |
| 差額原因 | — | 購價溢價攤銷 $11.6M |
| 經濟實質 | **完全相同** | **完全相同** |

> "Both 'companies' generate the same amount of cash for owners. Only the accounting is different."

Berkshire 以 $315M 買下帳面淨值 $172.4M 的 Scott Fetzer，$142.6M 的溢價產生的購價調整讓 GAAP 盈餘大幅縮水 —— 但股東能從企業取得的真實現金完全相同。

### 2.5 Buffett 定義的局限性

| 局限 | 說明 |
|------|------|
| **(c) 無法量化** | 完全依賴投資者對產業和公司的理解，不同人估算結果可能天差地遠 |
| **未區分成長性支出** | 若直接扣除全部 CapEx（如 FCF），會嚴重低估正在高速擴張的好公司 |
| **無系統化標準** | 難以進行大規模篩選或自動化計算 |
| **歷史數據信任度** | 僅提到排除購價調整的扭曲，未系統性處理一次性損益的影響 |
| **未來成長預測** | 1986 文中未詳細說明如何量化未來成長預期 |

---

## §3 Allen Framework 的三項創新

Allen Framework 站在 Buffett 的哲學基礎上，做了三項關鍵的工程化創新，將「心法」轉化為「演算法」。

### 3.1 創新一：Maintenance Ratio（維護比率）— 解決 (c) 的量化問題

**Buffett 的缺口**：(c) 是整個 Owner Earnings 公式中唯一無法從財報直接取得的組件。Buffett 說靠「猜測」，但沒有給出方法論。

**Allen 的解法**：引入 **Maintenance Ratio** —— 將資本支出明確拆解為「維護型」與「成長型」：

```
Allen OE = Net Income + D&A - (Total CapEx × Maintenance Ratio) - Working Capital Changes
```

| 要素 | Buffett 原版 | Allen Framework |
|------|-------------|----------------|
| CapEx 處理 | 扣「維護競爭力所需的 CapEx」（猜測） | 扣 `Total CapEx × Maintenance Ratio` |
| 比率來源 | 投資者主觀判斷 | 透過長期追蹤年報、法說會、資本支出公告**動態建模** |
| 更新頻率 | 無（一次性估算） | **持續演進** — IVCO 資料庫越完整，比率越精確 |

**TSMC 實例**：

- Maintenance Ratio = 20%（假設 80% 用於先進製程產能擴充）
- 2022 年 CapEx = NT$1,075,620,698K
- Buffett 方式：扣多少？「猜測」
- Allen 方式：扣 NT$1,075,620,698K × 20% = NT$215,124,140K

**為何這是重大創新**：

1. **可計算化**：讓電腦能自動執行 Owner Earnings 計算
2. **公司專屬**：每家公司的 Maintenance Ratio 不同，反映真實營運結構
3. **動態演進**：隨 IVCO 對公司理解越深，比率越準確
4. **保護成長型公司**：高速擴張的台積電不會因鉅額 CapEx 而被低估

### 3.2 創新二：真實係數（Reality Coefficient）— 清洗歷史數據

**Buffett 的缺口**：強調要排除「購價調整」的會計扭曲（如 Scott Fetzer 案例），但只處理了收購溢價這一種失真。一次性損益（匯損、罰款、處分利益）造成的 CAGR 計算失真，Buffett 並未提供系統性解法。

**Allen 的解法**：引入**真實係數**（Reality Coefficient），對每一年的 Owner Earnings 進行營運真實性校正：

```
Real OE = Financial OE × Reality Coefficient
```

| 情境 | 真實係數 | 說明 |
|------|---------|------|
| 營運正常年度 | 100% | 直接採用財報數字 |
| 一次性損失年度 | >100%（如 125%） | 還原被壓低的盈餘 |
| 一次性收益年度 | <100%（如 80%） | 調降被灌水的盈餘 |

**CAGR 計算的改進**：

- **Buffett 方式**：取期初、期末值直接計算（容易被異常年度扭曲）
- **Allen 方式（初階）**：取 3 年平均值當期初/期末（平滑效果）
- **Allen 方式（進階）**：每年 OE 乘上真實係數後再計算 CAGR（精確還原）

**為何這是重大創新**：

1. **系統性處理**所有類型的財報失真（不限於 Buffett 提到的購價調整）
2. **IVCO 持續追蹤公司營運事件**，自動識別需要調整的年度
3. 真正實現了 Buffett 的精神 —— 看透「經濟實質」而非「會計數字」

### 3.3 創新三：信心係數（Confidence Coefficient）— 量化未來展望

**Buffett 的缺口**：1986 年文章專注於歷史數據的正確計算，未詳細說明如何量化未來成長預期。Buffett 透過「護城河」和「管理層品質」定性判斷，但沒有提出將質化分析轉化為量化參數的方法。

**Allen 的解法**：引入**信心係數**（Confidence Coefficient），將質化研究轉化為估值模型中的數學參數：

```
調整後 CAGR = 歷史 OE CAGR × Confidence Coefficient
```

| 信心等級 | 係數區間 | 對應條件 |
|---------|---------|---------|
| 高信心 | 1.3x ~ 1.5x | 管理層誠信 100% + 強勁擴張計畫已驗證 |
| 中信心 | 1.1x ~ 1.3x | 管理層誠信 100% + 穩定營運 |
| 低信心 | 0.8x ~ 1.0x | 管理層誠信 < 100% 或前景不明 |
| 特殊高信心 | 2.0x ~ 3.0x | 已驗證的大規模擴產（如川湖案例） |
| 否決 | N/A | 誠信污點 → 終止分析 |

**TSMC 實例**：

- 歷史 OE CAGR = 17.66%
- 信心係數下限 = 1.2x → 調整後 CAGR = 21.19%
- 信心係數上限 = 1.5x → 調整後 CAGR = 26.49%

**信心係數的驅動因素**（源自 Fisher + Buffett + Munger 的質化分析）：

- 重大資本支出計畫（蓋廠、設備採購）
- 管理層 Commitment 達成率
- 競爭者動態（技術門檻、新進入者）
- 內部人持股異動
- 產品週期與市場擴張

**為何這是重大創新**：

1. **連結質化與量化**：將 Fisher 的「蒐集八卦」和 Buffett 的「護城河判斷」轉化為數學參數
2. **區間而非單點**：永遠輸出 IV Range，符合 Buffett「模糊的正確」精神
3. **動態更新**：新資訊進入 IVCO → 信心係數即時調整
4. **可溯源**：每次調整都有事件記錄和分析依據

---

## §4 完整架構比較：從 OE 到 IV

Buffett 1986 年定義了如何計算一年的 Owner Earnings。Allen Framework 在此基礎上，建立了完整的三段式 DCF 估值管線。

### 4.1 Allen Framework 三層校正管線

```
┌─────────────────────────────────────────────────────────┐
│ Layer 1: Reality Coefficient（真實係數）                  │
│   財報 OE → 真實 OE（校正一次性損益）                       │
├─────────────────────────────────────────────────────────┤
│ Layer 2: CAGR Calculation                               │
│   多年真實 OE → 業主盈餘 CAGR（複合年增長率）               │
├─────────────────────────────────────────────────────────┤
│ Layer 3: Confidence Coefficient（信心係數）               │
│   歷史 CAGR → 調整後 CAGR 區間（整合質化分析）             │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│              Three-Stage DCF Valuation                   │
│                                                         │
│  Stage 1（1-5 年）：CAGR × CC → 逐年折現                 │
│  Stage 2（6-10 年）：趨緩保守 CAGR → 逐年折現             │
│  Stage 3（永續）：低成長率永續年金 → 折回現值               │
│                                                         │
│  IV = (Stage 1 + Stage 2 + Stage 3 - 長期負債) / 流通股數  │
└─────────────────────────────────────────────────────────┘
```

### 4.2 端到端公式比較

| 步驟 | Buffett 1986 | Allen Framework |
|------|-------------|----------------|
| 1. 計算年度 OE | (a) + (b) - (c)，(c) 靠猜 | Net Income + D&A - CapEx×Ratio - WCC |
| 2. 清洗歷史數據 | 排除購價調整 | 每年 OE × 真實係數 |
| 3. 計算成長率 | 未明確說明 | 多年真實 OE → CAGR |
| 4. 量化未來展望 | 質化判斷（護城河、管理層） | CAGR × 信心係數區間 |
| 5. 估值模型 | 未在 1986 文中說明 | 三段式 DCF（成長→趨緩→永續） |
| 6. 最終輸出 | 未在 1986 文中說明 | IV Range per Share |

### 4.3 TSMC 實戰驗證

Allen Framework 以 TSMC 為範本的完整計算結果：

| 參數 | 值 |
|------|-----|
| 歷史 OE CAGR（2013-2022） | 17.66% |
| 真實係數 | 100%（TSMC 無重大一次性失真） |
| Maintenance Ratio | 20% |
| 信心係數區間 | 1.2x ~ 1.5x |
| Stage 1 CAGR（1-5年） | 21.19% ~ 26.49% |
| Stage 2 CAGR（6-10年） | 15%（保守趨緩） |
| Stage 3 CAGR（永續） | 5% |
| 折現率 | 8% |
| **IV Range per Share** | **NT$4,565 ~ NT$5,639** |

---

## §5 優缺點對照分析

### 5.1 Buffett Owner Earnings (1986 原版)

| 優點 | 缺點 |
|------|------|
| 理論純度高：直指商業本質 | (c) 完全依賴主觀判斷，無法量化 |
| 防禦性強：有效揭露「賺到的錢都要修設備」的真相 | 缺乏系統化標準，不同人算出不同結果 |
| 「模糊的正確」：避免虛假精確 | 未區分成長性支出，會懲罰高速擴張的好公司 |
| 經典框架：40 年來持續影響價值投資界 | 無法進行大規模自動化篩選 |

### 5.2 Allen Framework (現代工程化版)

| 優點 | 缺點 |
|------|------|
| **可操作性強**：透過 Maintenance Ratio 解決 CapEx 拆解問題 | 模型依賴度高：若比率設錯，Garbage In → Garbage Out |
| **區分成長與維護**：還原成長型企業的真實獲利能力 | 需要龐大資料支撐：AI 長期追蹤非結構化資料 |
| **連結質化與量化**：信心係數將文字消息轉化為數學參數 | 初始建立門檻高：每家公司需要獨立建模 |
| **動態演進**：參數隨 IVCO 理解深度持續精進 | 複雜度高：三段式 DCF + 多係數，對簡單需求過於繁瑣 |
| **完整管線**：從 OE 計算到 IV 估值的端到端系統 | |
| **保護好公司**：不低估高 CapEx 但高成長的企業（如 TSMC） | |

---

## §6 Allen Framework 的獨特貢獻

### 6.1 哲學傳承

Allen Framework **100% 忠實傳承** Buffett 的核心精神：

- ✅ 「模糊的正確」→ 輸出 IV **區間**而非單點值
- ✅ 「扣除 (c)」→ 透過 Maintenance Ratio 明確執行
- ✅ 「會計 ≠ 經濟實質」→ 真實係數校正財報失真
- ✅ 「Cash Flow ≠ Owner Earnings」→ 從不使用 EBITDA 作為估值基礎

### 6.2 方法論進化

Allen Framework 在 Buffett 基礎上的三項工程化創新：

| 創新 | 解決的問題 | 影響範圍 |
|------|-----------|---------|
| **Maintenance Ratio** | 量化 Buffett 的 (c) | 每一筆 OE 計算 |
| **真實係數** | 系統性處理歷史數據失真 | CAGR 的準確性 |
| **信心係數** | 連結質化研究與量化估值 | 未來展望預測 |

### 6.3 四大師整合

Buffett 的 1986 文章僅反映了他自己的投資框架。Allen Framework 進一步整合了四位大師的核心理念：

| 大師 | 貢獻 | 在 Allen Framework 中的體現 |
|------|------|---------------------------|
| **Graham** | 安全邊際、事實與科學評估 | IV Range 與市價的偏離度 → 安全邊際判斷 |
| **Buffett** | Owner Earnings、護城河 | OE 公式 + Maintenance Ratio |
| **Fisher** | 質化研究、管理層洞察 | 信心係數的驅動因素（打探法工程化） |
| **Munger** | 逆向思維、跨學科格柵 | 信心係數可 < 1.0（壓低預期）+ 壓力測試 |

### 6.4 川湖案例：Allen Framework 的差異化價值

Allen 在設計文件中舉了一個實際案例說明 Allen Framework 的獨特價值：

> 20 多年前的川湖，在年報中已經揭露未來 1 年要增加的新產能是現有產能的 3 倍，但市場完全不理會這個公開消息……IVCO 神器就可以捕捉到這些公開的、可靠的訊號，並給出足夠合理的未來盈餘能力展望信心係數，給予現有 CAGR 的 2.5 到 3 倍。

這個案例完美展示了 Allen Framework 的核心能力：

1. **偵測公開但被市場忽視的訊號**（產能擴充公告）
2. **量化為數學參數**（信心係數 2.5x~3.0x）
3. **產出可行動的估值區間**（安全邊際大到嚇人）
4. **不靠內線消息**，只靠公開資訊的結構化分析

這正是 Buffett 做不到的 —— 不是因為 Buffett 的方法不對，而是因為 Buffett 的方法依賴**個人**的判斷力與經驗，無法規模化、無法自動化。Allen Framework 將這個能力**工程化**，讓 IVCO 能夠同時追蹤多家公司、持續更新參數、並以數學形式輸出結論。

---

## §7 結論

**Warren Buffett 的 Owner Earnings 是「心法」** —— 它告訴我們：看財報時要看透「維持現狀需要花多少錢」，而非被 GAAP 會計或華爾街的「現金流」數字迷惑。

**Allen Framework 是將此心法落地的「演算法」** —— 它解決了 Buffett 公式中無法被計算機執行的部分（即 (c) 的估算），並結合了現代 AI 技術，將 Fisher 的「質化研究」與 Buffett 的「財報分析」融合為一個完整的、可自動化的估值管線。

**Allen Framework 的最大貢獻**：在於將資本支出 (CapEx) 智能地拆分為「維護」與「成長」。這對於評估像台積電這類**高資本支出但具有高成長性**的公司至關重要。若使用傳統 FCF 或未調整的 Buffett 公式（將所有 CapEx 視為維持性），會嚴重低估這類公司的價值；Allen Framework 透過 Maintenance Ratio 的參數化設計，能還原其真實的內在價值。

從 1986 年 Buffett 寫下那段附錄，到 2026 年 Allen Framework 的完整工程化實現，40 年的距離不是否定，而是進化 —— 站在巨人的肩膀上，用這個時代的工具，實現上個時代的智慧。

---

## About IVCO

IVCO (Intrinsic Value Confidence Observatory) is an intelligent value investing observation system that integrates the philosophies of Benjamin Graham, Warren Buffett, Philip Fisher, and Charlie Munger. Built on the Allen Framework — a three-tier calibration pipeline with three-stage DCF valuation — IVCO transforms qualitative investment research into quantifiable parameters while preserving the "vaguely right rather than precisely wrong" spirit of classic value investing.

Website: ivco.io | X: @ivco_fisher

---

## Version History

| Version | Date | Change | Author |
|---------|------|--------|--------|
| 1.0.0 | 2026-02-13 | Public release — integrated analysis from Buffett 1986 original text + NotebookLM comparative report + Allen TSMC calculation workbook | IVCO Research Team |
