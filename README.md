# K-means
Cluster algorithm to assign data to k clusters.

This code generates 100 random data points that are clustered in k=2 clusters.

The algorithm has two steps:
1) Data are classified according to the initial means.
2) Means are re-estimated given the data that was classified in step 1.
Steps 1 and 2 are repeated until means do not change.

For every iteration, a plot is generated to visualy follow the clusters.

# Usage
Clone repository and run k_means.py using any IDE.

# Plot Examples
<img src="https://github.com/melanchthon19/k_means/blob/master/plot_examples/unclassified.png" width="400" height="400" />
<img src="https://github.com/melanchthon19/k_means/blob/master/plot_examples/i1.png" width="400" height="400" />
<img src="https://github.com/melanchthon19/k_means/blob/master/plot_examples/i3.png" width="400" height="400" />
<img src="https://github.com/melanchthon19/k_means/blob/master/plot_examples/converged.png" width="400" height="400" />
