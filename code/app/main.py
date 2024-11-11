import streamlit as st
import pandas as pd
from insurance_data_parser import extract_vehicle_insurance_info, VehicleInsurance
from typing import Optional
import io

dummy_data = """
policy_id,subscription_length,vehicle_age,customer_age,region_code,region_density,segment,model,fuel_type,max_torque
POL045360,9.3,1.2,41,C8,8794,C2,M4,Diesel,250Nm@2750rpm
POL016745,8.2,1.8,35,C2,27003,C1,M9,Diesel,200Nm@1750rpm
POL007194,9.5,0.2,44,C8,8794,C2,M4,Diesel,250Nm@2750rpm
POL018146,5.2,0.4,44,C10,73430,A,M1,CNG,60Nm@3500rpm
POL049011,10.1,1.0,56,C13,5410,B2,M5,Diesel,200Nm@3000rpm
POL053680,3.1,2.0,36,C7,6112,B2,M7,Petrol,113Nm@4400rpm
POL053943,4.5,2.4,38,C2,27003,C2,M4,Diesel,250Nm@2750rpm
POL002857,10.7,2.0,56,C2,27003,B2,M6,Petrol,113Nm@4400rpm
POL028225,10.7,0.6,55,C5,34738,B1,M8,CNG,82.1Nm@3400rpm
POL047631,0.3,2.4,45,C3,4076,B2,M6,Petrol,113Nm@4400rpm
"""
# read csv
dummy_df = pd.read_csv(io.StringIO(dummy_data))

st.write("""
# Claim Predictor
Predicts the **Claim Likelihood** of a vehicle insurance claim!
""")
st.write("## Reference Data")
st.dataframe(dummy_df)

st.write("## Claim Description")
claim_description = st.text_area("Type `Claim description` below:", "Customer age 50, has a 2.5 year old petrol car with a 12 month subscription.")

if st.button("Extract"):
    insurance_info: Optional[VehicleInsurance] = extract_vehicle_insurance_info(claim_description)
    if insurance_info is not None:
        # Create two columns
        col1, col2 = st.columns(2)
        
        # Column 1: Extracted Information
        with col1:
            st.write("## Extracted Information")
            st.write("Subscription Length:", insurance_info.subscription_length)
            st.write("Vehicle Age:", insurance_info.vehicle_age)
            st.write("Customer Age:", insurance_info.customer_age)
            st.write("Fuel Type:", f"`{insurance_info.fuel_type}`")
        
        # Column 2: Prediction
        with col2:
            st.write("## Prediction")
            dummy_prediction = 0.75  # Dummy prediction value
            if dummy_prediction > 0.5:
                st.metric(
                    label="Claim Likelihood",
                    value=f"{dummy_prediction:.1%}",
                    delta="High Risk",
                    delta_color="inverse"  # This will make the delta red
                )
            else:
                st.metric(
                    label="Claim Likelihood",
                    value=f"{dummy_prediction:.1%}",
                    delta="Low Risk"
                )
    else:
        st.error("Could not extract insurance information from the description")