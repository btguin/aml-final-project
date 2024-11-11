import streamlit as st
import pandas as pd
from insurance_data_parser import extract_vehicle_insurance_info, VehicleInsurance
from typing import Optional
DATA_PATH = '../../data/'

# Load the dataset
FILE_PATH = f"{DATA_PATH}/raw/Insurance claims data.csv"
insurance_data = pd.read_csv(FILE_PATH)

st.write("""
# Claim Predictor
Predicts the **Claim Likelihood** of a vehicle insurance claim!
""")
st.write("## Reference Data")
st.dataframe(insurance_data)

st.write("## Claim Description")
claim_description = st.text_area("Type `Claim description` below:", "Customer age 50, has a 2.5 year old petrol car with a 12 month subscription.")

if st.button("Extract"):
    insurance_info: Optional[VehicleInsurance] = extract_vehicle_insurance_info(claim_description)
    if insurance_info is not None:
        st.write("## Extracted Information")
        st.write("Subscription Length:", insurance_info.subscription_length)
        st.write("Vehicle Age:", insurance_info.vehicle_age)
        st.write("Customer Age:", insurance_info.customer_age)
        st.write("Fuel Type:", f"`{insurance_info.fuel_type}`")
    else:
        st.error("Could not extract insurance information from the description")