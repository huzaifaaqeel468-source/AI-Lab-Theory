"""
Lab 1 - Comparison of transparent rule evaluation and conversational evaluation.

This script does not claim that a real conversational model is being trained.
It demonstrates why fluent dialogue is not sufficient evidence of reliable
general intelligence using the scholarship case.

Run:
    python lab1_compare.py
"""

from lab1_rules import ScholarshipInput, evaluate_scholarship


def conversational_style_answer(applicant: ScholarshipInput):
    """
    Deliberately simplified example of a fluent but incomplete answer.
    It illustrates the evaluation problem; it is NOT a real LLM.
    """
    if applicant.score >= 70 and applicant.attendance >= 80:
        return (
            "You appear to meet the main academic requirements, so you "
            "should qualify for the scholarship."
        )

    return "Your academic figures do not meet the stated minimums."


def correct_rule_answer(applicant: ScholarshipInput):
    result, reason = evaluate_scholarship(applicant)
    return f"{result}: {reason}"


def main():
    applicant = ScholarshipInput(
        score=70,
        documents_complete=True,
        attendance=80,
        recommendation=2,
    )

    print("LAB 1 - CONVERSATIONAL TEST COMPARISON")
    print()
    print("Scholarship input:")
    print(f"  score={applicant.score}")
    print(f"  documents_complete={applicant.documents_complete}")
    print(f"  attendance={applicant.attendance}%")
    print(f"  recommendation={applicant.recommendation}/5")
    print()

    print("Conversational-style response:")
    print(" ", conversational_style_answer(applicant))
    print()
    print("Transparent rule-based result:")
    print(" ", correct_rule_answer(applicant))
    print()
    print("Observation:")
    print("  The conversational response is fluent and plausible, but it misses")
    print("  the recommendation requirement. Fluent language therefore does not")
    print("  by itself prove reliable reasoning or general intelligence.")


if __name__ == "__main__":
    main()
