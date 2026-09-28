# Task Completion Notes

## Decision owner
For this retail-order dataset, Sales Operations owns order-volume KPIs and Finance owns monetary/payment KPIs. Marketing owns discount-related monitoring.

## Final deliverables
- KPI_Dictionary.csv — 10 KPI definitions.
- Data_Quality_Contract.md — thresholds and escalation actions.
- profile_data.py — executable profiling script.
- data_quality_checks.py — executable contract checks.
- data_profile_notebook.ipynb — notebook proof.
- data_quality_report.md — observed raw-data issues.
- kpi_queries.sql — SQL calculation patterns.
- KPI_Calculations.csv — KPI calculation reference.

## Important observation
The source data is intentionally not rewritten. Duplicate, missing, malformed, and out-of-range values are surfaced by the quality checks so downstream reporting can make an explicit pass/fail decision.
