---
chunk: B
section: §2 產品定義 + §6 實戰案例
lines: L145-234, L629-725
reviewer: Jane
status: complete
date: 2026-02-12
---

# Chunk B 審閱：§2 產品定義 + §6 實戰案例

## 摘要

§2 的產品定位清楚回答了「IVCO 是什麼、不是什麼」，六大創新和四階段流程結構完整。
§6 的四個案例覆蓋了不同情境（個股評估/監控調整/主題篩選），但案例間結構一致性不足，
且 IV 計算公式在三個位置（§1 核心公式、§2 Stage 3、CLAUDE.md）存在互相矛盾的定義，
台積電案例數字無法用任何版本的公式驗算通過。這是最嚴重的問題。

---

## ✅ 確認項

1. §2 核心定位「專屬資訊優勢的私有數據庫，非通用估值計算機」(L151-152) — 清楚且與 §1 哲學一致
2. 四階段評估流程（L178-201）邏輯排序正確：事實門檻 → 信心評估 → 計算 → 逆向挑戰
3. Stage 4 Jane 逆向挑戰強制產出失敗路徑 (L198-201) — 與 §1 L67 Munger 精神對齊
4. §6 POWL (案例 1) 和 NVMI (案例 2) 完整呈現四階段流程：投資論點 → IV 計算 → Jane 挑戰 → Allen 決策
5. 定價方案三層設計 (L209-213) 由免費到企業版梯度合理
6. §6 ESMC 案例 (案例 3) 展示信心係數動態調整的真實場景 — 證明 §1 的公式不只是理論
7. 「AI 時代注意力變現已死，轉向存取權收費」(L215-216) 商業模式洞察方向正確

---

## ❓ 質疑項

### Q-B1: IV 計算公式維度不一致 — DNA 最嚴重問題

> §1 原文：「IV Range = Owner Earnings (Historical CAGR) × Confidence Coefficient (1.2x~1.8x)」(L35)
> §2 原文：「IV_Low = Owner_Earnings × Historical_CAGR × Confidence_Low (1.2x)」(L194)
> CLAUDE.md 原文：「Intrinsic Value = Historical Owner Earnings CAGR × Confidence Coefficient Range」

**問題**：三處公式互相矛盾。

- §1 寫法含糊：OE 和 CAGR 用括號並列，不確定是乘法還是「OE 的 CAGR」
- §2 寫法明確是三項相乘：OE x CAGR x Confidence，但維度錯誤 — 「業主盈餘（$/股）x 成長率（%）x 倍數」不等於「每股內在價值（$/股）」。如果 CAGR 是百分比（如 15%），結果會過小；如果是倍數（如 15x），那不是 CAGR
- CLAUDE.md 寫法省略了 OE 本身，只有「CAGR x Confidence」

**Allen 需確認**：實際的 IV 計算步驟是什麼？是否類似 P/E-like 的「OE x (1+CAGR)^N x Terminal_Multiple x Confidence」？還是有另一套投射邏輯？公式必須能讓 Chi 寫成程式碼。

### Q-B2: 台積電案例數字無法驗算

> §2 原文：「每股業主盈餘 NT$88.51 / Historical CAGR ~15% / 信心係數 1.4x / IV Range NT$4,500-6,200」(L226-229)

**問題**：用 §2 Stage 3 公式驗算：
- IV_Low = 88.51 x 0.15 x 1.2 = NT$15.9（荒謬）
- 即使 CAGR 用 15（非 0.15）：88.51 x 15 x 1.4 = NT$1,859（仍非 4,500-6,200）
- 無論怎麼代入，88.51 x 15% x 任何合理倍數都無法得到 NT$4,500+

**Allen 需確認**：NT$4,500-6,200 這個 IV Range 的實際計算過程。這是 DNA 中唯一有完整數字的示範案例，如果公式和數字不能互相驗證，整個 §2 的可信度受損。

### Q-B3: 安全邊際計算方式不統一

> §2 原文：「安全邊際 67%」(L231)，IV Range NT$4,500-6,200，當前價格 NT$1,680
> §6 原文：「安全邊際：36%」(L645)，IV Range $280-$450，股價 $180

**問題**：
- TSMC: (4500-1680)/4500 = 62.7%（用 IV_Low），(5350-1680)/5350 = 68.6%（用 IV_Mid）— 67% 不精確對應任何一種
- POWL: (280-180)/280 = 35.7%（用 IV_Low）— 接近 36%
- 兩個案例似乎用不同基準（TSMC 偏向 midpoint，POWL 偏向 low）

**Allen 需確認**：安全邊際的標準公式是「(IV_Low - Price) / IV_Low」還是「(IV_Mid - Price) / IV_Mid」？DNA 應統一定義。

### Q-B4: 產品名稱仍含已退役的「Calculator」

> §2 原文：「產品名稱：IVC Calculator: The Allen Framework for Intelligent Valuation」(L149)
> CLAUDE.md Decision Log (2026-02-09)：「品牌統一為 IVCO」「IVC 保留為方法論名稱，IVCO 為系統/品牌名」

**問題**：DNA L149 仍使用 "IVC Calculator" 作為產品名稱，但 Allen 已在 2026-02-09 決定品牌統一為 IVCO (Observatory，非 Calculator)。此行需更新以反映最新品牌決策。

### Q-B5: 每日 Top 20 卡片在 MVP 階段是否可行

> §2 原文：「每日 Top 20 安全邊際卡片流」(L167)

**問題**：產出每日 Top 20 需要：(1) 完成至少 50 家公司的四階段評估 (2) 每日更新股價與安全邊際 (3) 排序並渲染卡片 UI。§1 選股漏斗 (L99-119) 從 10,000 篩到 Top 20 需要 Filter 1-3 全部自動化。在 MVP 階段（目前 Phase 1 只完成 1/7 Collection），這個功能離實現很遠。

**Allen 需確認**：MVP 階段的產品輸出是什麼？建議先定義 MVP 版的「最小可用輸出」（例如：Allen 持股 3-5 家的 IV Dashboard），避免 DNA 的產品描述與實際開發節奏脫節。

### Q-B6: §6 案例 4「關鍵材料」與四階段流程的關係

> §6 原文：「案例 4：關鍵材料戰略投資」(L703)

**問題**：案例 4 列出中國壟斷現狀和投資標的清單（Eaton, Quanta, Vertiv 等），但：
- 沒有任何一家完成四階段評估（無 OE、無 CAGR、無 IV Range）
- VRT 和 BWXT 各配置 10% 但沒有 IV 計算依據
- 案例標題「關鍵材料」但內容跨越基礎設施（Eaton）、液冷（VRT）、核能（BWXT），主題散焦

**Allen 需確認**：這個案例是否代表另一種投資分析路徑（主題/產業鏈投資），還是只是尚未完成四階段評估的候選名單？如果是後者，建議標記為「待評估」。

---

## 🔲 遺漏項

### M-B1: 業主盈餘公式缺少 Working Capital Changes

> CLAUDE.md 定義：「Owner Earnings = Net Income + D&A - Maintenance CapEx - Working Capital Changes」
> DNA §2 L184：「業主盈餘 = Net Income + D&A - (Total CapEx × Maintenance Ratio)」

**建議**：DNA 的 OE 公式缺少「Working Capital Changes」這一項。CLAUDE.md 明確包含它。如果 Allen 的 OE 計算確實包含營運資金變動，DNA 應補齊；如果 Allen 刻意省略，CLAUDE.md 應同步更新。兩處必須一致。

### M-B2: §6 案例缺少 Stage 1 歷史事實的具體數據

**建議**：§6 的 POWL 和 NVMI 案例只列出 CAGR 和信心係數，但缺少：
- 每股業主盈餘（OE per share）— 只有 TSMC 案例有
- Maintenance Ratio 假設
- Log-Linear R² 值
- DSO/DIO 等穩健性指標（POWL 有提 DSO 52 天，但是在投資論點而非 Stage 1 框架中）

四階段流程的「Stage 1 歷史事實門檻」要求這些數據。案例應至少提供 OE per share，否則讀者無法理解 IV Range 是如何算出來的。

### M-B3: 信心係數的低值和高值拆分邏輯未說明

**建議**：§2 Stage 3 公式使用 Confidence_Low 和 Confidence_High 產生 IV Range (L194-195)，但所有案例（TSMC、POWL、NVMI）都只給出單一信心係數值（1.4x、1.3x、1.2x）。如何從一個係數生成區間？是否有隱含的 +/- 偏移？或者低值和高值是分別評估的？此邏輯應在 §2 中明確。

### M-B4: 定價方案缺少 Allen 自用階段定位

**建議**：§2 定價方案 (L209-213) 直接列出 Free/Pro/Enterprise 三層商業方案，但 IVCO 目前是 Allen 自用階段（Pre-Development）。建議補充一段「Phase 0: Private Use」說明，標記定價方案屬於「未來公開版」願景。否則讀者可能誤以為 MVP 就要實現三層定價。

### M-B5: §6 缺少一個「Stage 1 未通過而終止分析」的案例

**建議**：四個案例都是通過分析的正面案例。§2 Stage 1 的價值在於「不達標者直接終止分析」(L185 的篩選邏輯)，但 §6 沒有展示這個終止機制。建議補充一個被誠信門檻或歷史事實門檻攔截的案例，完整展示四階段流程的防禦能力。

---

## ⚠️ 矛盾項

### C-B1: 信心係數範圍 §1 vs §2 不一致

> §1 原文：「基線：1.2x~1.4x / 擴展：最高可達 1.8x」(L45-46)
> §2 原文：「Confidence_Low (1.2x) / Confidence_High (1.4x-1.8x)」(L194-195)

**衝突**：§1 將 1.2x-1.4x 定義為「基線」（一般穩健企業），暗示 1.2x 是最低的合理值。但 §2 公式將 1.2x 固定為 Confidence_Low，1.4x-1.8x 為 Confidence_High。如果一家企業的信心係數本身就是 1.2x（如 NVMI 因地緣風險），那 IV_Low 用 1.2x 是合理的，但 IV_High 呢？NVMI 案例 (L667) 只用了 1.2x，得出 $210-$345 的範圍 — 但如果 Low 和 High 都是 1.2x，範圍從何而來？

### C-B2: §2 台積電信心係數 vs §6 ESMC 案例的時序矛盾

> §2 原文：「信心係數 1.4x（2nm 量產前夜 + 零負債）」(L228)
> §6 原文：「TSMC 信心係數從 1.5x 下調至 1.4x」(L697)

**衝突**：表面上一致（§2 反映下調後的 1.4x），但 §2 把 1.4x 的理由歸於「2nm 量產前夜 + 零負債」— 這是正面因素。如果 1.4x 其實是因為 ESMC 風險而下調的結果，理由應該提及風險折減，而非只列正面因素。讀者不知道 1.4x 是「本來就是 1.4x」還是「從 1.5x 被拉下來的 1.4x」，這對理解信心係數的動態本質很重要。

### C-B3: 四大師 §2 vs DNA 標題 vs CLAUDE.md 人選不一致

> DNA 標題 (L14)：「整合 Buffett、Munger、Lynch、Fisher」
> §1 四大師表 (L62-67)：Graham、Buffett、Fisher、Munger
> §2 六大創新第 4 項 (L158)：「四大師整合評分卡」
> CLAUDE.md：「整合 Graham、Buffett、Fisher、Munger 四位大師理念」

**衝突**：DNA 標題包含 Lynch 但不包含 Graham；§1 表格和 CLAUDE.md 包含 Graham 但不包含 Lynch。四大師到底是哪四位？§2 的「四大師整合評分卡」指向哪個版本？此矛盾貫穿全文件，必須統一。

### C-B4: §6 案例 3 和案例 4 未遵循 §2 四階段流程

> §2 原文：四階段流程 — Stage 1 歷史事實 → Stage 2 信心係數 → Stage 3 IV 計算 → Stage 4 Jane 挑戰 (L178-201)
> §6 案例 3 (L679-700)：無 Stage 1-3，只有信心係數動態調整
> §6 案例 4 (L703-722)：無 Stage 1-4，只有產業觀察和標的清單

**衝突**：§2 定義的是 IVCO 的核心產品流程，但 §6 只有 2/4 案例完整遵循此流程。案例 3 展示的是「已持有標的的動態監控」，案例 4 展示的是「主題篩選」。這暗示 IVCO 可能需要定義多種分析模式（而非只有四階段），但 §2 沒有提到這些變體。

---

## 統計
- 確認項：7
- 質疑項：6（需 Allen 回覆）
- 遺漏項：5
- 矛盾項：4
