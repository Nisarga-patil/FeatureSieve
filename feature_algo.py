from itertools import combinations
import numpy as np
import networkx as nx

def featuresieve(df, sample_size=100, tau=0.95):
    """
    Implements the featuresieve algorithm that identifies redundant features in a dataset.
    """
    # Validate tau
    if tau <= 0 or tau >= 1:
        raise ValueError("tau must be greater than 0 and lesser than 1")
    
    # Validate Sample Size
    if sample_size < 1:
        raise ValueError("sample_size must be greater than 0")
    if sample_size > len(df):
        raise ValueError("sample_size must be lesser than the number of rows in the DataFrame")

    # ✅ FIXED: Check that all columns are numeric
    if not all(np.issubdtype(dtype, np.number) for dtype in df.dtypes):
        raise ValueError("DataFrame must contain only numeric columns")
    
    # Validate DataFrame
    if len(df.columns) < 2:
        raise ValueError("DataFrame must have at least 2 columns")

    sample = df.sample(sample_size).to_numpy()
    r2_scores = {}
    col_idx = {col: df.columns.get_loc(col) for col in df.columns}
    
    # Calculate R-squared values
    for first, second in combinations(df.columns, 2):
        first_i = col_idx[first]
        second_i = col_idx[second]
        cov = np.cov(sample[:, first_i], sample[:, second_i])
        r2_scores[first, second] = cov[1, 0]**2 / (cov[1, 1] * cov[0, 0]) if np.all(cov) else 0

    def make_graph(scores, tau):
        def get_weight(r2):
            return (r2 - tau)/(1 - tau) * 0.5 + 0.5

        G = nx.Graph()
        for (first, second), r2 in scores.items():
            if r2 >= tau:
                G.add_edge(first, second, weight=get_weight(r2))
        return G

    G = make_graph(r2_scores, tau)
    del sample
    del r2_scores

    essential = []
    for comp in list(nx.connected_components(G)):
        subgraph = G.subgraph(comp)
        max_degree_node, _ = max(subgraph.degree(), key=lambda item: item[1])
        essential.append(max_degree_node)

    redundant = [node for node in G.nodes() if node not in essential]

    return redundant
