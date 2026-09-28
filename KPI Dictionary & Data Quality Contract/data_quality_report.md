# Data Quality Profile Report

The report is based directly on the supplied raw retail-orders CSV and its supplied data dictionary.

| Dimension | Finding | Evidence |
|---|---|---|
| Completeness | Failed | Missing city, discount_pct, and order_date values are present |
| Uniqueness | Failed | RT-1004 appears twice |
| Date validity | Failed | RT-1006 has 2026-13-10; RT-1011 has a missing date |
| Quantity validity | Failed | RT-1006 has -1; RT-1008 contains text two |
| Discount validity | Failed | RT-1007 has 105% |
| Category normalization | Needs normalization | payment status contains paid as well as Paid; customer segment contains student as well as Student |
| Unit price | Pass | No negative unit prices are present |
| Freshness | Runtime check | Depends on the execution date |

The raw data should not be silently repaired. The executable checks identify records that need quarantine or source correction before critical sales KPIs are published.
