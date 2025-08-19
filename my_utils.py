import numpy as np
import pandas as pd


def state_to_binary_string(state):
    """
    Convert an initial state into a binary string.
    Example: [0, 1, 0, 1] -> "0101"
    """
    return "".join(map(str, state))


def group_duplicates(freq_vectors):
    """Group all rules that produce identical frequency vectors."""
    groups = {}
    for rule_num, vec in enumerate(freq_vectors, start=1):
        key = tuple(vec)
        groups.setdefault(key, []).append(rule_num)

    # keep only groups with more than 1 rule
    return [group for group in groups.values() if len(group) > 1]


def create_summary_table(init_states, all_results):
    """
    Generate a summary table showing the number of duplicate groups
    and their details for each initial state.

    Parameters:
        init_states : The original initial states.
        all_results : Results for running the full pipeline on each initial state.

    Returns:
        Summary table with columns: Initial State, Group Count, Duplicate Groups Pairs
    """

    stats = []

    # Iterate over each initial state and its corresponding result
    for idx, init in enumerate(init_states):
        freq_vectors = all_results[idx]["frequency_vectors"]

        # Find duplicate groups for a particular initial state
        dup_groups = group_duplicates(freq_vectors)

        # Record statistics for the summary table
        stats.append({
            "Initial State": state_to_binary_string(init),
            "Group Count": len(dup_groups),
            "Duplicate Groups": dup_groups
        })

    pd.set_option("max_colwidth", 50)

    # Create a summary DataFrame
    df = pd.DataFrame(stats)
    return df
