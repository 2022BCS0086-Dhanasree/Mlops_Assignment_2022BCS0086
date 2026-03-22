def calculate_risk(customer, ticket):
    tickets = int(ticket["tickets_last_30_days"])
    complaint = int(ticket["complaint_flag"])
    charge_increase = int(ticket["charge_increase"])
    contract = customer["Contract"]

    if tickets > 5:
        return "HIGH"

    if charge_increase == 1 and tickets >= 3:
        return "MEDIUM"

    if contract == "Month-to-month" and complaint == 1:
        return "HIGH"

    return "LOW"