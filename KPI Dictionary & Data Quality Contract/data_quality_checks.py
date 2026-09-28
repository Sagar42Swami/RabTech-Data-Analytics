from pathlib import Path
import pandas as pd

BASE=Path(__file__).resolve().parent
DATA=BASE/"retail-orders-raw (1).csv"

def check(label,passed,detail):
    print(f"[{"PASS" if passed else "FAIL"}] {label}: {detail}")

def main():
    df=pd.read_csv(DATA)
    required=["order_id","order_date","customer_segment","city","category","quantity","unit_price","discount_pct","payment_status"]
    missing=int(df[required].isna().sum().sum())
    check("Completeness",missing==0,f"{missing} required-field null cells")
    dup=int(df["order_id"].duplicated(keep=False).sum())
    check("Uniqueness",dup==0,f"{dup} rows have duplicated order_id values")
    dates=pd.to_datetime(df["order_date"],errors="coerce")
    bad_dates=int(dates.isna().sum())
    check("Date validity",bad_dates==0,f"{bad_dates} invalid/unparseable dates")
    qty=pd.to_numeric(df["quantity"],errors="coerce")
    bad_qty=int((qty.isna()|(qty<=0)|(qty%1!=0)).sum())
    check("Quantity validity",bad_qty==0,f"{bad_qty} invalid quantity values")
    discount=pd.to_numeric(df["discount_pct"],errors="coerce")
    bad_discount=int(((discount<0)|(discount>100)).sum())
    check("Discount validity",bad_discount==0,f"{bad_discount} out-of-range discounts")
    seg=df["customer_segment"].dropna().astype(str).str.strip().str.lower()
    check("Customer segment",int((~seg.isin({"student","fresher","professional"})).sum())==0,"values normalized to allowed set")
    status=df["payment_status"].dropna().astype(str).str.strip().str.lower()
    check("Payment status",int((~status.isin({"paid","pending","failed","refunded"})).sum())==0,"values normalized to allowed set")
    prices=pd.to_numeric(df["unit_price"],errors="coerce")
    check("Unit price",int((prices<0).sum())==0,f"{int((prices<0).sum())} negative unit prices")
    latest=dates.dropna().max()
    age=(pd.Timestamp.today().normalize()-latest.normalize()).days
    check("Freshness",age<=1,f"latest valid order date is {latest.date()} ({age} days old)")
    print("\nContract result: KPI publication should be BLOCKED when any Critical rule fails.")

if __name__=="__main__":
    main()
