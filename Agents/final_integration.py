# Importing individual agents
from peer_comparison_agent import peer_compare
from justification_agent import justification
from regret_agent import regret
from whatif_agent import what_if
from explanation_agent import explain


def final_judgment_engine(
    income,
    total_spend,
    category,
    category_spend,
    peer_average,
    what_if_reduction=None
):

    # Peer comparison
    peer_insight = peer_compare(
        category_spend,
        peer_average,
        category
    )

    # Justification scoring
    justification_insight = justification(category)

    # Regret minimization
    regret_insight = regret(
        income,
        total_spend,
        savings_goal_percent=20
    )

    # What-If simulation
    what_if_insight = None
    if what_if_reduction is not None:
        what_if_insight = what_if(
            category_spend,
            what_if_reduction
        )

    # Explanation
    explanation_text = explain(
        "income, spending behavior, category importance, savings health, "
        "and optional scenario simulations were evaluated"
    )

    result = {
        "peer_insight": peer_insight,
        "justification_insight": justification_insight,
        "regret_insight": regret_insight,
        "what_if_insight": what_if_insight,
        "explanation": explanation_text
    }

    return result

if __name__ == "__main__":
    demo_output = final_judgment_engine(
        income=50000,
        total_spend=42000,
        category="shopping",
        category_spend=8000,
        peer_average=5000,
        what_if_reduction=20
    )

    for key, value in demo_output.items():
        print(f"{key.upper()}:\n{value}\n")
