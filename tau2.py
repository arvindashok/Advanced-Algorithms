from math import pi, sqrt, exp
import numpy as np
import scipy.stats as stats

def kendalltau_pdf(tau, n):
    """
    Calculates the PDF of Kendall's Tau under the null hypothesis.

    Args:
        tau: The value of Kendall's Tau.
        n: The number of items being ranked.

    Returns:
        The probability density of tau under the null hypothesis.
    """
    numerator = exp(-tau**2 / (2 * (n * (n - 1) / 12)))
    denominator = sqrt(n * (n - 1) / 2) / pi
    return numerator / denominator

# Get input for rankings and number of items
rankings_a = list(map(int, input("Enter ranking of a (space-separated integers): ").split()))
rankings_b = list(map(int, input("Enter ranking of b (space-separated integers): ").split()))
n = len(rankings_a)

# Calculate observed Tau and hypothesis test p-value
tau, p_value = stats.kendalltau(rankings_a, rankings_b)

# Generate range of possible Tau values
tau_range = np.linspace(-1, 1, 100)

# Calculate PDF for each Tau value
tau_pdf = [kendalltau_pdf(x, n) for x in tau_range]

# Import and configure plotting library
import matplotlib.pyplot as plt

# Plot the PDF and mark observed Tau
plt.plot(tau_range, tau_pdf, label="Null Hypothesis Distribution")
plt.axvline(x=tau, color="red", label=f"Observed Tau ({tau:.3f})")
plt.xlabel("Kendall's Tau")
plt.ylabel("Probability Density")
plt.title("Distribution of Kendall's Tau under Null Hypothesis")
plt.legend()
plt.show()


# Interpretation
if p_value < 0.1:
    print(f"Kendall's Tau: {tau:.3f} is statistically significant (p-value = {p_value:.3f}). There is a significant correlation between the rankings.")
else:
    print(f"Kendall's Tau: {tau:.3f} is not statistically significant (p-value = {p_value:.3f}). There is no significant correlation between the rankings.")
