import math
import pandas as pd

# Password strength classifier function
def password_strength_numeric(password):
    S, L, D, P = 0, 0, 0, 0
    a, b, c, d = 0.66, 0.02, 0.32, 0.20
    upper, symbol, lower, number = False, False, False, False
    length = len(password)

    # Length evaluation (max score 25 points)
    if length >= 16:
        L += 25
    elif length < 16:
        if length >= 12:
            L += 15
        elif 8 <= length < 12:
            L += 10
        elif length < 8:
            L += 5

    L = L / 25 * 100

    # Evaluating the diversity of characters (max score 94 points)
    for char in password:
        if char.isupper():
            upper = True
        elif char.isdigit():
            number = True
        elif not char.isalnum() and not char.isspace():
            symbol = True
        elif char.islower():
            lower = True

    if upper:
        D += 26
    if lower:
        D += 26
    if number:
        D += 10
    if symbol:
        D += 32

    D = D / 94 * 100

    # Evaluating entropy (max score 25 points)
    E = length * math.log2(D) if D > 0 else 0
    E = min(25, E / 4)

    E = E / 25 * 100

    # Penalties
    char_frequencies = {}
    for char in password:
        char_frequencies[char] = char_frequencies.get(char, 0) + 1

    repeated_chars = sum(1 for char, count in char_frequencies.items() if count > 2)
    P += (repeated_chars / len(password)) * 0.3

    sequential = 0
    for i in range(len(password) - 1):
        if ord(password[i + 1]) - ord(password[i]) == 1:
            sequential += 1
    P += (sequential / len(password)) * 0.3

    common_patterns = ['123', 'abc', 'password', 'admin']
    pattern_matches = sum(1 for pattern in common_patterns if pattern in password.lower())
    P += pattern_matches * 0.4

    P = min(1, P) * 100

    # Final score
    S = a*L + b*D + c*E - d*P

    # Numeric classification based on the score
    if S >= 66:
        return 2  # Very Strong
    elif 33 < S < 66:
        return 1  # Strong
      # Moderate
    elif S <= 33:
        return 0  # Weak
    else:
        return 0  # Very Weak

# Load dataset
df = pd.read_csv('data2.csv', on_bad_lines='skip', encoding='latin1')  # Ensure this CSV is in the same folder as the script
df['password'] = df['password'].astype(str)

# Take a sample of the dataset
sample_df = df.sample(frac=0.1)  # Adjust frac to control the percentage sampled

# Apply the password strength classifier to the sampled data
sample_df['predicted_strength'] = sample_df['password'].apply(password_strength_numeric)

sample_df['match'] = sample_df['predicted_strength'] == sample_df['strength']
sample_df['difference'] = sample_df['predicted_strength'] - sample_df['strength']

# Calculate total accuracy
total_accuracy = sample_df['match'].mean() * 100
print(f"Total Accuracy: {total_accuracy:.2f}%")

# Calculate accuracy for each strength level
for strength in [0, 1, 2]:
    subset = sample_df[sample_df['strength'] == strength]
    if not subset.empty:  # Ensure there's data for the given strength
        strength_accuracy = subset['match'].mean() * 100
        print(f"Accuracy for strength {strength}: {strength_accuracy:.2f}%")
    else:
        print(f"No samples found for strength {strength}")

# Calculate over-predictions and under-predictions
over_predictions = sample_df[sample_df['difference'] > 0].shape[0]
under_predictions = sample_df[sample_df['difference'] < 0].shape[0]
total_mismatches = over_predictions + under_predictions

if total_mismatches > 0:
    over_prediction_rate = (over_predictions / total_mismatches) * 100
    under_prediction_rate = (under_predictions / total_mismatches) * 100
    print(f"Over-predictions: {over_prediction_rate:.2f}%")
    print(f"Under-predictions: {under_prediction_rate:.2f}%")
else:
    print("No mismatches found between predictions and dataset labels.")

# Breakdown by how far predictions were off
exact_mismatch = sample_df[sample_df['difference'].abs() == 1].shape[0]
more_than_one_mismatch = sample_df[sample_df['difference'].abs() > 1].shape[0]

print(f"Mismatches off by 1 level: {(exact_mismatch / len(sample_df)) * 100:.2f}%")
print(f"Mismatches off by more than 1 level: {(more_than_one_mismatch / len(sample_df)) * 100:.2f}%")

# Visualize the comparison
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='strength', data=sample_df, label="True Label")
sns.countplot(x='predicted_strength', data=sample_df, label="Predicted")
plt.legend()
plt.show()
