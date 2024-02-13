from collections import defaultdict
from random import uniform
from math import sqrt


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


#________________________________End of Functions________________________________


# Test on 2-dimensions (6 points into 3 clusters)
Test_X = [5, 4, 8, 9, 6, 8]
Test_Y = [1, 2, 4, 3, 5, 5]
PointSet = as_point_format(Test_X, Test_Y)

print("Point Set: " + str(PointSet))
print("Result: " + str(k_means(PointSet, 3)))

# Test on 5-dimensions (6 points into 3 clusters)
PointSet2 = [(5, 1, 1, 6, 7), (4, 2, 8, 6, 1), (8, 4, 1, 10, 5), (9, 3, 7, 5, 7), (5, 7, 5, 7, 5), (1, 1, 1, 1, 1)]
print("Point Set: " + str(PointSet2))
print("Result: " + str(k_means(PointSet2, 3)))
