from pathlib import Path
import pandas as pd
import numpy as np
INPUT=Path("data/messy_customers.csv"); CLEANED=Path("output/cleaned_customers.csv"); REPORT=Path("output/cleaning_report.csv")
def clean_data(df):
    original_rows=len(df)
    df.columns=df.columns.str.strip().str.lower().str.replace(r"[^a-z0-9]+","_",regex=True).str.strip("_")
    for c in df.select_dtypes(include="object").columns:
        df[c]=df[c].astype("string").str.strip().replace({"":pd.NA,"N/A":pd.NA,"n/a":pd.NA,"NA":pd.NA,"null":pd.NA})
    df["name"]=df["name"].str.title(); df["city"]=df["city"].str.title(); df["email"]=df["email"].str.lower()
    df["age"]=pd.to_numeric(df["age"],errors="coerce"); df["salary"]=pd.to_numeric(df["salary"],errors="coerce")
    df.loc[(df["age"]<0)|(df["age"]>100),"age"]=np.nan
    bad=df["email"].notna() & ~df["email"].str.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$",na=False)
    df.loc[bad,"email"]=pd.NA
    df["join_date"]=pd.to_datetime(df["join_date"],errors="coerce",dayfirst=True)
    dup=int(df.duplicated().sum()); df=df.drop_duplicates().copy()
    df["age"]=df["age"].fillna(df["age"].median()); df["salary"]=df["salary"].fillna(df["salary"].median())
    df["city"]=df["city"].fillna("Unknown"); df["email"]=df["email"].fillna("unknown@email.com"); df["join_date"]=df["join_date"].fillna(pd.Timestamp("2000-01-01"))
    report=pd.DataFrame({"metric":["original_rows","final_rows","duplicates_removed","missing_values_after_cleaning"],"value":[original_rows,len(df),dup,int(df.isna().sum().sum())]})
    return df,report
def main():
    d=pd.read_csv(INPUT); c,r=clean_data(d); c["join_date"]=c["join_date"].dt.strftime("%Y-%m-%d"); c.to_csv(CLEANED,index=False); r.to_csv(REPORT,index=False); print(r.to_string(index=False))
if __name__=="__main__": main()
