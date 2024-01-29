import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def kendalls_tau_similarity(rankings_a, rankings_b):
    """Calculates Kendall's Tau similarity between two rankings, with hypothesis testing."""

    n = len(rankings_a)
    concordant_pairs, discordant_pairs = 0, 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if (rankings_a[i] < rankings_a[j] and rankings_b[i] < rankings_b[j]) or (rankings_a[i] > rankings_a[j] and rankings_b[i] > rankings_b[j]):
                concordant_pairs += 1
            elif (rankings_a[i] < rankings_a[j] and rankings_b[i] > rankings_b[j]) or (rankings_a[i] > rankings_a[j] and rankings_b[i] < rankings_b[j]):
                discordant_pairs += 1

    total_pairs = n * (n - 1) / 2
    tau = (concordant_pairs - discordant_pairs) / total_pairs

    # Hypothesis testing using Kendall's tau statistic
    z_score, p_value = stats.kendalltau(rankings_a, rankings_b)

    print(f"Kendall's Tau coefficient is : {tau}")
    print(z_score)
    print(p_value)
    # Interpretation of results
    if p_value < 0.1:  # significance level of 0.05
        print(f"Kendall's Tau: {tau:.3f} is statistically significant (p-value = {p_value:.3f}). There is a significant correlation between the rankings.")
    else:
        print(f"Kendall's Tau: {tau:.3f} is not statistically significant (p-value = {p_value:.3f}). There is no significant correlation between the rankings.")


    sns.scatterplot(x=rankings_a, y=rankings_b)
    plt.xlabel("Rankings A")
    plt.ylabel("Rankings B")
    plt.title("Scatter Plot of Rankings")
    plt.show()
    

    
# Get input for rankings_a and rankings_b
rankings_a = list(map(int, input("Enter ranking of a (space-separated integers): ").split()))
rankings_b = list(map(int, input("Enter ranking of b (space-separated integers): ").split()))

kendalls_tau_similarity(rankings_a, rankings_b)



