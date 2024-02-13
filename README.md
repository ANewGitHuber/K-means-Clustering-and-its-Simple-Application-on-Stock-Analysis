## K-means-clustering-and-its-simple-application-on-stock-analysis

K-means is a popular clustering algorithm used in data mining and machine learning. It aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean, serving as a prototype of the cluster. This results in a partitioning of the data space into Voronoi cells.

The algorithm works through the following steps:

Initialization: Start by selecting k initial centroids, where k is a user-defined number of clusters. The initial centroids can be chosen randomly from the data points, or they can be selected by other methods designed to speed up convergence and improve cluster quality.

Assignment step: Assign each data point to the closest centroid. The closeness is usually measured by the Euclidean distance between a data point and the centroids.

Update step: Calculate the new centroids (means) of the observations in the new clusters.

Repeat: Repeat the assignment and update steps until the centroids no longer change significantly, indicating that the algorithm has converged, or until a specified number of iterations is reached.


### 2 simple K-means applications on the stock price.

#### Two dimensional
Based on Yearly Volatility (x-axis) and Yearly Return (y-axis), cluster the stocks in 10 groups.
