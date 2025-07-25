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


**Use case**: Finds bottlenecks or "bridge" nodes between communities.

**Function**: `nx.betweenness_centrality(G)`

---

## 3. Closeness Centrality

**Definition**: Inverse of the average distance from a node to all other nodes.


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


## Graph Density and Diameter

### 1. Graph Density

**Definition**:  
Graph density measures how close the graph is to being fully connected.

**Explanation**:  
- In a fully connected graph, every node has an edge to every other node.
- The density is a number between 0 and 1:
  - A value of 1 means the graph is completely connected.
  - A value close to 0 means very few connections.

**For Undirected Graphs**:  
Density = (2 × number of edges) / (number of nodes × (number of nodes - 1))

**For Directed Graphs**:  
Density = (number of edges) / (number of nodes × (number of nodes - 1))


### 2. Graph Diameter

**Definition**:  
The diameter is the longest shortest path between any two nodes in the graph.

**Explanation**:  
- For each pair of nodes, find the shortest path between them.
- The diameter is the **maximum** of all those shortest path lengths.
- Only defined for **connected graphs**.

**If the graph is not connected**:  
Use the diameter of the **largest connected component**.



