# Lab 2 — Artificial Intelligence

## Files

- `lab2_percepts.py` — stateful temperature/occupancy controller. It remembers the previous target mode and returns the target plus whether a command should be sent.
- `lab2_model.py` — environment classifications and simulator assumptions.
- `lab2_check.py` — reproducible checks and complete mode-transition trace.
- `input_data.csv` — trace inputs.
- `outputs/lab2_check_output.txt` — captured execution output.
- `Lab2_Report.docx` — required report.
- `Lab2_Report.pdf` — optional PDF copy.

## Requirements

Python 3.9+; no third-party packages are required to run the Python source.

## Run

```bash
python lab2_check.py
```

## Controller assumptions

The lab controller uses these explicit thresholds:
- Temperature < 18°C → `HEAT`
- Temperature > 24°C → `COOL`
- 18°C ≤ temperature ≤ 24°C → `OFF`
- Occupancy = 0 has priority and forces `OFF`

These thresholds and priority rules are treated as the existing lab assumptions for this implementation. If the instructor supplied different original thresholds, replace the constants/rules with those exact values before submission.

The stateful extension stores `previous_mode`. It returns:
- the new target mode, and
- `SEND` when the target differs from the previous mode,
- `NO-COMMAND` when the target is identical.

## Test coverage

The trace contains:
1. repeated percepts,
2. exact lower boundary (18°C),
3. exact upper boundary (24°C),
4. a transition to HEAT,
5. a transition to COOL,
6. an empty-room case with occupancy priority.

## Submission

Commit the `lab2/` folder to GitHub. Submit the repository URL and final commit identifier through the course submission channel. Do not commit credentials, private data, or virtual environments.
