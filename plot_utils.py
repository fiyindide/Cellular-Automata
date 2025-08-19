# plot_utils.py
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_frequency_vector(rule_num, frequency_vector, title_prefix="Frequency Vector"):
    """
    Plots the frequency vector for a given rule.
    Ex. plot_frequency_vector(42, frequency_vectors[42])
    """
    plt.figure(figsize=(10, 6))
    plt.plot(np.arange(len(frequency_vector)), frequency_vector, label=f"Rule {rule_num}")
    plt.title(f"{title_prefix} for Rule {rule_num}")
    plt.xlabel("Position")
    plt.ylabel("Frequency of 1s")
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_pca_scatter(reduced_data, labels, title="PCA of Frequency Vectors"):
    """
    Plots a PCA scatter plot given reduced data and cluster labels.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=reduced_data[:, 0], y=reduced_data[:, 1], hue=labels, palette='tab10')
    plt.title(title)
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.grid(True)
    plt.show()


def plot_multiple_frequency_vectors(frequency_vectors, rule_nums, title="Frequency Vectors"):
    """
    Plots multiple frequency vectors for comparison.
    E.G. plot_multiple_frequency_vectors(frequency_vectors, [0, 42, 100])
    """
    plt.figure(figsize=(10, 6))
    for rule_num in rule_nums:
        plt.plot(np.arange(len(frequency_vectors[rule_num])), frequency_vectors[rule_num], label=f"Rule {rule_num}")
    plt.title(title)
    plt.xlabel("Position")
    plt.ylabel("Frequency of 1s")
    plt.grid(True)
    plt.legend()
    plt.show()
