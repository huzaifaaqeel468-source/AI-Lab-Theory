# AI Lab 4 Submission

## Overview
This package contains the Lab 4 work for A* heuristic auditing, UCS comparison, and a controlled heuristic overestimate experiment.

## Requirements
- Python 3.9+
- No third-party packages

## Structure
```text
lab4/
├── lab4_astar_audit.py
├── input_data.csv
├── README.md
├── Lab4_Report.docx
└── outputs/
    └── lab4_output.txt
```

## Run
```bash
python lab4_astar_audit.py
```

## Graph and Heuristic Assumption
The task prompt refers to a supplied campus graph and heuristic table, but those materials were not included in the supplied message. For reproducibility, this submission uses the following documented equivalent graph:

S-A=2, S-B=4, A-C=2, A-D=5, B-C=1, B-D=2, C-G=5, D-G=2.

Successor order is exactly the order listed in the code.

Heuristic:
h(S)=7, h(A)=6, h(B)=4, h(C)=5, h(D)=2, h(G)=0.

If the course's Section graph/heuristic differs, replace these values with the instructor-supplied originals before final submission.

## Experiments
1. First three A* expansions with g, h, f and remaining frontier.
2. A* versus zero-heuristic UCS on identical topology.
3. Single-value overestimate experiment: h(C) changed from 5 to 10.

The report independently sums returned path costs and records processed/expanded nodes.

## Reproducibility
Captured output is in `outputs/lab4_output.txt`. The report documents assumptions, calculations, comparisons, limitations, an edge case, reflection, and responsible practice.
