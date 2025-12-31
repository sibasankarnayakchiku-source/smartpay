def regret(income, total_spend, savings_goal_percent = 20):
    if income<=0:
        return "Income data is unavailable."
    
    savings = income - total_spend
    savings_percent = (savings/income)*100

    if savings<=0:
        return ("Your spending currently leaves no savings. This may lead to financial stress. Consider reducing non-essential expenses")
    
    elif savings_percent < savings_goal_percent:
        return (f"Your savings are {savings_percent:.1f}% of your income"
                f"which is below recommended {savings_goal_percent:.1f}%."
                f"Small adjustments now can help avoid future regret.")
    else:
        return(f"Your savings are {savings_percent:.1f}% of your income."
               f"This is a healthy level and supports long-term financial stability.")
    
if __name__== "__main__":
    print(regret(-5000,4500,20))
    print(regret(-5000,3000,20))
    print(regret(5000,3000,20))