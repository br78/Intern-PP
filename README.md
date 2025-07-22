# Medicare Fraud Detection Using Machine Learning

This project detects fraudulent Medicare claims using a machine learning model and a Streamlit web app. It uses a dataset of prescriptions and costs, applies synthetic fraud injection, and trains a model to predict fraud.


# Source site of sample data:
 https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-provider?fbclid=IwY2xjawLsl0dleHRuA2FlbQIxMQABHkBpR745aU8rCiPm_88cmkgDQkS-sypEm8OmX92ifAmn_uq9089kVJewqhGM_aem_7XXkPOcIf4_2zDUCvhJTng 



##  Features Used

- Total Claims (Tot_Clms)
- Total Drug Cost (Tot_Drug_Cst)
- Generic Drug Cost (Gnrc_Tot_Drug_Cst)
- Brand Drug Cost (Brnd_Tot_Drug_Cst)
- Opioid Drug Cost (Opioid_Tot_Drug_Cst)
- Average Age of Beneficiaries (Bene_Avg_Age)
- Female and Male Beneficiary Counts (Bene_Feml_Cnt, Bene_Male_Cnt)


##  ML Models Used

- Logistic Regression
- Random Forest Classifier

Random Forest gave better accuracy and feature importance visualization.



##  How to Run

1. Clone the repo or download the files.

2. Install the required packages:
   ```bash
   pip install streamlit pandas scikit-learn matplotlib seaborn joblib
