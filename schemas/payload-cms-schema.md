# IVCO - Payload CMS Collection Schemas

> Version: 1.0.0
> Date: 2026-02-04
> Author: Chi (AI Native Full-Stack Engineer)

---

## 1. Companies Collection (公司主檔)

**用途**: 儲存所有追蹤公司的基本資料、誠信評分、歷史業主盈餘

### Fields

```typescript
{
  slug: 'companies',
  fields: [
    // === 基本資訊 ===
    {
      name: 'ticker',
      type: 'text',
      required: true,
      unique: true,
      admin: {
        description: '股票代碼 (e.g., TSMC, AAPL)'
      }
    },
    {
      name: 'company_name',
      type: 'text',
      required: true,
      admin: {
        description: '公司全名 (e.g., Taiwan Semiconductor Manufacturing Company)'
      }
    },
    {
      name: 'company_name_zh',
      type: 'text',
      admin: {
        description: '公司中文名稱（選填）'
      }
    },
    {
      name: 'exchange',
      type: 'select',
      required: true,
      options: [
        { label: 'NYSE', value: 'NYSE' },
        { label: 'NASDAQ', value: 'NASDAQ' },
        { label: 'TSE', value: 'TSE' },
        { label: 'TWSE', value: 'TWSE' },
        { label: 'Other', value: 'OTHER' }
      ]
    },
    {
      name: 'sector',
      type: 'text',
      required: true,
      admin: {
        description: '產業類別 (e.g., Semiconductors, Technology)'
      }
    },
    {
      name: 'country',
      type: 'text',
      required: true,
      admin: {
        description: '總部所在國家'
      }
    },

    // === 財務基礎數據 ===
    {
      name: 'total_shares',
      type: 'number',
      required: true,
      admin: {
        description: '總股本（股數，單位：百萬股）'
      }
    },
    {
      name: 'currency',
      type: 'select',
      required: true,
      defaultValue: 'USD',
      options: [
        { label: 'USD', value: 'USD' },
        { label: 'TWD', value: 'TWD' },
        { label: 'JPY', value: 'JPY' },
        { label: 'EUR', value: 'EUR' }
      ]
    },

    // === 歷史業主盈餘 (Owner Earnings) ===
    {
      name: 'latest_owner_earnings',
      type: 'number',
      required: true,
      admin: {
        description: '最新年度業主盈餘（單位：百萬）'
      }
    },
    {
      name: 'historical_oe_cagr_7y',
      type: 'number',
      required: true,
      admin: {
        description: '過去 7 年業主盈餘 CAGR (%)，這是 IVC 計算的「事實基礎」'
      }
    },
    {
      name: 'historical_oe_cagr_10y',
      type: 'number',
      admin: {
        description: '過去 10 年業主盈餘 CAGR (%)（若有）'
      }
    },

    // === 誠信門檻 (Integrity Gate) ===
    {
      name: 'integrity_score',
      type: 'number',
      required: true,
      min: 0,
      max: 100,
      admin: {
        description: '管理層誠信評分 (0-100%)，低於 100% 必須說明原因'
      }
    },
    {
      name: 'integrity_notes',
      type: 'richText',
      admin: {
        description: '誠信評分說明（若 <100%，必須詳述原因）'
      }
    },
    {
      name: 'has_integrity_red_flag',
      type: 'checkbox',
      defaultValue: false,
      admin: {
        description: '是否有誠信污點？（若勾選，系統會終止分析）'
      }
    },

    // === 生物學護城河 ===
    {
      name: 'moat_type',
      type: 'select',
      options: [
        { label: '網絡效應', value: 'network_effect' },
        { label: '規模經濟', value: 'economies_of_scale' },
        { label: '技術專利', value: 'technology_patent' },
        { label: '品牌效應', value: 'brand' },
        { label: '轉換成本', value: 'switching_cost' },
        { label: '監管護城河', value: 'regulatory' },
        { label: '複合型', value: 'multiple' }
      ],
      admin: {
        description: '主要護城河類型（費雪的競爭優勢評估）'
      }
    },
    {
      name: 'moat_strength',
      type: 'select',
      required: true,
      options: [
        { label: '極強（台積電級別）', value: 'very_strong' },
        { label: '強勁', value: 'strong' },
        { label: '中等', value: 'moderate' },
        { label: '弱', value: 'weak' }
      ]
    },
    {
      name: 'biological_advantage',
      type: 'richText',
      admin: {
        description: '生物學競爭優勢描述（如何在演化中保持領先？）'
      }
    },

    // === 管理層追蹤 ===
    {
      name: 'ceo_name',
      type: 'text',
      admin: {
        description: '現任 CEO 姓名'
      }
    },
    {
      name: 'ceo_tenure_years',
      type: 'number',
      admin: {
        description: 'CEO 任期（年）'
      }
    },
    {
      name: 'management_stability',
      type: 'select',
      options: [
        { label: '極穩定（10年+）', value: 'very_stable' },
        { label: '穩定', value: 'stable' },
        { label: '中等', value: 'moderate' },
        { label: '不穩定', value: 'unstable' }
      ]
    },

    // === 最新市價與估值狀態 ===
    {
      name: 'current_price',
      type: 'number',
      admin: {
        description: '最新市價（每股）'
      }
    },
    {
      name: 'current_price_updated_at',
      type: 'date',
      admin: {
        description: '市價更新時間'
      }
    },
    {
      name: 'latest_iv_low',
      type: 'number',
      admin: {
        description: '最新 IVC 保守下限（每股）'
      }
    },
    {
      name: 'latest_iv_high',
      type: 'number',
      admin: {
        description: '最新 IVC 樂觀上限（每股）'
      }
    },
    {
      name: 'valuation_status',
      type: 'select',
      options: [
        { label: '極度低估（買入良機）', value: 'deep_value' },
        { label: '合理偏低（可買入）', value: 'undervalued' },
        { label: '合理價格（持有）', value: 'fair' },
        { label: '偏高（觀望）', value: 'overvalued' },
        { label: '泡沫區（避開）', value: 'bubble' }
      ],
      admin: {
        description: '當前估值狀態（系統自動更新）'
      }
    },

    // === 觀察名單狀態 ===
    {
      name: 'in_watchlist',
      type: 'checkbox',
      defaultValue: false,
      admin: {
        description: '是否在觀察名單中'
      }
    },
    {
      name: 'is_core_holding',
      type: 'checkbox',
      defaultValue: false,
      admin: {
        description: '是否為核心持股（Allen 的 3-5 家核心標的）'
      }
    },
    {
      name: 'allocation_percentage',
      type: 'number',
      admin: {
        description: '持股配置比例 (%)（若是核心持股）'
      }
    },

    // === 關聯 ===
    {
      name: 'valuations',
      type: 'relationship',
      relationTo: 'valuations',
      hasMany: true,
      admin: {
        description: '歷史估值記錄'
      }
    },
    {
      name: 'events',
      type: 'relationship',
      relationTo: 'events',
      hasMany: true,
      admin: {
        description: '重大事件記錄'
      }
    },
    {
      name: 'financial_data',
      type: 'relationship',
      relationTo: 'financial_data',
      hasMany: true,
      admin: {
        description: '財務數據記錄'
      }
    },

    // === 時間戳 ===
    {
      name: 'created_at',
      type: 'date',
      admin: {
        readOnly: true
      }
    },
    {
      name: 'updated_at',
      type: 'date',
      admin: {
        readOnly: true
      }
    }
  ]
}
```

---

## 2. Valuations Collection (估值記錄)

**用途**: 記錄每一次 IVC 計算的完整過程與結果，支援「時間旅行」回溯

### Fields

```typescript
{
  slug: 'valuations',
  fields: [
    // === 關聯公司 ===
    {
      name: 'company',
      type: 'relationship',
      relationTo: 'companies',
      required: true,
      admin: {
        description: '關聯的公司'
      }
    },

    // === 計算時間 ===
    {
      name: 'valuation_date',
      type: 'date',
      required: true,
      admin: {
        description: '估值計算日期'
      }
    },

    // === 階段二：歷史事實 ===
    {
      name: 'historical_oe',
      type: 'number',
      required: true,
      admin: {
        description: '歷史業主盈餘（用於計算的基準值）'
      }
    },
    {
      name: 'historical_cagr',
      type: 'number',
      required: true,
      admin: {
        description: '歷史業主盈餘 CAGR (%)，這是「事實常數」'
      }
    },
    {
      name: 'total_shares',
      type: 'number',
      required: true,
      admin: {
        description: '計算時使用的總股本（百萬股）'
      }
    },

    // === 階段三：展望因子與信心係數 ===
    {
      name: 'confidence_coefficient_low',
      type: 'number',
      required: true,
      min: 0.5,
      max: 2.0,
      admin: {
        description: '信心係數下限（保守情境，通常 1.1x - 1.2x）'
      }
    },
    {
      name: 'confidence_coefficient_high',
      type: 'number',
      required: true,
      min: 0.5,
      max: 2.0,
      admin: {
        description: '信心係數上限（樂觀情境，通常 1.3x - 1.5x）'
      }
    },
    {
      name: 'confidence_rationale',
      type: 'richText',
      required: true,
      admin: {
        description: '信心係數的依據（資本支出計畫、新產品週期、市場擴張等）'
      }
    },

    // === 計算結果 ===
    {
      name: 'iv_total_low',
      type: 'number',
      required: true,
      admin: {
        description: 'IVC 保守下限（總市值，單位：百萬）'
      }
    },
    {
      name: 'iv_total_high',
      type: 'number',
      required: true,
      admin: {
        description: 'IVC 樂觀上限（總市值，單位：百萬）'
      }
    },
    {
      name: 'iv_per_share_low',
      type: 'number',
      required: true,
      admin: {
        description: 'IVC 保守下限（每股價值）⭐ 強制項目'
      }
    },
    {
      name: 'iv_per_share_high',
      type: 'number',
      required: true,
      admin: {
        description: 'IVC 樂觀上限（每股價值）⭐ 強制項目'
      }
    },

    // === 階段四：實戰導航 ===
    {
      name: 'market_price_at_valuation',
      type: 'number',
      required: true,
      admin: {
        description: '計算時的市場價格（每股）'
      }
    },
    {
      name: 'deviation_percentage',
      type: 'number',
      admin: {
        description: '偏離度 (%) = (市價 / IV 中值) - 1'
      }
    },
    {
      name: 'recommendation',
      type: 'select',
      required: true,
      options: [
        { label: '強烈買入（深度價值）', value: 'strong_buy' },
        { label: '買入', value: 'buy' },
        { label: '持有', value: 'hold' },
        { label: '觀望', value: 'watch' },
        { label: '避開', value: 'avoid' }
      ]
    },

    // === Jane 的逆向挑戰 ===
    {
      name: 'risk_factors',
      type: 'richText',
      admin: {
        description: 'Jane 的風險警告：列出三個可能導致投資失敗的路徑'
      }
    },
    {
      name: 'stress_test_result',
      type: 'richText',
      admin: {
        description: '壓力測試：股價大跌 50% 對質押安全性的影響'
      }
    },

    // === 元數據 ===
    {
      name: 'calculation_method',
      type: 'select',
      defaultValue: 'ivc_framework',
      options: [
        { label: 'IVC Framework (Allen 方法)', value: 'ivc_framework' },
        { label: 'DCF 折現現金流', value: 'dcf' },
        { label: '相對估值法', value: 'relative' }
      ]
    },
    {
      name: 'calculated_by',
      type: 'select',
      options: [
        { label: 'Allen 手動計算', value: 'manual' },
        { label: 'Chi (CLI 自動)', value: 'cli_auto' },
        { label: 'Jane (AI 輔助)', value: 'ai_assisted' }
      ]
    },
    {
      name: 'notes',
      type: 'richText',
      admin: {
        description: '其他備註或特殊考量'
      }
    },

    // === 時間戳 ===
    {
      name: 'created_at',
      type: 'date',
      admin: {
        readOnly: true
      }
    }
  ]
}
```

---

## 3. Events Collection (重大事件追蹤)

**用途**: 記錄影響信心係數的所有重大事件，支援「預測對帳單」

### Fields

```typescript
{
  slug: 'events',
  fields: [
    // === 關聯公司 ===
    {
      name: 'company',
      type: 'relationship',
      relationTo: 'companies',
      required: true
    },

    // === 事件基本資訊 ===
    {
      name: 'event_date',
      type: 'date',
      required: true,
      admin: {
        description: '事件發生日期'
      }
    },
    {
      name: 'event_type',
      type: 'select',
      required: true,
      options: [
        { label: '財報發布', value: 'earnings_report' },
        { label: '電話會議', value: 'earnings_call' },
        { label: '法說會', value: 'investor_day' },
        { label: '重大資本支出', value: 'capex_announcement' },
        { label: '併購案', value: 'ma_activity' },
        { label: '新產品發布', value: 'product_launch' },
        { label: '管理層變動', value: 'management_change' },
        { label: '股利政策', value: 'dividend_policy' },
        { label: '股票回購', value: 'share_buyback' },
        { label: '地緣政治', value: 'geopolitical' },
        { label: '監管變化', value: 'regulatory' },
        { label: '其他', value: 'other' }
      ]
    },
    {
      name: 'event_title',
      type: 'text',
      required: true,
      admin: {
        description: '事件標題（簡潔描述）'
      }
    },
    {
      name: 'event_description',
      type: 'richText',
      required: true,
      admin: {
        description: '事件詳細描述'
      }
    },

    // === 事件影響評估 ===
    {
      name: 'impact_on_confidence',
      type: 'select',
      required: true,
      options: [
        { label: '顯著正面（+10%以上）', value: 'very_positive' },
        { label: '正面（+5%）', value: 'positive' },
        { label: '中性（無影響）', value: 'neutral' },
        { label: '負面（-5%）', value: 'negative' },
        { label: '顯著負面（-10%以上）', value: 'very_negative' }
      ],
      admin: {
        description: '對信心係數的影響程度'
      }
    },
    {
      name: 'triggers_revaluation',
      type: 'checkbox',
      defaultValue: false,
      admin: {
        description: '是否觸發 IVC 重新計算？'
      }
    },
    {
      name: 'is_structural_change',
      type: 'checkbox',
      defaultValue: false,
      admin: {
        description: '是否為結構性變化？（非短期波動）'
      }
    },

    // === 管理層承諾追蹤（若適用）===
    {
      name: 'contains_management_commitment',
      type: 'checkbox',
      defaultValue: false,
      admin: {
        description: '事件中是否包含管理層承諾？'
      }
    },
    {
      name: 'commitment_details',
      type: 'richText',
      admin: {
        condition: (data) => data.contains_management_commitment,
        description: '管理層承諾的具體內容（如：2026 Q4 投產、毛利率達 45%）'
      }
    },
    {
      name: 'commitment_target_date',
      type: 'date',
      admin: {
        condition: (data) => data.contains_management_commitment,
        description: '承諾預期達成日期'
      }
    },

    // === 實際結果對照（預測對帳單）===
    {
      name: 'has_actual_result',
      type: 'checkbox',
      defaultValue: false,
      admin: {
        description: '是否已有實際結果可供對照？'
      }
    },
    {
      name: 'actual_result',
      type: 'richText',
      admin: {
        condition: (data) => data.has_actual_result,
        description: '實際執行結果（用於對帳單）'
      }
    },
    {
      name: 'achievement_rate',
      type: 'number',
      admin: {
        condition: (data) => data.has_actual_result,
        description: '承諾達成率 (%)，影響誠信評分'
      }
    },

    // === 資料來源 ===
    {
      name: 'source_type',
      type: 'select',
      options: [
        { label: 'SEC Filings (10-K, 10-Q, 8-K)', value: 'sec_filing' },
        { label: '公司官網', value: 'company_website' },
        { label: '財經媒體', value: 'financial_media' },
        { label: 'Twitter/X', value: 'twitter' },
        { label: 'Reddit', value: 'reddit' },
        { label: '其他社群媒體', value: 'social_media' },
        { label: '其他', value: 'other' }
      ]
    },
    {
      name: 'source_url',
      type: 'text',
      admin: {
        description: '資料來源 URL'
      }
    },

    // === 時間戳 ===
    {
      name: 'created_at',
      type: 'date',
      admin: {
        readOnly: true
      }
    },
    {
      name: 'updated_at',
      type: 'date',
      admin: {
        readOnly: true
      }
    }
  ]
}
```

---

## 4. Financial_Data Collection (財務數據)

**用途**: 儲存季度/年度財務數據，用於計算業主盈餘

### Fields

```typescript
{
  slug: 'financial_data',
  fields: [
    // === 關聯公司 ===
    {
      name: 'company',
      type: 'relationship',
      relationTo: 'companies',
      required: true
    },

    // === 財報期間 ===
    {
      name: 'period_type',
      type: 'select',
      required: true,
      options: [
        { label: '年報 (10-K)', value: 'annual' },
        { label: '季報 (10-Q)', value: 'quarterly' }
      ]
    },
    {
      name: 'fiscal_year',
      type: 'number',
      required: true,
      admin: {
        description: '會計年度（如：2025）'
      }
    },
    {
      name: 'fiscal_quarter',
      type: 'select',
      options: [
        { label: 'Q1', value: 'Q1' },
        { label: 'Q2', value: 'Q2' },
        { label: 'Q3', value: 'Q3' },
        { label: 'Q4', value: 'Q4' }
      ],
      admin: {
        condition: (data) => data.period_type === 'quarterly',
        description: '會計季度'
      }
    },
    {
      name: 'filing_date',
      type: 'date',
      admin: {
        description: '財報提交日期'
      }
    },

    // === 損益表數據 ===
    {
      name: 'revenue',
      type: 'number',
      required: true,
      admin: {
        description: '營業收入（單位：百萬）'
      }
    },
    {
      name: 'net_income',
      type: 'number',
      required: true,
      admin: {
        description: '淨利（單位：百萬）'
      }
    },
    {
      name: 'depreciation_amortization',
      type: 'number',
      required: true,
      admin: {
        description: '折舊與攤銷 (D&A)（單位：百萬）'
      }
    },

    // === 現金流量表數據 ===
    {
      name: 'operating_cash_flow',
      type: 'number',
      admin: {
        description: '營運現金流（單位：百萬）'
      }
    },
    {
      name: 'total_capex',
      type: 'number',
      required: true,
      admin: {
        description: '總資本支出（單位：百萬）'
      }
    },
    {
      name: 'maintenance_capex',
      type: 'number',
      required: true,
      admin: {
        description: '維持性資本支出（用於業主盈餘計算）'
      }
    },
    {
      name: 'growth_capex',
      type: 'number',
      admin: {
        description: '成長性資本支出（擴張性投資）'
      }
    },
    {
      name: 'working_capital_change',
      type: 'number',
      admin: {
        description: '營運資本變動（單位：百萬）'
      }
    },

    // === 業主盈餘計算（Owner Earnings）===
    {
      name: 'owner_earnings',
      type: 'number',
      required: true,
      admin: {
        description: '業主盈餘 = 淨利 + D&A - 維持性 CapEx - 營運資本變動'
      }
    },
    {
      name: 'owner_earnings_per_share',
      type: 'number',
      admin: {
        description: '每股業主盈餘'
      }
    },

    // === 其他關鍵指標 ===
    {
      name: 'roic',
      type: 'number',
      admin: {
        description: 'ROIC (%)：投入資本回報率'
      }
    },
    {
      name: 'fcf',
      type: 'number',
      admin: {
        description: '自由現金流（單位：百萬）'
      }
    },

    // === 元數據 ===
    {
      name: 'data_source',
      type: 'select',
      options: [
        { label: 'SEC EDGAR', value: 'sec_edgar' },
        { label: 'Yahoo Finance', value: 'yahoo_finance' },
        { label: 'Financial Modeling Prep', value: 'fmp' },
        { label: '手動輸入', value: 'manual' },
        { label: '其他', value: 'other' }
      ]
    },
    {
      name: 'notes',
      type: 'richText',
      admin: {
        description: '備註（如：一次性費用調整說明）'
      }
    },

    // === 時間戳 ===
    {
      name: 'created_at',
      type: 'date',
      admin: {
        readOnly: true
      }
    },
    {
      name: 'updated_at',
      type: 'date',
      admin: {
        readOnly: true
      }
    }
  ]
}
```

---

## 5. Commitments Collection (管理層承諾對帳單)

**用途**: 追蹤管理層承諾 vs 實際執行，用於計算誠信評分

### Fields

```typescript
{
  slug: 'commitments',
  fields: [
    // === 關聯 ===
    {
      name: 'company',
      type: 'relationship',
      relationTo: 'companies',
      required: true
    },
    {
      name: 'related_event',
      type: 'relationship',
      relationTo: 'events',
      admin: {
        description: '關聯的事件（如法說會、電話會議）'
      }
    },

    // === 承諾內容 ===
    {
      name: 'commitment_date',
      type: 'date',
      required: true,
      admin: {
        description: '管理層做出承諾的日期'
      }
    },
    {
      name: 'commitment_type',
      type: 'select',
      required: true,
      options: [
        { label: '資本支出計畫', value: 'capex_plan' },
        { label: '產能擴張', value: 'capacity_expansion' },
        { label: '新產品上市', value: 'product_launch' },
        { label: '毛利率目標', value: 'margin_target' },
        { label: '營收目標', value: 'revenue_target' },
        { label: '併購計畫', value: 'ma_plan' },
        { label: '股利政策', value: 'dividend_policy' },
        { label: '其他', value: 'other' }
      ]
    },
    {
      name: 'commitment_description',
      type: 'richText',
      required: true,
      admin: {
        description: '承諾的具體內容（原文或摘要）'
      }
    },
    {
      name: 'quantitative_target',
      type: 'text',
      admin: {
        description: '量化目標（如：毛利率 45%、資本支出 $100B）'
      }
    },
    {
      name: 'target_date',
      type: 'date',
      required: true,
      admin: {
        description: '承諾預期達成的日期'
      }
    },

    // === 執行追蹤 ===
    {
      name: 'status',
      type: 'select',
      required: true,
      defaultValue: 'pending',
      options: [
        { label: '進行中', value: 'pending' },
        { label: '按計畫執行', value: 'on_track' },
        { label: '提前達成', value: 'ahead' },
        { label: '延遲但仍在執行', value: 'delayed' },
        { label: '已達成', value: 'achieved' },
        { label: '未達成', value: 'missed' },
        { label: '已取消', value: 'cancelled' }
      ]
    },
    {
      name: 'actual_completion_date',
      type: 'date',
      admin: {
        condition: (data) => ['achieved', 'missed'].includes(data.status),
        description: '實際完成日期（若已達成或未達成）'
      }
    },
    {
      name: 'actual_result',
      type: 'richText',
      admin: {
        condition: (data) => ['achieved', 'missed'].includes(data.status),
        description: '實際執行結果'
      }
    },
    {
      name: 'achievement_percentage',
      type: 'number',
      min: 0,
      max: 150,
      admin: {
        condition: (data) => ['achieved', 'missed'].includes(data.status),
        description: '達成率 (%)，100% 表示完全達成，>100% 表示超額達成'
      }
    },

    // === 影響評估 ===
    {
      name: 'impact_on_integrity_score',
      type: 'number',
      admin: {
        description: '對誠信評分的影響（+5 ~ -10 分）'
      }
    },
    {
      name: 'lessons_learned',
      type: 'richText',
      admin: {
        description: '從此次承諾/執行中學到的教訓'
      }
    },

    // === 時間戳 ===
    {
      name: 'created_at',
      type: 'date',
      admin: {
        readOnly: true
      }
    },
    {
      name: 'updated_at',
      type: 'date',
      admin: {
        readOnly: true
      }
    }
  ]
}
```

---

## 6. Watchlist Collection (觀察名單)

**用途**: 管理 Allen 的觀察名單（10+ 家公司）與核心持股（3-5 家）

### Fields

```typescript
{
  slug: 'watchlist',
  fields: [
    // === 關聯公司 ===
    {
      name: 'company',
      type: 'relationship',
      relationTo: 'companies',
      required: true
    },

    // === 觀察狀態 ===
    {
      name: 'added_date',
      type: 'date',
      required: true,
      defaultValue: () => new Date(),
      admin: {
        description: '加入觀察名單日期'
      }
    },
    {
      name: 'priority',
      type: 'select',
      required: true,
      defaultValue: 'medium',
      options: [
        { label: '核心持股（P0）', value: 'core_holding' },
        { label: '高優先級（P1）', value: 'high' },
        { label: '中優先級（P2）', value: 'medium' },
        { label: '低優先級（P3）', value: 'low' }
      ]
    },
    {
      name: 'tracking_status',
      type: 'select',
      required: true,
      defaultValue: 'active',
      options: [
        { label: '積極追蹤', value: 'active' },
        { label: '定期檢查', value: 'periodic' },
        { label: '暫停追蹤', value: 'paused' },
        { label: '已移除', value: 'removed' }
      ]
    },

    // === 追蹤原因 ===
    {
      name: 'reason_for_watching',
      type: 'richText',
      required: true,
      admin: {
        description: '為什麼加入觀察名單？（符合哪些篩選條件？）'
      }
    },
    {
      name: 'target_entry_price',
      type: 'number',
      admin: {
        description: '目標進場價格（每股）'
      }
    },
    {
      name: 'target_entry_iv_discount',
      type: 'number',
      admin: {
        description: '目標進場時的 IV 折扣 (%)，如：20% 表示要等到市價低於 IV 20%'
      }
    },

    // === 持股資訊（若已持有）===
    {
      name: 'is_holding',
      type: 'checkbox',
      defaultValue: false,
      admin: {
        description: '是否已持有？'
      }
    },
    {
      name: 'position_size',
      type: 'number',
      admin: {
        condition: (data) => data.is_holding,
        description: '持股數量（股數）'
      }
    },
    {
      name: 'average_cost',
      type: 'number',
      admin: {
        condition: (data) => data.is_holding,
        description: '平均成本（每股）'
      }
    },
    {
      name: 'allocation_percentage',
      type: 'number',
      admin: {
        condition: (data) => data.is_holding,
        description: '佔總資產比例 (%)，核心持股應有明確配置'
      }
    },

    // === 質押狀態（Live in Loans）===
    {
      name: 'is_pledged',
      type: 'checkbox',
      defaultValue: false,
      admin: {
        description: '是否已質押？（Live in Loans 策略）'
      }
    },
    {
      name: 'pledged_percentage',
      type: 'number',
      admin: {
        condition: (data) => data.is_pledged,
        description: '質押比例 (%)，Allen 通常控制在 30-40%'
      }
    },
    {
      name: 'pledge_safety_margin',
      type: 'number',
      admin: {
        condition: (data) => data.is_pledged,
        description: '質押安全邊際 (%)，股價還能跌多少才會觸及維持率'
      }
    },

    // === 追蹤頻率 ===
    {
      name: 'last_reviewed_date',
      type: 'date',
      admin: {
        description: '最後一次深度檢視日期'
      }
    },
    {
      name: 'next_review_date',
      type: 'date',
      admin: {
        description: '下次預計檢視日期（如財報日）'
      }
    },
    {
      name: 'review_notes',
      type: 'richText',
      admin: {
        description: '最近一次檢視的備註'
      }
    },

    // === 時間戳 ===
    {
      name: 'created_at',
      type: 'date',
      admin: {
        readOnly: true
      }
    },
    {
      name: 'updated_at',
      type: 'date',
      admin: {
        readOnly: true
      }
    }
  ]
}
```

---

## 7. Integrity_Scores Collection (誠信評分歷史)

**用途**: 追蹤管理層誠信評分的動態變化

### Fields

```typescript
{
  slug: 'integrity_scores',
  fields: [
    // === 關聯 ===
    {
      name: 'company',
      type: 'relationship',
      relationTo: 'companies',
      required: true
    },

    // === 評分記錄 ===
    {
      name: 'score_date',
      type: 'date',
      required: true,
      admin: {
        description: '評分日期'
      }
    },
    {
      name: 'integrity_score',
      type: 'number',
      required: true,
      min: 0,
      max: 100,
      admin: {
        description: '誠信評分 (0-100%)'
      }
    },
    {
      name: 'score_change',
      type: 'number',
      admin: {
        description: '相較於上次評分的變化 (+/-)'
      }
    },

    // === 評分依據 ===
    {
      name: 'change_reason',
      type: 'richText',
      required: true,
      admin: {
        description: '評分變動的原因'
      }
    },
    {
      name: 'related_commitment',
      type: 'relationship',
      relationTo: 'commitments',
      admin: {
        description: '相關的承諾記錄（若因承諾達成/未達成而調整）'
      }
    },
    {
      name: 'related_event',
      type: 'relationship',
      relationTo: 'events',
      admin: {
        description: '觸發評分變動的事件'
      }
    },

    // === 時間戳 ===
    {
      name: 'created_at',
      type: 'date',
      admin: {
        readOnly: true
      }
    }
  ]
}
```

---

## 📊 Collection 關聯圖

```
Companies (公司主檔)
├── 1:N → Valuations (估值記錄)
├── 1:N → Financial_Data (財務數據)
├── 1:N → Events (重大事件)
├── 1:N → Commitments (承諾對帳單)
├── 1:N → Integrity_Scores (誠信評分歷史)
└── 1:1 → Watchlist (觀察名單)

Events (事件)
├── N:1 → Companies
└── 1:N → Commitments (某些事件包含承諾)

Commitments (承諾)
├── N:1 → Companies
├── N:1 → Events (承諾來源)
└── 1:1 → Integrity_Scores (影響誠信評分)
```

---

## 🎯 Schema 設計原則

### 1. **三層架構分離**
- **Framework Layer**：`Companies.moat_type`, `Companies.integrity_score` 等核心不變欄位
- **Perception Layer**：`Events`, `Financial_Data` 等可擴充的監測數據
- **Judgment Layer**：`Valuations.confidence_rationale`, `Commitments` 等人類決策記錄

### 2. **時間旅行能力**
- 所有 Collection 都保留 `created_at` 和 `updated_at`
- `Valuations` 完整記錄每次計算的輸入與輸出
- `Integrity_Scores` 追蹤誠信評分的動態變化

### 3. **預測對帳單**
- `Commitments` Collection 設計了 `commitment_date` → `target_date` → `actual_completion_date` 的完整生命週期
- `achievement_percentage` 用於量化管理層執行力
- 自動影響 `Integrity_Scores` 的評分

### 4. **強制執行 IVC 規範**
- `Valuations.iv_per_share_low` 和 `iv_per_share_high` 標記為 **強制項目** ⭐
- `market_price_at_valuation` 必填，避免「忽略現實」的錯誤
- `recommendation` 必填，確保每次估值都有明確決策建議

---

## 🚀 下一步：實作建議

### Phase 1: 核心 Collections（立即實作）
1. `Companies` - 公司主檔
2. `Valuations` - 估值記錄
3. `Financial_Data` - 財務數據

### Phase 2: 進階功能（P1）
4. `Events` - 事件追蹤
5. `Commitments` - 承諾對帳單
6. `Integrity_Scores` - 誠信評分

### Phase 3: 使用者功能（P2）
7. `Watchlist` - 觀察名單

---

## 📝 備註

- 所有金額欄位單位：**百萬**（Million）
- 所有百分比欄位單位：**%**（已轉換為 0-100 的數值）
- 日期格式：**ISO 8601** (YYYY-MM-DD)
- 幣別：預設 USD，可選 TWD/JPY/EUR

---

**Last Updated**: 2026-02-04
**Schema Version**: 1.0.0
**Maintained by**: Chi (AI Native Full-Stack Engineer)
