def kendalls_tau_similarity(rankings_a, rankings_b):
    n = len(rankings_a)
    concordant_pairs = 0
    discordant_pairs = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if (rankings_a[i] < rankings_a[j] and rankings_b[i] < rankings_b[j]) or \
               (rankings_a[i] > rankings_a[j] and rankings_b[i] > rankings_b[j]):
                concordant_pairs += 1
            elif (rankings_a[i] < rankings_a[j] and rankings_b[i] > rankings_b[j]) or \
                 (rankings_a[i] > rankings_a[j] and rankings_b[i] < rankings_b[j]):
                discordant_pairs += 1

    total_pairs = n * (n - 1) / 2
    tau = (concordant_pairs - discordant_pairs) / total_pairs

    return tau

rankings_a = [3, 1, 4, 2, 5]
rankings_b = [2, 1, 4, 3, 5]

tau_similarity = kendalls_tau_similarity(rankings_a, rankings_b)
print(f"Kendall's Tau Similarity: {tau_similarity}")
print(f"Kendall's Tau Dissimilarity: {1-tau_similarity}")
