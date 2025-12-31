def peer_compare(user_value, average_value, category = "spending"):
    if average_value == 0:
        return "Peer average data is unavailable for comparison"
    
    difference = user_value - average_value

    percentage_diff = (difference/average_value)*100

    if percentage_diff > 20 :
        return (f"Your {category} is {percentage_diff:.1f}% higher than similiar users."
        f"This is significantly higher and may lead to overspending.")

    elif percentage_diff > 10:
        return (f"Your {category} is {percentage_diff:.1f}% higher than peer average."
        f"You may want to keep an eye on this.")

    else:
        return (f"Your {category} is within the normal range compared to similar users."
        f"Nice work mainatining your spending!")

if __name__ == "__main__":
    print(peer_compare(5000,3000,"grocery spending"))
    print(peer_compare(5000,2000,"stationary spending"))


