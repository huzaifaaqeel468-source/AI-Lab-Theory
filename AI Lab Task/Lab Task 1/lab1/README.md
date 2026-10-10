# Lab 1 — Artificial Intelligence

## Contents

- `lab1_rules.py` — transparent rule-based scholarship evaluator and exactly four core tests.
- `lab1_compare.py` — demonstration comparing fluent conversational output with the transparent rule result.
- `input_data.csv` — reproducible inputs for the four core cases.
- `outputs/rules_output.txt` — captured output from `lab1_rules.py`.
- `outputs/compare_output.txt` — captured output from `lab1_compare.py`.
- `Lab1_Report.docx` — complete written report required by the lab.
- `Lab1_Report.pdf` — optional PDF copy for convenient viewing.

## Requirements

- Python 3.9 or later.
- No third-party Python packages are required to run the source code.

## Run

From the `lab1` directory:

```bash
python lab1_rules.py
python lab1_compare.py
```

The expected captured outputs are stored in `outputs/`.

## Reproducibility

The scholarship rule uses four explicit conditions:

1. `score >= 70`
2. documentation is complete
3. `attendance >= 80%`
4. `recommendation >= 3/5`

All thresholds are **synthetic lab assumptions** and are not presented as a real scholarship policy.

The four core cases deliberately cover:
- one pass,
- failure of the new attendance condition,
- failure of the new recommendation condition,
- exact threshold boundary behavior.

## Report

`Lab1_Report.docx` contains:
- sourced five-entry-plus AI timeline,
- assumptions and implementation choices,
- four rule tests and actual results,
- disagreement table,
- conversational-test comparison,
- failure/edge-case analysis,
- limitations,
- reflection,
- responsible-practice responses,
- references.

## Sources

Historical claims are supported in the report by academic/primary sources, including:
- Turing (1950), *Computing Machinery and Intelligence*.
- McCarthy et al. (1955), Dartmouth AI proposal.
- Weizenbaum (1966), ELIZA.
- Russell & Norvig (2021), *Artificial Intelligence: A Modern Approach*.
- Krizhevsky, Sutskever & Hinton (2012), AlexNet/ImageNet.
- Vaswani et al. (2017), Transformer architecture.
- Kaplan et al. (2020), scaling laws.
