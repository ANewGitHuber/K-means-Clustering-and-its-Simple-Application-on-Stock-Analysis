from collections import defaultdict
from random import uniform
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


def as_point_format(x_axis, y_axis):
    """
    Combine the x list and the y list into point (x,y) format
    Only use when we have just 2-dimensional indicators
    """
    points = list(zip(x_axis, y_axis))
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


# -------------------------------- End of Functions -------------------------------- #


# -------------------------------- Test on 100 random points-------------------------------- #

# Generate 100 random Points
X = np.random.rand(100).tolist()
Y = np.random.rand(100).tolist()

points = as_point_format(X, Y)
print("Point Set: " + str(points))

# Apply K-means Algorithm
K_means_assignment = k_means(points, 10)
print("Result: " + str(K_means_assignment))

# Draw Result Diagrams
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

x, y = zip(*points)
plt.scatter(x, y, color=set_colors, label='Scatter Plot', marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-Means Assignment Result, K=10')
plt.show()
