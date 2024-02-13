import pandas as pd
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from collections import defaultdict
from random import uniform
from math import sqrt


def read_names_into_dict():
    """
    Read company names into a dictionary
    """
    d = dict()
    with open("SP_500_firms.csv") as csvfile:
        input_file = csv.DictReader(csvfile)
        for row in input_file:
            d[row['Symbol']] = [row['Name'], row['Sector']]
    return d


def as_point_format(x_axis, y_axis, z_axis):
    """
    Combine the x list, y list and z list into three-dimensional point (x,y,z) format
    """
    points = list(zip(x_axis, y_axis, z_axis))
    return points


def center_point(points):
    """
    Returns the center point of all the points.
    """
    # Note - Allow multiple dimensions
    dimension = len(points[0])

    center = []

    for x in range(dimension):
        total_dim = 0  # dimension sum

        for p in points:
            total_dim += p[x]

        # average of each dimension
        center.append(total_dim / float(len(points)))

    return center


def distance(a, b):
    """
    Compute the distance between two points
    """
    dimensions = len(a)

    distances = 0

    if a != 0 and b != 0:
        for dimension in range(dimensions):
            dimensional_difference = (a[dimension] - b[dimension]) ** 2
            distances += dimensional_difference

    else:
        distances += 0

    return sqrt(distances)


def assign_points(points, centers):
    """
    For given dataset "points":
    assign each point to an index that corresponds to the index
    of the center point on its proximity to that point.

    Return an array of indexes of centers that correspond to
    an index in the data set; that is, if there are N points
    in `data_set` the list we return will have N elements.
    """
    assignments = []

    for point in points:
        shortest = float('inf')  # Positive Infinity
        shortest_index = 0

        for i in range(len(centers)):
            distances = distance(point, centers[i])

            if distances < shortest:
                shortest = distances
                shortest_index = i

        assignments.append(shortest_index)

    return assignments


def group_centers(points, assignments):
    """
    Compute the center for each of the assigned groups.
    Return `k` centers where `k` is the number of assignments.
    """
    new_means = defaultdict(list)
    centers = []

    for assignment, point in zip(assignments, points):
        new_means[assignment].append(point)

    for points in new_means.values():
        centers.append(center_point(points))

    return centers


def generate_k(data_set, k):
    """
    Given `data_set`, which is an array of arrays,
    find the minimum and maximum for each coordinate, a range.
    Generate `k` random points between the ranges.
    Return an array of the random points within the ranges.
    """
    centers = []
    dimensions = len(data_set[0])
    min_max = defaultdict(int)

    for point in data_set:
        for i in range(dimensions):
            val = point[i]
            min_key = 'min_%d' % i
            max_key = 'max_%d' % i
            if min_key not in min_max or val < min_max[min_key]:
                min_max[min_key] = val
            if max_key not in min_max or val > min_max[max_key]:
                min_max[max_key] = val

    for k in range(k):
        random_point = []

        for i in range(dimensions):
            min_val = min_max['min_%d' % i]
            max_val = min_max['max_%d' % i]

            random_point.append(uniform(min_val, max_val))

        centers.append(random_point)

    return centers


def k_means(dataset, k):
    """
    Apply the k-means algorithm
    """
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None

    while assignments != old_assignments:
        new_centers = group_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)

    return assignments


# ------------------- End of functions ------------------- #

names_dict = read_names_into_dict()
comp_names = names_dict.keys()

# Read price data with pandas
filename = 'SP_500_close_2015.csv'
price_data = pd.read_csv(filename, index_col=0)

first_price = price_data.iloc[0]
last_price = price_data.iloc[-1]
returns_prices = (price_data - price_data.shift(1)) / price_data.shift(1)

# Calculate the three a-xis
yearly_returns = (last_price - first_price) / first_price
yearly_volatilities = returns_prices.std()

# ------------------- Parameter Setting Part ------------------- #
# Set two characteristics of stocks as the attribute
x_attribute = yearly_volatilities
y_attribute = yearly_returns
z_attribute = last_price
preset_cluster_number = 10
# -------------------------------------------------------------- #

# Create a 3D scatterplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the data points
ax.scatter(x_attribute, y_attribute, z_attribute, c='red', marker='o')
ax.set_xlabel('Yearly Volatility')
ax.set_ylabel('Yearly Returns')
ax.set_zlabel('Last Price')
plt.title('Stock Distribution Based on Three Characteristics')

# Display the plot
plt.show()

# Based on the two attributes, format the stocks as points
stocks = as_point_format(x_attribute, y_attribute, z_attribute)

# Apply K-means
K_means_assignment = k_means(stocks, preset_cluster_number)
print("K means assignment result: ")
print(K_means_assignment)

# ------------------- Part that needs modifying if parameters changed ------------------- #
set_colors = []

for number in K_means_assignment:
    if number == 0:
        set_colors.append('red')
    elif number == 1:
        set_colors.append('blue')
    elif number == 2:
        set_colors.append('green')
    elif number == 3:
        set_colors.append('black')
    elif number == 4:
        set_colors.append('yellow')
    elif number == 5:
        set_colors.append("grey")
    elif number == 6:
        set_colors.append("purple")
    elif number == 7:
        set_colors.append('magenta')
    elif number == 8:
        set_colors.append('xkcd:coral')
    elif number == 9:
        set_colors.append('xkcd:teal')
    elif number == 10:
        set_colors.append('xkcd:lavender')
# ---------------------------------------------------------------------------------------- #

# Draw plot after the K-means clustering
x, y, z = zip(*stocks)

# Create a 3D scatterplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the data points
ax.scatter(x, y, z, c=set_colors, marker='o')
ax.set_xlabel('Yearly Volatility')
ax.set_ylabel('Yearly Returns')
ax.set_zlabel('Last Price')
plt.title('Assigment of Stocks after K-means clustering')

# Display the plot
plt.show()


