## K-means-clustering-and-its-simple-application-on-stock-analysis

### K-means Clustering

K-means is a popular clustering algorithm used in data mining and machine learning. It aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean, serving as a prototype of the cluster. This results in a partitioning of the data space into Voronoi cells.

The algorithm works through the following steps:

Initialization: Start by selecting k initial centroids, where k is a user-defined number of clusters. The initial centroids can be chosen randomly from the data points, or they can be selected by other methods designed to speed up convergence and improve cluster quality.

Assignment step: Assign each data point to the closest centroid. The closeness is usually measured by the Euclidean distance between a data point and the centroids.

Update step: Calculate the new centroids (means) of the observations in the new clusters.

Repeat: Repeat the assignment and update steps until the centroids no longer change significantly, indicating that the algorithm has converged, or until a specified number of iterations is reached.

### Pure K-means

The "pure K-means" code gives a K-means algorithm on points clustering, supporting multiple dimensions.
two and three-dimensional results display functions are also provided. For results with more than four dimensions, see matrix output.

#### Test on 100 2-dimensional random points
![myplot](https://github.com/ANewGitHuber/K-means-clustering-and-its-simple-application-on-stock-analysis/assets/88078123/4f43cc13-265a-4fff-bbab-174165259d56)
![myplot1](https://github.com/ANewGitHuber/K-means-clustering-and-its-simple-application-on-stock-analysis/assets/88078123/ed5d9fcf-cf7b-49ed-bbdd-fe06316b043c)
![myplot3](https://github.com/ANewGitHuber/K-means-clustering-and-its-simple-application-on-stock-analysis/assets/88078123/b54185db-db80-4406-9fb4-3191a2617f7f)


### 2 simple K-means applications on the stock price.

#### Two Dimensional
Based on Yearly Volatility (x-axis) and Yearly Return (y-axis), clustering the stocks in 10 groups.
![myplot-2](https://github.com/ANewGitHuber/K-means-clustering-and-its-simple-application-on-stock-analysis/assets/88078123/7b330052-f6e5-4e4a-b59d-2e7c4c2ff6b6)

#### Three Dimensional
Based on Yearly Volatility (x-axis), Yearly Return (y-axis) and Close Price (z-axis), clustering the stocks in 10 groups.
![myplot-3](https://github.com/ANewGitHuber/K-means-clustering-and-its-simple-application-on-stock-analysis/assets/88078123/7e703d2f-f39e-4ee5-8bab-bc39468dec69)

@John Chen, 2024, Imperial College London. All rights to source codes are reserved.
