# AI Lab 3 Submission

## Overview
This repository contains the complete AI Lab 3 work for BFS, DFS, DLS, IDDFS, and UCS.

## Requirements
- Python 3.9 or later
- No third-party packages are required.

## Folder Structure
```text
lab3/
├── lab3_bfs_dfs.py
├── lab3_depth_search.py
├── lab3_ucs.py
├── input_data.csv
├── README.md
├── Lab3_Report.docx
└── outputs/
    ├── bfs_dfs_trace.txt
    ├── depth_search_output.txt
    └── ucs_output.txt
```

## Run Commands
```bash
python lab3_bfs_dfs.py
python lab3_depth_search.py
python lab3_ucs.py
```

## Graph Assumption
The supplied A-G graph was represented with this successor order:
A: B, C
B: D, E
C: F
D: G
E: G
F: G
G: no successors

This order is preserved in the traces and code. If the instructor's Section 3.2 graph uses different edges/order, the supplied course graph should replace this explicitly documented equivalent.

## DLS / IDDFS
The root A is counted at depth 0. DLS distinguishes:
- FOUND: goal is reached within the depth limit.
- CUTOFF: no solution was found before the limit, but search reached the limit.
- FAILURE: no solution exists in the explored search space without a cutoff.

A path-local cycle check prevents revisiting a node already on the current path.

## Weighted UCS
The weighted version uses the same topology with the following weights:
A-B=1, A-C=2, B-D=1, B-E=8, C-F=1, D-G=10, E-G=1, F-G=1.

UCS returns the minimum-cost route. The report independently sums the selected path's edge weights and compares UCS with BFS on the same weighted topology.

## Reproducibility
Captured outputs are stored in `outputs/`. The report includes manual traces, results, weighted graph details, cost verification, limitations, edge-case analysis, reflection, and responsible-practice discussion.
