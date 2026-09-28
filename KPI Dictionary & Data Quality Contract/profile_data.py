from pathlib import Path
import pandas as pd

BASE=Path(__file__).resolve().parent
DATA=BASE/"retail-orders-raw (1).csv"

def main():
    df=pd.read_csv(DATA)
    print("Rows:",len(df))
    print("Columns:",len(df.columns))
    print("\nMissing values:")
    print(df.isna().sum().to_string())
    print("\nDuplicate order IDs:",int(df["order_id"].duplicated(keep=False).sum()))
    dates=pd.to_datetime(df["order_date"],errors="coerce")
    print("\nInvalid/unparseable dates:",int(dates.isna().sum()))
    print("Future dates:",int((dates>pd.Timestamp.today().normalize()).sum()))
    for col in ["customer_segment","category","payment_status"]:
        print(f"{col}:",sorted(df[col].dropna().astype(str).unique().tolist()))
if __name__=="__main__":
    main()
