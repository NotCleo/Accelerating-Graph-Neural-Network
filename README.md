# Accelerating-Graph-Neural-Network
This repository broadly will cover using Compressed Sparse Rows to accelerate GNN training and general graph theory ideas

# Graph Centrality Measures

Graph centrality measures are used to identify the most important or "central" nodes in a graph. Each type captures a different notion of importance or influence.

## 1. Degree Centrality

**Definition**: Number of edges connected to a node.

**Formula**:  
- For undirected graph: `deg(v) = number of neighbors`  
- For directed graph: in-degree and out-degree centralities

**Use case**: Identifies well-connected nodes (e.g., popular users in a social network).

**Function**: `nx.degree_centrality(G)`

---

## 2. Betweenness Centrality

**Definition**: Fraction of shortest paths that pass through a node.

**Formula**:  

![formula](https://latex.codecogs.com/png.image?\dpi{110}&space;C_B(v)=\sum_{s\ne\,v\ne\,t}\frac{\sigma_{st}(v)}{\sigma_{st}})


Where:
- `σ_st` is the total number of shortest paths from node `s` to node `t`.
- `σ_st(v)` is the number of those paths that pass through node `v`.

**Use case**: Finds bottlenecks or "bridge" nodes between communities.

**Function**: `nx.betweenness_centrality(G)`

---

## 3. Closeness Centrality

**Definition**: Inverse of the average distance from a node to all other nodes.

**Formula**:  

![formula](https://latex.codecogs.com/png.image?\dpi{110}&space;C_C(v)=\frac{1}{\sum_t\,d(v,\,t)})




**Use case**: Finds nodes that can spread information quickly to the whole network.

**Function**: `nx.closeness_centrality(G)`

---

## 4. Eigenvector Centrality

**Definition**: A node is important if it is connected to other important nodes.

**Use case**: Measures influence in a network more subtly than degree (used in ranking, e.g., Google’s PageRank).

**Function**: `nx.eigenvector_centrality(G)`

---

## 5. PageRank

**Definition**: Variant of eigenvector centrality used by Google; scores nodes based on incoming links and distributes importance iteratively.

**Use case**: Web page ranking, influence detection.

**Function**: `nx.pagerank(G)`

---

## 6. Katz Centrality

**Definition**: Like eigenvector centrality, but also includes immediate neighbors and applies a decay factor to distant connections.

**Use case**: Influence with small perturbations; more stable than eigenvector.

**Function**: `nx.katz_centrality(G, alpha=0.1, beta=1.0)`

---

## 7. Harmonic Centrality

**Definition**: Variant of closeness centrality using reciprocal of distance.

**Use case**: Works better in disconnected graphs.

**Function**: `nx.harmonic_centrality(G)`

---

## 8. Current-Flow Centrality

**Definition**: Uses electrical current flow analogy to measure centrality.

**Use case**: Suitable when information flow is not limited to shortest paths.

**Functions**:  
- Current-flow closeness: `nx.current_flow_closeness_centrality(G)`  
- Current-flow betweenness: `nx.current_flow_betweenness_centrality(G)`

---

## 9. Load Centrality

**Definition**: Based on how much "load" (flow of paths) passes through a node.

**Function**: `nx.load_centrality(G)`

---

## 10. Percolation Centrality

**Definition**: Centrality based on percolation (spread) of some information or disease.

**Use case**: Epidemiology, information spread.

**Function**: Not in standard NetworkX, requires custom implementation.
