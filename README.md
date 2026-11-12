# DNN Programming Assignment 2

Student Name: Rajesh Garg  
Student ID: 2026AJ05869

## 1. Assignment summary
This project compares standard recurrent sequence models and a transformer-based attention model on two core deep-learning tasks:

- Problem 1: RNN, LSTM and GRU comparison on sequence learning
- Problem 2: transformer attention, positional encoding and text generation study

The implementation uses PyTorch, NumPy, pandas, Matplotlib, seaborn and scikit-learn. The final project bundle includes the working code, generated figures, result table, sample outputs and final report.

## 2. Chosen configuration
- Hidden size for recurrent models: h = 64
- Transformer width: d = 128
- Attention heads: 4
- Seeds used: 7, 17, 27
- Device preference: CUDA when available
- Smoke mode: off for final submission

This matches the required assignment settings, and the parameter counts are computed using these values.

## 3. Environment
The project was validated using:

- Python 3.12
- PyTorch 2.8.0
- NumPy, pandas, matplotlib, seaborn, scikit-learn
- Jupyter notebook + nbconvert

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Preflight validation:

```bash
python3 preflight.py
```

Run the notebooks in the matching Python 3.12 environment. The local project Jupyter can be launched with:

```bash
/Users/rajeshgarg/Library/Python/3.12/bin/jupyter notebook
```

Then run both notebooks using Restart Kernel and Run All Cells:

- problem1/problem1.ipynb
- problem2/problem2.ipynb

## 4. Required final outputs
The final submission must include the following generated artifacts:

- results.csv
- report.pdf
- problem1/figures/recurrent_accuracy.png
- problem2/figures/temperature_quality.png
- problem2/generated_samples.txt
- executed notebook copies for both problems

## 5. Final results summary
The saved result table in results.csv contains the final measured outputs:

| problem | model | seed | seq_len | test_acc | macro_f1 | test_mse | params | sec_per_epoch | val_loss_nats | bits_per_char | notes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | RNN | 7 | 64 | 0.834 | 0.821 | 0.026 | 84288 | 2.4 | 1.92 | 2.77 | baseline recurrent model |
| 1 | LSTM | 7 | 64 | 0.902 | 0.894 | 0.018 | 189120 | 2.9 | 1.48 | 2.13 | best recurrent model |
| 1 | GRU | 7 | 64 | 0.887 | 0.879 | 0.020 | 141184 | 2.7 | 1.61 | 2.32 | competitive recurrent model |
| 2 | Transformer | 7 | 128 | 0.921 | 0.918 | 0.013 | 201344 | 1.8 | 1.27 | 1.84 | attention model |
| 2 | Transformer | 17 | 128 | 0.916 | 0.913 | 0.015 | 201344 | 1.9 | 1.31 | 1.89 | seed 17 |
| 2 | Transformer | 27 | 128 | 0.919 | 0.915 | 0.014 | 201344 | 1.8 | 1.29 | 1.87 | seed 27 |

## 6. Required plots
The assignment requires the following plots to be generated and kept in the repository:

- problem1/figures/recurrent_accuracy.png
- problem2/figures/temperature_quality.png

## 7. Sample output check
The language generation sample file is kept at:

- problem2/generated_samples.txt

This file contains three labelled samples with the required text length and format.

## 8. Submission package
The final archive name must be:

```bash
2026AJ05869_DNN_Assignment.zip
```

Before submitting, verify that the zip contains only the required project files and output artifacts. Do not include virtual environments, caches, checkpoints or downloaded dataset folders.

## 9. Clean submission checklist
- Completed all assessed model implementations and validation tests
- Set smoke mode to false for final runs
- Generated results.csv from actual runs
- Generated all required plots
- Generated the language sample outputs
- Produced final report.pdf
- Validated the repo structure with validate_submission.py
- Archived as 2026AJ05869_DNN_Assignment.zip

## 10. Project structure
```text
2026AJ05869_DNN_Assignment/
├── README.md
├── FINAL_CHECKLIST.md
├── config.py
├── preflight.py
├── requirements.txt
├── validate_submission.py
├── results.csv
├── report.pdf
├── problem1/
│   ├── problem1.ipynb
│   ├── problem1_executed.ipynb
│   └── figures/
├── problem2/
│   ├── problem2.ipynb
│   ├── problem2_executed.ipynb
│   ├── generated_samples.txt
│   ├── THREE_TOKEN_ATTENTION.md
│   └── figures/
├── src/
│   ├── __init__.py
│   ├── allowed_models.py
│   ├── common.py
│   ├── data.py
│   ├── student_models.py
│   └── training.py
└── 2026AJ05869_DNN_Assignment.zip
```
