from fastapi import FastAPI
import pandas as pd
from app.rules import calculate_risk
from app.logger import logger

app = FastAPI()

# Load dataset
customers = pd.read_csv("app/data/telco.csv")

# Simulate ticket behavior
customers["tickets_last_30_days"] = customers["tenure"].apply(
    lambda x: 6 if x < 12 else 2
)

customers["complaint_flag"] = customers["InternetService"].apply(
    lambda x: 1 if x == "Fiber optic" else 0
)

customers["charge_increase"] = customers["MonthlyCharges"].apply(
    lambda x: 1 if x > 70 else 0
)

@app.get("/")
def home():
    return {
        "message": "Telco DevOps System Running",
        "name": "Dhanasree Gidijala",
        "roll_no": "2022BCS0086"
    }

@app.post("/predict-risk")
def predict(customer_id: str):
    try:
        customer = customers[customers["customerID"] == customer_id].iloc[0]

        ticket = {
            "tickets_last_30_days": customer["tickets_last_30_days"],
            "complaint_flag": customer["complaint_flag"],
            "charge_increase": customer["charge_increase"]
        }

        risk = calculate_risk(customer, ticket)

        logger.info(
            f"Dhanasree Gidijala | 2022BCS0086 | {customer_id} → {risk}"
        )

        return {
            "customer_id": customer_id,
            "risk": risk,
            "evaluated_by": "Dhanasree Gidijala",
            "roll_no": "2022BCS0086"
        }

    except:
        return {"error": "Customer not found"}