import numpy as np
import math
import matplotlib.pyplot as plt
from splitters import split_to_intervals, split_to_discrete
# from interval_estimates import *
from scipy.stats import norm
from points import *


# def norm(mean, sq_dev, x):
#     return (1.0 / (sq_dev * np.sqrt(2 * np.pi))) * (np.exp((-1/2)*((x - mean) / sq_dev) ** 2))


# гистограмма
def create_bar_chart(inp_data: list) -> None:
    plt.style.use('_mpl-gallery')

    n = len(inp_data)
    print(n)

    data = split_to_intervals(inp_data)
    data.append([((data[1][i] + data[0][i]) / 2) for i in range(len(data[0]))])

    mean = get_mean(inp_data)
    sq_dev = get_square_root_deviation(inp_data)
    sq_dev = 85.33345416636304
    p = mean / (sq_dev ** 2)
    p = 0.297
    l = 1 / mean

    print(data[2])
    # print(data[3])

    x = [(data[1][i] + data[0][i]) / 2 for i in range(len(data[0]))]
    # x = np.arange(-1000, 1000)
    y = np.array([(i + 1) / 1e5 for i in data[2]])

    plt.figure(figsize=(20, 7))

    mean = np.mean(inp_data)
    print(mean, sq_dev)

    plt.hist(inp_data, 90, density=True)
    # plt.bar(x, data[2])

    x = np.arange(-1000, 1000, 1)

    # Visualizing the results
    pdf = norm.pdf(x, loc=mean, scale=sq_dev)
    plt.plot(x, pdf, 'r-', lw=2, alpha=0.6)

    print(pdf)
    # pdf = [pois(mean, i) * n for i in x]
    # plt.plot(x, pdf, 'r-', lw=2, alpha=0.6, label='expon pdf', color='red')
    #
    # pdf = [expon(l, i) * n for i in x]
    # plt.plot(x, pdf, 'r-', lw=2, alpha=0.6, label='expon pdf', color='green')

    plt.show()
