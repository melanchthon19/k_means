import random
import plot
import numpy as np


def generate_random_samples():
    x1 = random.sample(range(1000), 100)
    y1 = random.sample(range(1000), 100)

    return x1, y1


def get_distance(x, mean):
    x1, y1 = x
    x2, y2 = mean
    distance = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    return distance


def classify_data(data, centroids):
    x1, y1, x2, y2 = [], [], [], []
    for x in data:
        if get_distance(x, centroids[0]) <= get_distance(x, centroids[1]):
            x1.append(x[0])
            y1.append(x[1])
        else:
            x2.append(x[0])
            y2.append(x[1])

    return x1, y1, x2, y2


def reestimate_means(class_1, class_2):
    mean_1 = np.array([0.0, 0.0])
    mean_2 = np.array([0.0, 0.0])

    for x in class_1:
        mean_1 += x
    for x in class_2:
        mean_2 += x
    mean_1 /= len(class_1)
    mean_2 /= len(class_2)

    return mean_1, mean_2


x1, y1 = generate_random_samples()
data = np.array(list(zip(x1, y1)))
print('number of data points:', len(data))
k = 2
centroids = np.array([random.sample(range(1000), k) for i in range(k)])
print('number of initial centroids:', len(centroids))
print('centroid 1: {}\t centroid 2: {}'.format(centroids[0], centroids[1]))
plot.initial_graph(x1, y1, centroids)

converged = False
i = 0
while not converged:
    # Step 1: Classify given means
    x1, y1, x2, y2 = classify_data(data, centroids)
    plot.plot(x1, y1, x2, y2, i, centroids)

    # Step 2: Re-estimate means given classification
    class_1 = np.array(list(zip(x1, y1)))
    class_2 = np.array(list(zip(x2, y2)))
    new_centroids = np.array(reestimate_means(class_1, class_2))

    if np.array_equal(new_centroids, centroids):
        converged = True
        print('converged!\nat iteration {}'.format(i))
        print('centroid 1: {} number of data points: {}\ncentroid 2: {} number of data points: {}'.
              format(centroids[0], len(x1), centroids[1], len(x2)))
        plot.plot(x1, y1, x2, y2, i, centroids, converged=True)
    else:
        centroids = new_centroids
        print('iteration:', i)
        print('centroid 1: {}\tcentroid 2: {}'.format(centroids[0], centroids[1]))
    i += 1

