import matplotlib.pyplot as plt


def initial_graph(x1, y1, centroids):
    plt.scatter(x1, y1, label='data', color='lightblue')
    plt.scatter(centroids[0][0], centroids[0][1], label='mean 1', color='purple', marker='^')
    plt.scatter(centroids[1][0], centroids[1][1], label='mean 2', color='indigo', marker='v')
    plt.title('Initial data: unclassified')
    plt.legend()
    plt.show()


def plot(x1, y1, x2, y2, i, centroids, converged=False):
    plt.scatter(x1, y1, label='class 1', color='r')
    plt.scatter(x2, y2, label='class 2', color='b')
    plt.scatter(centroids[0][0], centroids[0][1], label='mean 1', color='purple', marker='^')
    plt.scatter(centroids[1][0], centroids[1][1], label='mean 2', color='indigo', marker='v')
    if converged:
        plt.title('iteration = {} Converged!'.format(i))
    else:
        plt.title('iteration = {}'.format(i))
    plt.legend()
    plt.show()