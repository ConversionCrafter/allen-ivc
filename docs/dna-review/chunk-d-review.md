---
chunk: D
section: §4 Agent 分工 + §5 開發路線圖
lines: L427-628
reviewer: Jane
status: complete
date: 2026-02-12
---

# Chunk D 審閱：§4 Agent 分工 + §5 開發路線圖

## 摘要

§4 Agent 分工定義了四個角色（Jane/Chi/Data Hunter/Allen），但與現行運作架構（rules/08 Dual-Agent Collaboration）有多處脫節。最關鍵的問題是 Data Hunter 角色在實際系統中不存在，且 Codex 的定位過於模糊。§5 開發路線圖的四階段結構合理，但 Phase 3 總覽與詳細段落互相矛盾，Phase 結構與 CLAUDE.md Project Milestones 不一致（4 階段 vs 5 階段），時間估算對 solo founder + AI agents 的一人軍團偏樂觀。

---

## ✅ 確認項

1. Jane 核心職責（L433-437）準確：失敗路徑、壓力測試（50% 大跌 + 利率翻倍 + 地緣危機）、四大師評分卡、誠信對帳單 — 與 CLAUDE.md 分析執行標準吻合
2. Jane Anti-Sycophancy 憲法（L455-456）與 CLAUDE.md 及 jane.md anti-sycophancy rules 一致
3. Chi 核心職責（L464-468）：CLI 工具鏈 + Payload/Supabase + n8n + 監控除錯 — 與 CLAUDE.md Chi 角色完全一致
4. Chi PSB 開發紀律（L470-473）與 CLAUDE.md PSB 系統定義一致
5. Allen 終裁者角色（L489-501）三項唯一權威清楚界定：Belief Memory commit 權 / 信心係數校準 / 投資組合配置
6. Allen 決策實例（L499-500）POWL 15% 配置 — 與 §6 案例 1（L652）交叉驗證一致
7. Agent 協作共識原則（L508-511）CLI > Browser 與 §3 CLI-First 哲學一致
8. Phase 1 依賴鏈（L549-558）8 個阻塞項與 SCRATCHPAD IVCO 啟動鏈吻合
9. Phase 2 CLI 工具鏈（L566-577）原子化設計 + JSON 輸出 + --help 文檔化與 §3 一致
10. 技術債風險識別（L617-625）三項合理：Prompt Injection / 逆向 API TOS / 數據分散

---

## ❓ 質疑項

### Q-D1: Data Hunter 角色的實體化問題
> 原文：「Data Hunter — 數據偵察機器人」(L477)
> 原文：「核心職責：EODHD API 數據抓取（財報 + News + Transcripts）、Bird CLI（X 平台地緣政治監控）、SEC EDGAR 二次驗證、數據清洗與異常值修正（Winsorized CAGR）」(L482-485)

**問題**：Data Hunter 在現行 Agent Roster（rules/08）中不存在。目前架構只有 Jane / Chi / Codex 三角色。Data Hunter 的職責在實際運作中由 Chi（CLI 工具開發）和 launchd cron（X intel collect）承擔。Allen 打算：(A) 實作為獨立 agent/subagent？(B) 視為 Chi 的子功能模組？(C) 視為 n8n workflow 的擬人化？三者對開發路線影響完全不同。

### Q-D2: Jane Constitution v2.1 的版本追蹤
> 原文：「Jane Constitution 演進：v1.0：分散投資 3-5 檔 / v2.0：TSMC 可佔 40-100%（Allen 決策）/ v2.1：IV 相對便宜度比較（動態配置觸發）」(L439-442)

**問題**：CLAUDE.md 和 jane.md 中都沒有 Jane Constitution 版本概念。此版本演進是從歷史研究中提取的？還是 Allen 計劃在 IVCO 中正式維護 Jane Constitution 版本？如果是後者，應在 jane.md 或 CLAUDE.md 建立版本追蹤。

### Q-D3: 6+2 Skill 模組 vs Skills 上限治理
> 原文：「核心 6：risk-gatekeeper, financial-xray, growth-catalyst, loan-stress-test, trust-tracker, archive-master / 防禦 2：graham-shield, buffett-moat」(L444-446)

**問題**：這 8 個 skill 目前都不存在於 ~/.claude/skills/。rules/02 Skills 治理規則限制上限 12 個。8 個新 skill 加上既有 skill 可能觸碰上限。Allen 計劃逐一建立？還是概念設計，實作時可能合併簡化？

### Q-D4: Phase 1 時間估算 — Solo Founder 現實性
> 原文：「Phase 1（Week 1-4）：Foundation / Blog SEO + 基礎數據模型 + Payload CMS + MCP 整合」(L531-532)

**問題**：Phase 1 包含 Blog SEO + 7 個 Payload Collections（目前只完成 1/7）+ MCP 整合 + 7 個阻塞項。CLAUDE.md 顯示 Phase 1 進度 40%。4 週是否現實？Blog SEO 還需要大量內容產出（§5 L603 提到 29 篇文章）。建議 Allen 重新評估時間框架。

### Q-D5: Phase 3 內部矛盾 — Intelligence vs Content Pipeline
> 原文（四階段總覽 L537-538）：「Phase 3（Week 13-20）：Intelligence / AI Agent 深度整合 + 信心係數自動調整 + Jane 逆向挑戰自動化」
> 原文（Phase 3 詳細 L580-594）：「Phase 3: n8n Content Pipeline / 三階段流程：偵查 → 策略 → 執行 / SEO 策略：Pillar Page + Cluster Content」

**問題**：同一個 Phase 3，總覽說是 AI Intelligence，詳細段落卻是 SEO Content Pipeline。兩個完全不同的工作流被裝進同一個 Phase，DNA 內部自相矛盾。哪個才是 Phase 3 的真正內容？建議拆分或釐清。

### Q-D6: Phase 4 商業化 — 6 個月是否過早
> 原文：「Phase 4（Month 6+）：Scale / API 產品化 + 社群建設 + Enterprise 諮詢服務」(L540-541)

**問題**：6 個月後推出 Enterprise 諮詢服務（$199+/月 + 5000 萬級高端諮詢），但系統可能剛完成 Phase 3。Allen 是先做 private tool（服務自己），還是確定走 SaaS 產品化？如果是後者，payment、用戶管理、投資建議法律免責等在路線圖中完全未提及。

### Q-D7: Mission Control 10 Agent 模式的定位
> 原文：「Mission Control 模式（參考）：10 Agent squad，各有 SOUL.md + session key / Heartbeat：每 15 分鐘交錯喚醒」(L518-521)

**問題**：標註為「參考」，但 10 Agent + 15 分鐘 heartbeat 的複雜度遠超目前 3 agent 架構。Allen 計劃在某個 Phase 實作？還是僅為知識參考不打算實作？如果不實作，建議移至附錄或明確標註「知識參考，非 IVCO 規劃」，避免誤導開發預期。

---

## 🔲 遺漏項

### M-D1: Codex 在 Agent 分工中缺乏明確定位
**建議**：§4 有 Jane、Chi、Data Hunter、Allen 四個角色的詳細描述，但 Codex 只在 L513-516 被提為 "Future"。rules/08 已定義 Codex 為正式第三 agent（ChatGPT 5.2），且已有實戰記錄。建議在 §4 補充 Codex 角色定義，說明「Propose only, Jane reviews」的邊界。

### M-D2: Agent 間衝突解決機制缺失
**建議**：§4 定義 Allen 為終裁者，但沒有描述 Jane vs Chi 意見分歧時的解決流程。rules/08 有 Decision Chain（Codex 提出 -> Jane 仲裁 -> Allen 終裁）。DNA 應定義投資分析衝突解決鏈，例如 Chi 數據計算結果 vs Jane 風險評估結論不一致時的優先級。

### M-D3: Phase 驗收標準（Exit Criteria）不明確
**建議**：Phase 1 列出 8 個阻塞項，但沒有定義「Phase 1 完成」的驗收標準。全部 8 項是 must-have 還是部分 nice-to-have？每個 Phase 都需要明確的 Exit Criteria。

### M-D4: 營運成本預算缺失
**建議**：EODHD API 99 歐/月、Supabase Pro $25/月、域名維護（ivco.io + ivco.ai）、未來可能的 VPS/CDN 費用。Solo founder 的月度固定成本估算完全缺失。建議在路線圖或附錄中加入。

### M-D5: 各 Phase 回滾策略缺失
**建議**：路線圖只有前進路徑，沒有回滾計劃。EODHD API 中斷、Payload CMS 不適合、n8n 效能瓶頸等情境的 fallback 方案未定義。Allen 的 rules/02 強調「可回滾」，路線圖應體現。

### M-D6: Security 基建在路線圖中缺位
**建議**：技術債（L617-625）提到 Prompt Injection，但未涵蓋 API key 管理、用戶認證、IVCO Fisher 品牌帳號安全。建議在某個 Phase 明確包含安全基建里程碑。

---

## ⚠️ 矛盾項

### C-D1: 四大師 vs Lynch — 標題人物不一致
> DNA L14：「整合 Buffett、Munger、**Lynch**、Fisher 的 Allen 演繹」
> DNA §1 L62-67（四大師表格）：**Graham**、Buffett、Fisher、Munger

**衝突**：DNA 標題提到 Lynch（Peter Lynch），§1 四大師表格卻是 Graham（Benjamin Graham）。§8 結語 L840 和 L843 又提到 Lynch。Graham 和 Lynch 的投資風格差異很大（Graham = Deep Value + Safety Margin，Lynch = Growth at Reasonable Price）。這直接影響 IVCO 哲學定位。Allen 需要統一：框架的四大師究竟包含誰？

### C-D2: Phase 結構不一致 — DNA 4 階段 vs CLAUDE.md 5 階段
> DNA §5：Phase 1 Foundation / Phase 2 Automation / Phase 3 Intelligence / Phase 4 Scale
> CLAUDE.md Milestones：Phase 1 Payload CMS / Phase 2 Python CLI / Phase 3 n8n / Phase 4 Playground 前端 / Phase 5 Qdrant

**衝突**：DNA 4 個 Phase，CLAUDE.md 5 個 Phase，且內容分佈完全不同。DNA Phase 1 包含 Blog SEO + Payload CMS + MCP，CLAUDE.md Phase 1 只有 Payload CMS Collections。DNA 沒有 Qdrant Phase，CLAUDE.md 沒有 Blog SEO 和商業化。兩份文件的路線圖必須統一，否則開發時會混亂。

### C-D3: Jane 報告格式不一致 — 五段 vs 六段
> DNA §4 L448-453：五段式（1.公司概述 / 2.財務分析 / 3.展望評估 / 4.風險警告 / 5.結論建議）
> CLAUDE.md Jane 報告格式：六段式（1.Jane 風險警告 / 2.核心指標掃描 / 3.OE 評估 / 4.Live in Loans 影響 / 5.結論與存檔建議 / 6.來源標註）

**衝突**：DNA 版「風險警告」放第四位，CLAUDE.md 版「風險警告」放第一位（risk-first）。DNA 版缺少「Live in Loans 影響」和「來源標註」。Jane 的 DNA 是 risk-first，CLAUDE.md 版更符合角色定位。需要 Allen 確認哪個版本為準。

### C-D4: Codex 定位 — DNA "Future" vs rules/08 "Already Active"
> DNA L513-514：「Codex 整合（Future）：CLI wrapper（最穩定）→ MCP adapter（探索中）」
> rules/08 Agent Roster：「Codex (OpenAI MCP) | ChatGPT 5.2 | External Consultant | Propose only -> Jane reviews」

**衝突**：DNA 將 Codex 標記為 "Future"，rules/08 已定義 Codex 為 active agent 且有多次實戰記錄（PDCA 根因分析）。DNA 應反映 Codex 現行狀態。

### C-D5: Phase 3 自相矛盾 — 總覽 vs 詳細段落
> DNA L537-538（總覽）：「Phase 3: Intelligence — AI Agent 深度整合 + 信心係數自動調整 + Jane 逆向挑戰自動化」
> DNA L580-594（詳細）：「Phase 3: n8n Content Pipeline — 偵查 → 策略 → 執行 / SEO 策略」

**衝突**：同一個 Phase 3，總覽說是 AI Intelligence，詳細說是 SEO Content Pipeline。兩個完全不同的工作流被裝進同一個 Phase，DNA 內部自相矛盾。

---

## 統計

- 確認項：10
- 質疑項：7（需 Allen 回覆）
- 遺漏項：6
- 矛盾項：5
