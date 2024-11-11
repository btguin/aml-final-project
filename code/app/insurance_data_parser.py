from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv
from typing import Optional
from datetime import date
load_dotenv()
api_key = os.getenv("OPEN_AI_API_KEY")

client = OpenAI(api_key=api_key)
today_date = date.today().isoformat()

class VehicleInsurance(BaseModel):
    subscription_length: int
    vehicle_age: float
    customer_age: int
    fuel_type: str

def extract_vehicle_insurance_info(text, data_structure=VehicleInsurance):
    completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",  # Updated to latest model
    messages=[
        {"role": "system", "content": f"Extract the vehicle insurance information from the following text. Today's date is {today_date}"},
        {"role": "user", "content": f"Input Text: ```{text}```"},
    ],
    response_format=data_structure
    )
    return completion.choices[0].message.parsed


print(type(extract_vehicle_insurance_info("Customer born April 7 1998, has a 2.5 year old petrol car with a 12 month subscription.")))