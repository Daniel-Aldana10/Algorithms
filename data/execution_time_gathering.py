import time

from sorting_algorithms import bubblesort
from sorting_algorithms import mergesort
from sorting_algorithms import shellsort

from data import constants
from data import data_generator


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size):
    samples = []
    for _ in range(samples_by_size):
        samples.append(data_generator.get_random_list(size))

    return [
        take_time_for_algorithm(samples, bubblesort.bubblesort),
        take_time_for_algorithm(samples, mergesort.mergesort),
        take_time_for_algorithm(samples, shellsort.shellsort),
    ]


"""
    Returns the median of the execution time measures for a sorting approach given in 
"""


def take_time_for_algorithm(samples_array, sorting_approach):
    times = []

    for sample in samples_array:
        start_time = time.time()
        sorting_approach(sample.copy())
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))

    times.sort()
    return times[len(times) // 2]
