import time
import tracemalloc
from sorting_algorithms import bubblesort, mergesort, shellsort
from data import constants, data_generator

def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []
    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size:", size)
        results = take_times(size, samples_by_size)
        bubble_time, bubble_mem = results[0]
        merge_time, merge_mem = results[1]
        shell_time, shell_mem = results[2]
        return_table.append([size, bubble_time, merge_time, shell_time, bubble_mem, merge_mem, shell_mem])
    return return_table

def take_times(size, samples_by_size):
    samples = []
    for _ in range(samples_by_size):
        samples.append(data_generator.get_random_list(size))
    return [
        take_time_and_memory_for_algorithm(samples, bubblesort.bubblesort),
        take_time_and_memory_for_algorithm(samples, mergesort.mergesort),
        take_time_and_memory_for_algorithm(samples, shellsort.shellsort),
    ]

def take_time_and_memory_for_algorithm(samples_array, sorting_approach):
    times = []
    mem_usages = []
    for sample in samples_array:
        tracemalloc.start()
        start_time = time.time()
        sorting_approach(sample.copy())
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        exec_time = int(constants.TIME_MULTIPLIER * (end_time - start_time))
        times.append(exec_time)
        mem_usages.append(peak)
    times.sort()
    mem_usages.sort()
    return times[len(times) // 2], mem_usages[len(mem_usages) // 2]

