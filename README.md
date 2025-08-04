## Password Strength Analyzer

This project was developed as part of the **CAHSI LREU Program** (Oct 2024 – Dec 2024). It analyzes password datasets to evaluate strength using custom logic and feature-based processing. Each dataset is processed by its own dedicated Python script.

## Datasets Used

This project uses five publicly available password datasets from Kaggle:

data1.csv -> Password Strength Classifier (https://www.kaggle.com/datasets/vivekprajapati2048/password-strength-classifier?resource=download)

data2.csv -> Password Dataset (https://www.kaggle.com/datasets/soylevbeytullah/password-datas)

data3.csv -> Password Metrics Dataset (https://www.kaggle.com/datasets/karthikudyawar/password-metrics-dataset)

data4.csv -> Password Strength Dataset (https://www.kaggle.com/datasets/jeffersonvalandro/password-dataset)

data5.csv -> Password Security: Sber Dataset (https://www.kaggle.com/datasets/morph1max/password-security-sber-dataset?select=passwords.csv)

## Features

- **Length-based scoring** — Rewards longer passwords, with max score at 16+ characters
- **Character diversity analysis** — Measures variety (uppercase, lowercase, numbers, symbols) based on a 94-character space
- **Entropy estimation** — Approximates password entropy using Shannon-like formula scaled to 25 points
- **Penalty system** — Reduces score for:
  - Character repetition
  - Sequential characters (like `abcd`, `1234`)
  - Common patterns (e.g., `password`, `admin`, `123`)
- Final score calculated as:
  
S = aL + bD + cE - dP

where:
- `L` = length score  
- `D` = diversity score  
- `E` = entropy estimate  
- `P` = penalty factor  
- `a, b, c, d = 0.66, 0.02, 0.32, 0.20`

- One script per dataset for modular evaluation
- Passwords are classified into 3 numeric categories:
- `0` = Weak  
- `1` = Strong  
- `2` = Very Strong

## How to Run

### 1. Requirements

This project uses:

- Python **3.8+**
- `pandas` — for CSV data processing
- `matplotlib` — for visualizing strength predictions
- `seaborn` — for enhanced plotting aesthetics
- `os`, `math` — Python standard libraries

Install the required packages with:

```bash
pip install pandas matplotlib seaborn
```

### 2. Run the Menu Script
After installing the dependencies, launch the interactive menu:

```bash
python main.py
```

You’ll see a menu where you can choose which dataset processor to run:

=== Password Strength Analyzer Menu ===
1. Run Dataset Processor 1
2. Run Dataset Processor 2
3. Run Dataset Processor 3
4. Run Dataset Processor 4
5. Run Dataset Processor 5
6. Exit

## Results & Visualization

Each dataset processor outputs:

- **Total accuracy** of the prediction model
- **Accuracy by strength level** (Weak = 0, Strong = 1, Very Strong = 2)
- **Over-prediction vs. Under-prediction rate**
- **Mismatch severity** (how far off predictions were)
- **Visualization** comparing actual vs. predicted strength scores using Seaborn

### Example Output:
```text
Total Accuracy: 78.24%
Accuracy for strength 0: 88.57%
Accuracy for strength 1: 71.42%
Accuracy for strength 2: 65.00%
Over-predictions: 62.50%
Under-predictions: 37.50%
Mismatches off by 1 level: 19.23%
Mismatches off by more than 1 level: 2.54%
```

## Acknowledgment

This project was completed under the mentorship of the **CAHSI LREU Program** — a collaborative research experience initiative sponsored by the Computing Alliance of Hispanic-Serving Institutions (CAHSI).

## Author

**Diego Molina**  
GitHub: [@diego-molina10](https://github.com/diego-molina10)
