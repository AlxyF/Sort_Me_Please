import matplotlib.pyplot as plt
import random

from bubble_sort import bubble_sort
from merge_sort import merge_sort_bottom_up

# array to sort
n = 50
numbers = [x for x in range(1, n + 1)]
labels = numbers.copy()
random.shuffle(numbers)

# sort plots
sorts = [bubble_sort, merge_sort_bottom_up]
sorts_gen = [x(numbers.copy()) for x in sorts]

n_cols = len(sorts) // 2 + 1
n_rows = len(sorts) // 2 + 1

fig, subplots = plt.subplots(n_cols, n_rows, figsize=(10.24, 7.68))
axis = []
print(subplots.flatten())
for ax in subplots.flatten():
    axis.append(ax)

pause = 0.001


def plot_sort(arr, current_change, axis, title):
    barlist = axis.bar(height=arr, x=labels, width=0.8)
    axis.set_ylim([0, n])
    axis.set_title(title)
    barlist[current_change].set_color('r')
    plt.draw()


def multiP():
    while True:
        for ax, sort in enumerate(sorts_gen):
            try:
                y = next(sort)
                axis[ax].cla()
                plot_sort(y[0], y[1], axis[ax], sort.__name__)
            except StopIteration:
                pass
        plt.pause(pause)


if __name__ == "__main__":
    multiP()
