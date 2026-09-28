# Data Cleaning Automation
A Python + Streamlit project that automatically cleans and validates messy tabular data.

## Features
- CSV upload
- Column and text standardization
- Missing-value handling
- Numeric conversion and validation
- Email validation
- Date conversion
- Duplicate removal
- Median imputation
- Cleaning report
- Cleaned CSV download

## Run
```bash
pip install -r requirements.txt
python run_cleaning.py
streamlit run app.py
```

## Workflow
Raw CSV -> Standardize -> Validate -> Remove duplicates -> Fill missing values -> Clean CSV + Report

## Future Enhancements
Excel/JSON support, outlier detection, data-quality scoring, database integration, Airflow scheduling, cloud ETL and anomaly detection.

## Author
Shaik Sofiya

Educational project; review cleaning rules before production use.
