"""
Lab 2 - Environment/model definitions for the PEAS and classification task.

This file documents the simplified simulator assumptions used by lab2_check.py.
"""

DELIVERY_ROBOT = {
    "observability": "partially observable in the real environment",
    "determinism": "stochastic in the real environment",
    "notes": [
        "Sensors may not reveal every obstacle, pedestrian intention, or package state.",
        "Wheel slip, traffic, weather, and human behavior can make outcomes uncertain.",
    ],
}

STUDENT_SUPPORT_AGENT = {
    "observability": "partially observable in the real environment",
    "determinism": "stochastic in the real environment",
    "notes": [
        "The agent cannot directly observe all student intentions, emotions, or offline circumstances.",
        "Student responses, tool availability, and external events introduce uncertainty.",
    ],
}

SIMPLIFIED_SIMULATOR = {
    "delivery_robot": {
        "observability": "fully observable if the simulator exposes the complete state",
        "determinism": "deterministic if transition rules contain no random/noise component",
    },
    "student_support_agent": {
        "observability": "fully observable only in a toy simulator that exposes every relevant variable",
        "determinism": "deterministic only if student/tool responses are fixed by scripted transition rules",
    },
}
