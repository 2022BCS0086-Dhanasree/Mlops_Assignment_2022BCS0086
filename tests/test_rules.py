# from app.rules import calculate_risk

# def test_high():
#     customer = {"Contract": "Month-to-month"}
#     ticket = {"tickets_last_30_days": 6, "complaint_flag": 1, "charge_increase": 1}
#     assert calculate_risk(customer, ticket) == "HIGH"

# def test_medium():
#     customer = {"Contract": "Two year"}
#     ticket = {"tickets_last_30_days": 3, "complaint_flag": 0, "charge_increase": 1}
#     assert calculate_risk(customer, ticket) == "MEDIUM"

# def test_low():
#     customer = {"Contract": "Two year"}
#     ticket = {"tickets_last_30_days": 1, "complaint_flag": 0, "charge_increase": 0}
#     assert calculate_risk(customer, ticket) == "LOW"

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ml_prediction():
    response = client.post("/predict-risk?customer_id=7590-VHVEG")
    assert response.status_code == 200