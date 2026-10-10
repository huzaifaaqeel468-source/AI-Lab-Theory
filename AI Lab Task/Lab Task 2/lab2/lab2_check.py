"""
Lab 2 - Reproducible checks and complete state-transition trace.

Run:
    python lab2_check.py
"""

from lab2_percepts import StatefulController, format_percept
from lab2_model import DELIVERY_ROBOT, STUDENT_SUPPORT_AGENT, SIMPLIFIED_SIMULATOR


TRACE = [
    # Repeated percept: first command, then suppressed duplicate.
    (20, 1, "repeated percept / initial"),
    (20, 1, "repeated percept / duplicate"),

    # Exact boundaries.
    (18, 1, "exact lower temperature boundary"),
    (24, 1, "exact upper temperature boundary"),

    # Mode transition.
    (17, 1, "transition to HEAT"),
    (25, 1, "transition to COOL"),

    # Empty room case with occupancy priority.
    (25, 0, "empty room / occupancy priority"),
]


def run_trace():
    controller = StatefulController()
    rows = []

    for temperature, occupancy, label in TRACE:
        target, should_send, previous = controller.step(temperature, occupancy)
        rows.append({
            "label": label,
            "previous": previous,
            "temperature": temperature,
            "occupancy": occupancy,
            "target": target,
            "command": "SEND" if should_send else "NO-COMMAND",
        })

    return rows


def main():
    print("LAB 2 - STATEFUL CONTROL CHECK")
    print("Thresholds: HEAT below 18C; COOL above 24C; occupancy=0 has priority -> OFF")
    print()

    print("Environment classifications:")
    print("  Delivery robot:", DELIVERY_ROBOT["observability"], ";", DELIVERY_ROBOT["determinism"])
    print("  Student-support agent:", STUDENT_SUPPORT_AGENT["observability"], ";",
          STUDENT_SUPPORT_AGENT["determinism"])
    print("  Simulator qualification:", SIMPLIFIED_SIMULATOR["delivery_robot"]["observability"],
          "and", SIMPLIFIED_SIMULATOR["delivery_robot"]["determinism"])
    print()

    print("Complete mode-transition trace:")
    print("Step | Previous | Percept | Target | Command | Purpose")
    print("-" * 86)
    for i, row in enumerate(run_trace(), start=1):
        percept = format_percept(row["temperature"], row["occupancy"])
        print(
            f"{i:>4} | {str(row['previous']):>8} | "
            f"{percept:<34} | {row['target']:<6} | "
            f"{row['command']:<10} | {row['label']}"
        )

    print()
    print("Check: repeated identical percepts suppress duplicate commands.")
    print("Check: exact 18C and 24C boundaries produce OFF under strict < and > rules.")
    print("Check: temperature mode transitions produce a new command.")
    print("Check: empty room forces OFF regardless of temperature.")


if __name__ == "__main__":
    main()
