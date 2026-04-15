import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from pipeline import feature_engineering
df = pd.read_csv("app/data/telco.csv")
df = feature_engineering(df)
features = [
    "tickets_7d",
    "tickets_30d",
    "tickets_90d",
    "complaint_flag",
    "charge_increase",
    "contract_encoded"
]
X = df[features]
y = df["churn"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)
joblib.dump(model, "ml/model.pkl")
print("Model trained and saved!")