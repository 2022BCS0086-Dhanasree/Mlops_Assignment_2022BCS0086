import pandas as pd

def feature_engineering(df):

    df["tickets_30d"] = df["tenure"].apply(lambda x: 6 if x < 12 else 2)
    df["tickets_90d"] = df["tenure"].apply(lambda x: 10 if x < 12 else 4)
    df["tickets_7d"] = df["tenure"].apply(lambda x: 2 if x < 12 else 1)

    df["complaint_flag"] = df["InternetService"].apply(
        lambda x: 1 if x == "Fiber optic" else 0
    )

    df["charge_increase"] = df["MonthlyCharges"].apply(
        lambda x: 1 if x > 70 else 0
    )

    df["contract_encoded"] = df["Contract"].map({
        "Month-to-month": 0,
        "One year": 1,
        "Two year": 2
    })

    df["churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    return df