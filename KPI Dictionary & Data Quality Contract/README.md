# KPI Dictionary & Data Quality Contract

## Objective
Translate the retail business request into measurable KPIs and a testable agreement for trustworthy data.

## Source data
- retail-orders-raw (1).csv
- retail-data-dictionary (1).csv

## Deliverables
1. KPI dictionary with formulas, grain, filters, owners, and refresh cadence.
2. Data quality contract with thresholds and escalation actions.
3. Executable Python profiling and quality checks.
4. SQL KPI examples.
5. Profile report and notebook.

## Quality dimensions
Completeness, uniqueness, validity, consistency, and freshness.

## Run
pip install -r req.txt
python data_quality_checks.py
python profile_data.py

The scripts report findings and do not overwrite the raw dataset.
