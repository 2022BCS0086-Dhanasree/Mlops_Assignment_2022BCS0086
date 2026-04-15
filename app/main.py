from fastapi import FastAPI
import pandas as pd
import joblib
from app.logger import logger

app = FastAPI()

# Load model
model = joblib.load("ml/model.pkl")

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
    print("INPUT ID:", customer_id)

    print("AVAILABLE IDs SAMPLE:")
    print(customers["customerID"].head())

    try:
        customer = customers[
            customers["customerID"].str.strip() == str(customer_id).strip()
        ]

        print("MATCH FOUND:", customer)

        customer = customer.iloc[0]

        # ✅ Contract Encoding
        contract_map = {
            "Month-to-month": 0,
            "One year": 1,
            "Two year": 2
        }

        contract_encoded = contract_map.get(customer["Contract"], 0)

        # ✅ Feature vector
        features = [
            customer["tickets_last_30_days"],
            customer["complaint_flag"],
            customer["charge_increase"],
            contract_encoded
        ]

        # ✅ Prediction
        # prediction = model.predict([features])[0]
        import pandas as pd

        input_df = pd.DataFrame([{
            "tickets_7d": customer["tickets_last_30_days"] // 3,
            "tickets_30d": customer["tickets_last_30_days"],
            "tickets_90d": customer["tickets_last_30_days"] * 2,
            "complaint_flag": customer["complaint_flag"],
            "charge_increase": customer["charge_increase"],
            "contract_encoded": 0 if customer["Contract"] == "Month-to-month" else 1
        }])

        prediction = model.predict(input_df)[0]
        risk = "HIGH" if prediction == 1 else "LOW"

        logger.info(
            f"Dhanasree Gidijala | 2022BCS0086 | {customer_id} → {risk}"
        )

        return {
            "customer_id": customer_id,
            "risk": risk,
            "evaluated_by": "Dhanasree Gidijala",
            "roll_no": "2022BCS0086"
        }

    except Exception as e:
        logger.error(str(e))
        return {"error": "Customer not found"}