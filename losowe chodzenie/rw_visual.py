import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    # Przygotowanie losowego chodzenia
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('ggplot')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none')
    ax.scatter(0, 0, c='green', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100, edgecolors='none')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

