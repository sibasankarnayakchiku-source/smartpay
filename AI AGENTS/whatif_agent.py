def what_if(money_spend, reduction_percent):
    if money_spend<0:
        return "Spending cannot be negative."
    if reduction_percent<0 or reduction_percent>100:
        return"Reduction percent must between 0 to 100."
    
    new_spend = money_spend*(1-reduction_percent / 100)
    savings_gain = money_spend - new_spend

    explanation = (
        f"If you reduce money spent by {reduction_percent:.1f}%,"
        f"your money spend will reduce from {money_spend:.0f} to {new_spend:.0f}."
        f"This frees up approximately {savings_gain:.0f} that can go toward savings."
    )
    return explanation

if __name__ == "__main__":
    print(what_if(2000,15))
    print(what_if(1500,25))