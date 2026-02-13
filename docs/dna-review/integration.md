---
id: dna-review-integration
type: allen-response-guide
status: decisions-confirmed-2026-02-13
created: 2026-02-12
description: 53 個審閱項目收斂為 8 個根決策 — Allen 回答這 8 題即可解決全部矛盾
---

# IVCO DNA 審閱：Allen 回覆指南

> **使用方法**：每個決策下方有 `Allen 回覆：` 區塊，直接填入答案即可。
> 回答完 8 個根決策 = 解決 32 個質疑項 + 21 個矛盾項的 80%+。
> 剩餘零散項目在最後「快速確認清單」中以 Yes/No 回覆。

---

## 決策 1：IV 計算公式 🔴 CRITICAL

**涉及項目**：Q-A1, Q-B1, Q-B2, Q-B3, C-E3（5 項）

**現狀矛盾**：DNA 三處公式互相矛盾，台積電案例無法驗算。

| 位置 | 公式 | 問題 |
|------|------|------|
| §1 L35 | IV = OE (Historical CAGR) × Confidence | OE 和 CAGR 用括號並列，無法解析 |
| §2 L194 | IV_Low = OE × CAGR × Confidence_Low | 三項相乘維度錯誤（$/股 × % × 倍數 ≠ $/股）|
| CLAUDE.md L32 | IV = Historical OE CAGR × Confidence | 省略 OE 本身，輸出是成長率而非價值 |

**台積電驗算失敗**：OE $88.51 × CAGR 15% × Confidence 1.4x = NT$18.6（實際 IV Range NT$4,500-6,200）

### ✅ Allen 回覆（2026-02-12，修正 2026-02-13）

**方法：三段式 DCF + 信心係數修正 CAGR**

> 參考 Allen 實際計算：`inbox/TSMC 台積電 Owners_earning.md`（TSMC 三段式完整算法）

```
IV = Three-Stage DCF - Long_Term_Debt

Stage 1（高信心期，1-5 年）：
  OE_t = OE_base × (1 + CAGR_adjusted)^t
  CAGR_adjusted = Historical_OE_CAGR × Confidence_Coefficient
  （TSMC 範例：17.66% × 1.2 = 21.19% ~ 17.66% × 1.5 = 26.49%）

Stage 2（成長趨緩期，6-10 年）：
  OE_t = OE_5 × (1 + CAGR_moderate)^(t-5)
  CAGR_moderate = 固定保守成長率（TSMC 範例：15%）
  （假設：成長會趨緩但仍會成長）

Stage 3（永續成長期，Year 11+）：
  Terminal_Value = OE_10 × (1 + g_perpetual) / (r - g_perpetual)
  g_perpetual = 永續成長率（TSMC 範例：5%）

折現率 r = 8%（TSMC 範例；概念上 ≈ US 10yr + 風險溢價）

IV_per_share = (PV_Stage1 + PV_Stage2 + PV_Terminal - Long_Term_Debt) / 流通股數

IV Range：
  IV_Low = 用 Confidence_Low 計算（TSMC：NT$4,629）
  IV_High = 用 Confidence_High 計算（TSMC：NT$5,703）
```

**CAGR 計算（兩階段演進）**：
- **V0 防失真平滑法**：期初值 = 前 3 年平均 OE，期末值 = 近 3 年平均 OE → 防一次性損益失真
- **V1+ 真實盈餘能力反應指數**：每年 OE × 反應指數（如一次性損失年 → 120%）→ 還原真實盈餘能力後再算 CAGR

**信心係數的本質（Allen 原話精華）**：
- 乘在 **CAGR** 上，不是 OE 或 IV
- 範圍無固定上下限：競爭威脅 → 0.8x，川湖產能 3 倍擴張 → 2.5-3.0x
- 來源：透過徹底了解一家公司（Fisher 打探法 + Buffett 20 年年報研讀），判斷公開資訊對未來盈餘能力的影響
- **動態調整**：重大資本支出 / 裁員 / 換 CEO / 併購 / 新產品 / 專利訴訟 / 競爭者動態 / 內部人持股異動 → 隨時修正
- IVCO 的核心價值：用工具持續監控公開資訊 → 即時調整信心係數 → 即時更新 IV Range

**篩選門檻**：無法投射未來 5 年的公司 = 不值得分析。「弱水三千只取一瓢飲」

**TSMC 驗算**：✅ 2026-02-13 完成。三輪反覆校正後公式與數值完全一致：
- P = M - N → 118,363,999,450（低）/ 146,215,633,369（高）
- Q = P / O × 10 → **NT$4,565（低）/ NT$5,639（高）**
- 參考文件已同步更新：`Obsidian/projects/ivco/allen-framework-tsmc-owners-earning.md`

**安全邊際公式**：待 Allen 確認（IV_Low 或 IV_Mid 基準）。

**DNA 修訂方向**：✅ 2026-02-13 完成。§1 核心公式、§2 Stage 3 計算、TSMC 案例數據、CLAUDE.md Core Formula 全部更新為三段式 DCF。

**關鍵學習**：反覆回問 → 修正 → 再確認的過程，同時提升了理解深度和參考文件精確度。每家公司 6 個可調參數（維護 CapEx 比率、CC 上下限、Stage 2 CAGR、Stage 3 CAGR、折現率、長期負債）全部公司專屬且動態演進。

---

## 決策 2：四大師人選 🔴 CRITICAL

**涉及項目**：C-A1, C-B3, C-D1, C-E1, Q-E5（5 項）

**現狀矛盾**：

| 位置 | 四大師 |
|------|--------|
| DNA 標題 L14 | Buffett, Munger, **Lynch**, Fisher |
| §1 表格 L62-67 | **Graham**, Buffett, Fisher, Munger |
| CLAUDE.md L3 | **Graham**, Buffett, Fisher, Munger |
| 結語 L840, L843 | 提到 **Lynch** 的 PEG，比喻 Allen 為 Lynch |

Graham（Deep Value + 安全邊際）和 Lynch（Growth at Reasonable Price + PEG）風格差異大。

### ✅ Allen 回覆（2026-02-12）

**選擇 (A)：Graham / Buffett / Fisher / Munger**

Lynch 在標題和結語中移除。§1 四大師表格和 CLAUDE.md 已正確，無需修改。

**DNA 修訂方向**：
- L14 標題：「Lynch」→「Graham」
- L840 結語：移除「Lynch 的 PEG」參考
- L843 結語：移除「Peter Lynch」比喻，改為更貼切的表述

---

## 決策 3：信心係數體系 🟠 HIGH

**涉及項目**：Q-A2, C-A2, C-B1, C-B2, Q-E3, Q-E4, M-A1, C-E3（8 項）

**現狀矛盾**：信心係數在四個位置有不同定義。

| 位置 | 範圍 | 特點 |
|------|------|------|
| §1 L45-46 | 1.2x ~ 1.8x | 無懲罰區間（< 1.2x） |
| §2 L194-195 | Low 固定 1.2x, High 1.4x-1.8x | Low/High 分離 |
| CLAUDE.md L354-359 | 0.8x ~ 1.5x | 有懲罰區間（誠信 < 100% → 0.8x-1.0x）|
| 附錄 L817-823 | 五類因子權重矩陣 | 無基線值 |

**Allen 需要回答 4 個子問題**：

(3a) 信心係數的**完整範圍**是多少？是否存在 < 1.0x 的懲罰區間？

```
Allen 回覆：


```

(3b) Low 和 High 如何從單一係數產生？（如 NVMI 1.2x → IV Range $210-$345，範圍從何而來？）

```
Allen 回覆：


```

(3c) 附錄五類因子（管理層 30% / 產業 25% / 技術 20% / 財務 15% / 地緣 10%）的**基線值**是多少？（如：基線 1.0x，五因子加總決定最終值？）

### ✅ Allen 回覆（2026-02-13）

**(A) 保留作為 CC 定級時的參考框架**。五因子矩陣不取代§1的 CC 分級制（保守/穩健/積極/極端），而是在決定 CC 等級時的評估維度參考。最終 CC 等級由分級制決定。

(3d) TSMC 信心係數的實際推導過程？（附錄說「產業前夜 +0.2 / 台海風險 -0.1 = 1.4x」，但基線是多少？）

### ✅ Allen 回覆（2026-02-13）

已在 Allen Framework 文件中完整展示。TSMC CC = 1.2x ~ 1.5x（2nm 量產前夜 + 零負債 + 台海風險折減）。推導過程參考 `allen-framework-tsmc-owners-earning.md`。

---

## 決策 4：Phase 結構統一 🟠 HIGH

**涉及項目**：C-D2, C-D5, Q-D4, Q-D5, C-C4（5 項）

**現狀矛盾**：

| DNA §5 四階段 | CLAUDE.md 五階段 |
|--------------|-----------------|
| Phase 1: Foundation（Blog + CMS + MCP） | Phase 1: Payload CMS Collections |
| Phase 2: Automation（CLI + n8n） | Phase 2: Python CLI |
| Phase 3: Intelligence **或** n8n Content Pipeline（內部矛盾） | Phase 3: n8n |
| Phase 4: Scale（API + 社群 + Enterprise） | Phase 4: Playground 前端 |
| — | Phase 5: Qdrant |

**DNA Phase 3 內部矛盾**：總覽說 AI Intelligence，詳細段落說 SEO Content Pipeline — 完全不同的工作。

**Allen 選擇**：

- (A) 以 **CLAUDE.md 5 階段**為準（已在開發中使用），DNA 對齊
- (B) 以 **DNA 4 階段**為準，CLAUDE.md 對齊
- (C) 重新設計統一版本

DNA Phase 3 的 Intelligence vs Content Pipeline 哪個是正確內容？還是要拆分？

### ✅ Allen 回覆（2026-02-13）

**(A) 以 CLAUDE.md 5 階段為準，DNA 對齊。** Intelligence 是 Phase 3 願景，Content Pipeline（SEO）是其中元件。5 階段：Foundation → CLI → Automation+Intelligence → Frontend → Scale+Qdrant。

---

## 決策 5：MVP 範圍與過度工程 🟡 MEDIUM

**涉及項目**：Q-A3, Q-B5, Q-C1, Q-C2, Q-C8, Q-D7（6 項）

**核心問題**：DNA 描繪了完整願景，但對 solo founder + AI agents 過於龐大。以下功能在 V0 是否需要？

| 功能 | DNA 描述 | 建議 | Allen 決定（V0必要/V1/V2/不做）|
|------|---------|------|------|
| 選股漏斗 10,000 → Top 20 | §1 三層篩選 | V0 先做 Allen 已知的 30 家 | |
| 每日 Top 20 卡片流 | §2 L167 | 需要完整自動化，V0 不現實 | |
| CLI 命令列入口 | §3 CLI-First | CLI 當內部 API，Allen 入口是 Web UI | |
| 七層 Schema | §3 IVC_Analysis | V0 只做 BASE + OUTPUT | |
| Vector DB 年報語意搜尋 | §3 pgvector | 20 家公司用 grep 夠了 | |
| Mission Control 10 Agent | §4 L518 | 遠超目前 3 agent 架構 | |

### ✅ Allen 回覆（2026-02-13，全部採用建議值）

```
選股漏斗：V0 先做 Allen 已知 30 家
每日 Top 20：V1
CLI 入口：V0 作為內部 API
七層 Schema：V0 只做 BASE + OUTPUT
Vector DB：V2
Mission Control：V2
```

**V0 入口**：**(A) Payload CMS Dashboard + Jane 對話**

---

## 決策 6：Agent 角色現實化 🟡 MEDIUM

**涉及項目**：Q-D1, Q-D2, Q-D3, C-D4, M-D1, M-D2（6 項）

### ✅ Allen 回覆（2026-02-13，全部採用建議值）

**(6a) Data Hunter → (D)** 移除獨立 agent，由 Chi + launchd cron 承擔。保留功能描述，歸屬於 Chi。

**(6b) Codex → Yes**，更新為 active。rules/08 已生效，DNA 同步。

**(6c) Jane Skills → (C)** 融入 Jane DNA（`agents/jane.md`），不建為獨立 skills 檔案。6+2 為概念設計框架。

---

## 決策 7：技術設計邊界 🟡 MEDIUM

**涉及項目**：Q-C3, Q-C4, Q-C5, Q-C6, Q-C7（5 項）

### ✅ Allen 回覆（2026-02-13，全部採用建議值）

**(7a) ImpactAssessment → (A) 提案制**。Jane 建議 → Allen 批准 → 才寫入 DB。AI 不可自動修改 Belief Memory。

**(7b) IVCO 三層記憶 → (A) 獨立系統在 Supabase 內**。與 Allen 全域 Memory v2.0 分離，各自演進。

**(7c) SEC EDGAR + 新聞自動標籤 → Future（非 V0）**。Phase 2+ 再導入。

---

## 決策 8：商業化節奏 🟢 LOW

**涉及項目**：Q-D6, M-E6, M-D4, Q-B4（4 項）

### ✅ Allen 回覆（2026-02-13，全部採用建議值）

**(8a)** Private tool first。先建 Allen 私用工具，驗證投資決策品質後再逐步 SaaS 化。

**(8b)** ✅ 已完成。DNA §2 已改為 "IVCO"（2026-02-13 全面改名時一併處理）。

---

## 快速確認清單

> 以下項目不需要長回覆，Yes/No 或一句話即可。

| # | 項目 | 預設建議 | Allen 確認 |
|---|------|---------|-----------|
| 1 | Live in Loans 壓力測試改為「組合層級」計算？(Q-A4) | Yes | ✅ Yes |
| 2 | 「川湖漢唐」補充一句背景說明？(Q-A5) | Yes | ✅ Yes |
| 3 | 現金 15% 用途是什麼？(Q-A6) | 應急+等待買點 | ✅ 應急+等待買點 |
| 4 | QQQ 在「3-5 家」規則中算幾家？(C-A4) | 不計入 | ✅ 不計入 |
| 5 | OE 公式是否包含 Working Capital Changes？(M-B1) | Yes（CLAUDE.md 已含） | ✅ Yes |
| 6 | 信心係數校準頻率？(M-E5) | 季度+事件觸發 | ✅ 季度+事件觸發 |
| 7 | §6 案例 4 是待評估候選名單還是完整分析？(Q-B6) | 待評估 | ✅ 待評估 |
| 8 | §6 是否補充一個「Stage 1 未通過而終止」的案例？(M-B5) | Yes | ✅ Yes |
| 9 | §8 原則層是否補充「信心係數動態調整」「管理層誠信追蹤操作紀律」？(Q-E4, M-E3) | Yes | ✅ Yes |
| 10 | Jane 報告格式以 CLAUDE.md 六段版（risk-first）為準？(C-D3) | Yes | ✅ Yes |
| 11 | Jane Constitution 版本是否正式維護？(Q-D2) | 概念記錄即可 | ✅ 概念記錄即可 |
| 12 | 結語中期目標「1-2 年成為新標準」是否調整為「3-5 年」？(C-E4) | Yes | ✅ Yes |
| 13 | §7 是否補充 Allen 現有知識系統架構描述？(Q-E1) | Yes（簡述即可）| ✅ Yes |

---

## 解決統計

| 類型 | 總數 | 此指南覆蓋 | 殘留 |
|------|------|-----------|------|
| ❓ 質疑項 | 32 | 29（8 決策 + 快速清單） | 3（細節在 DNA 修訂時處理）|
| ⚠️ 矛盾項 | 21 | 19（8 決策覆蓋） | 2（輕度，自動修正）|
| 🔲 遺漏項 | 27 | 13（快速清單 + 決策附帶） | 14（建議項，DNA 修訂時自動補充）|
| **合計** | 80 | **61（76%）** | 19（自動處理） |

---

## 下一步

1. ✅ Allen 回覆 8 個根決策 + 13 個快速確認（2026-02-13 全部確認）
2. 🔄 Chi (Opus) 執行 DNA v1.1 修訂中
3. 🔄 Codex (ChatGPT 5.2) 一致性審查完成
4. ⬜ Allen 最終確認 → DNA v1.1 完成 → 進入 Brainstorming
