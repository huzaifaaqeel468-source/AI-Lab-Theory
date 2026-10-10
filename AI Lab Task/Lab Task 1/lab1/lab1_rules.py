"""
Lab 1 - Transparent rule-based scholarship evaluator.

All thresholds in this lab are SYNTHETIC LAB ASSUMPTIONS and do not represent
a real university scholarship policy.

Run:
    python lab1_rules.py
"""

from dataclasses import dataclass


SCORE_THRESHOLD = 70
ATTENDANCE_THRESHOLD = 80
RECOMMENDATION_THRESHOLD = 3


@dataclass
class ScholarshipInput:
    score: int
    documents_complete: bool
    attendance: float
    recommendation: int


def evaluate_scholarship(applicant: ScholarshipInput):
    """Return PASS/FAIL and transparent reasons."""
    failures = []

    if applicant.score < SCORE_THRESHOLD:
        failures.append(f"score {applicant.score} < {SCORE_THRESHOLD}")

    if not applicant.documents_complete:
        failures.append("documentation incomplete")

    if applicant.attendance < ATTENDANCE_THRESHOLD:
        failures.append(
            f"attendance {applicant.attendance:g}% < {ATTENDANCE_THRESHOLD}%"
        )

    if applicant.recommendation < RECOMMENDATION_THRESHOLD:
        failures.append(
            f"recommendation {applicant.recommendation}/5 < "
            f"{RECOMMENDATION_THRESHOLD}/5"
        )

    if failures:
        return "FAIL", "; ".join(failures)

    return "PASS", "all four conditions satisfied"


# Exactly four core test cases required by the lab.
CORE_TEST_CASES = [
    {
        "name": "Case 1 - Pass",
        "input": ScholarshipInput(85, True, 90, 4),
        "expected": "PASS",
    },
    {
        "name": "Case 2 - Attendance failure",
        "input": ScholarshipInput(85, True, 79, 4),
        "expected": "FAIL",
    },
    {
        "name": "Case 3 - Recommendation failure",
        "input": ScholarshipInput(85, True, 90, 2),
        "expected": "FAIL",
    },
    {
        "name": "Case 4 - Threshold boundary",
        "input": ScholarshipInput(70, True, 80, 3),
        "expected": "PASS",
    },
]


def format_input(applicant: ScholarshipInput):
    return (
        f"score={applicant.score}, "
        f"documents_complete={applicant.documents_complete}, "
        f"attendance={applicant.attendance:g}%, "
        f"recommendation={applicant.recommendation}/5"
    )


def main():
    print("LAB 1 - RULE-BASED SCHOLARSHIP TEST")
    print("Assumption: all thresholds are synthetic lab assumptions.")
    print("Rules: score >= 70 AND documents complete AND attendance >= 80% "
          "AND recommendation >= 3/5")
    print()

    for case in CORE_TEST_CASES:
        actual, reason = evaluate_scholarship(case["input"])
        status = "OK" if actual == case["expected"] else "MISMATCH"
        print(case["name"])
        print(f"  Input:    {format_input(case['input'])}")
        print(f"  Expected: {case['expected']}")
        print(f"  Actual:   {actual}")
        print(f"  Reason:   {reason}")
        print(f"  Check:    {status}")
        print()

    print("Selection rationale:")
    print("  Case 1 is a positive control (normal pass).")
    print("  Case 2 isolates the new attendance condition.")
    print("  Case 3 isolates the new recommendation condition.")
    print("  Case 4 checks inclusive >= behavior exactly at all thresholds.")


if __name__ == "__main__":
    main()
