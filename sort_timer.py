# Author: Kevin Braman
# GitHub username: bramank
# Date: 2/24/2023
# Description: This program defines a decorator function, two sorting functions, and a function to compare the
#              performance of the sorting functions. The decorator function 'sort_timer' decorates the two sorting
#              functions 'bubble_sort' and 'insertion_sort' with a timer from the 'time' module to determine the
#              amount of time taken to execute their functions. The function 'compare_sorts' compares both sorting
#              algorithms by generating a series of random lists for them to sort and then outputting a plot graph
#              using 'pyplot' that shows the time in seconds relative to the amount of elements sorted.

import functools
import random
import time
from matplotlib import pyplot


def sort_timer(function):
    """
    This decorator function takes a function as an argument and utilizes the 'wrapper' and 'perf_counter' functions
    to evaluate the execution time of the called function. The result is returned.
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start_timer = time.perf_counter()
        function(*args, **kwargs)
        end_timer = time.perf_counter()
        result = end_timer - start_timer
        return result

    return wrapper


@sort_timer
def bubble_sort(a_list):
    """Sorts a_list in ascending order using the bubble_sort method."""
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """Sorts a_list in ascending order using the insertion_sort method."""
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def compare_sorts(bubble_function, insertion_function):
    """
    This function takes the two sorting functions: 'bubble_sort' & ' insertion_sort' as arguments and compares the two
    algorithms by generating ten lists of increasing size (by increments of 1000), storing in a list the time it takes
    for each algorithm to execute. Once ten executions are preformed, the 'pyplot' module from 'matplotlib' is used
    to return a graph that shows the performance of both sorting methods.
    """
    # Generates 10 random lists of increasing size for the algorithms to sort, storing the results.
    test_cases, base_max_range, base_list, bubble_plots, insertion_plots = 0, 1001, [], [], []
    while test_cases < 10:
        for values in range(1, base_max_range):
            base_list.append(random.randint(1, 1000))

        test_list = list(base_list)
        bubble_plots.append(bubble_function(base_list)), insertion_plots.append(insertion_function(test_list))
        base_list.clear(), test_list.clear()
        test_cases, base_max_range = test_cases + 1, base_max_range + 1000

    # Creates a graph using the results.
    pyplot.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], bubble_plots, 'ro--', linewidth=2, label='Bubble Sort')
    pyplot.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], insertion_plots, 'go--', linewidth=2, label='Insertion Sort')
    pyplot.xlabel("Number of Elements Sorted (in thousands)")
    pyplot.ylabel("Time (in seconds)")
    pyplot.legend(loc='upper left')

    return pyplot.show()


def main():
    compare_sorts(bubble_sort, insertion_sort)


if __name__ == '__main__':
    main()
