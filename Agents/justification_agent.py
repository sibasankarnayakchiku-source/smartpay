def justification (category):
    score_table = {
        "rent": 10,
        "groceries": 8,
        "education": 9,
        "healthcare": 9,
        "transport": 7,
        "utilities": 7,
        "savings": 10,
        "entertainment": 4,
        "shopping": 3,
        "subscriptions": 4,
        "travel": 5,
        "luxury": 2
    }

    category = category.lower()
    score = score_table.get(category, 5)

    if score>=8:
       return( f"{category.capitalize( )} is a high-priority expense."
        f"Spending money is ju  stified and has lower negative impact on savings.")

    elif score>=5:
       return (f"{category.capitalize()} is a moderate-priority expense."
        f"It is reasonable but frequent spending can should be monitored.")

    else:
        return (f"{category.capitalize()} is a low-priority expense."
        f"Spending money here is less justified and can negatively impact savings.")

if __name__ == "__main__":
    print(justification("rent"))
    print(justification("entertainment"))