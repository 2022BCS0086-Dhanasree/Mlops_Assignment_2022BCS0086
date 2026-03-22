#  Telco Churn DevOps System

##  Student Details
Name: Dhanasree Gidijala  
Roll No: 2022BCS0086  

---

##  Objective
Build a rule-based churn prediction system using DevOps practices.

---

##  Dataset
Telco Customer Churn Dataset (Kaggle)

---

##  Rule-Based Logic

1. If tickets > 5 → HIGH RISK  
2. If charge increase + tickets ≥ 3 → MEDIUM RISK  
3. If contract = Month-to-Month + complaint → HIGH RISK  

Rules implemented in `rules.py`

---

## API

### Endpoint:
POST `/predict-risk`

### Example:
```json
{
  "customer_id": "7590-VHVEG"
}