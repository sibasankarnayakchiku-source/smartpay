def explain(reason=None):
    base_explanation = (
        "This advice is based on a transparent analysis of your income,"
        "spending patterns, category importance, and savings goals. "
        "No predictions or hidden models are used."
    )

    if reason:
        return f"{base_explanation}Specifically, {reason}."
    return base_explanation

if __name__ == "__main__":
    print(explain("your spending in entertainment is significantly higher than peers"))
    print(explain())