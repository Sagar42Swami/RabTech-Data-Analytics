# Data Quality Contract

## Scope
This contract applies to the supplied retail orders dataset and uses the quality rules in the supplied retail data dictionary.

| Dimension | Check | Target | Failure threshold | Action |
|---|---|---:|---:|---|
| Completeness | Required fields populated | 100% | Any required-field null | Quarantine affected records; notify data owner |
| Uniqueness | order_id unique | 100% | Any duplicate order_id | Block KPI publication; investigate duplicate source rows |
| Validity | order_date valid ISO date and not future | 100% | Any invalid date | Quarantine affected records |
| Validity | quantity is whole number greater than zero | 100% | Any violation | Block sales KPIs |
| Validity | discount_pct is 0 to 100 | 100% | Any violation | Quarantine affected records |
| Validity | payment_status allowed after normalization | 100% | Any unmapped value | Escalate to data owner |
| Validity | customer_segment allowed after normalization | 100% | Any unmapped value | Escalate to data owner |
| Consistency | unit_price non-negative | 100% | Any negative value | Block revenue calculation |
| Freshness | Latest order_date current enough for daily reporting | Daily | More than 24h stale | Alert pipeline owner |

## Severity
- Critical: uniqueness or revenue-field validity failure. KPI publication is blocked.
- High: required-field completeness or invalid categorical value. Affected records are quarantined.
- Medium: freshness breach or other non-financial quality issue.

## Escalation
1. Automated check records the failed rule and affected rows.
2. Data owner is notified with rule, count, and sample order IDs.
3. Critical failures block downstream KPI publication.
4. After correction, rerun checks and document the result.

The raw CSV is preserved and is not silently modified.
