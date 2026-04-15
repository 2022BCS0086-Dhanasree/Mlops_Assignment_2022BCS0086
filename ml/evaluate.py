from sklearn.metrics import f1_score, roc_auc_score, precision_score
import joblib

model = joblib.load("ml/model.pkl")

# Dummy example (you can improve later)
print("Model loaded successfully")