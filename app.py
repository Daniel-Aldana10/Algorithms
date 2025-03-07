from data import execution_time_gathering
import matplotlib.pyplot as plt

def print_results(table):
    print("Size | Bubble Sort (Time, Mem) | Merge Sort (Time, Mem) | Shell Sort (Time, Mem)")
    for row in table:
        size, bubble_time, merge_time, shell_time, bubble_mem, merge_mem, shell_mem = row
        print(f"{size:<5} | [{bubble_time}, {bubble_mem}] | [{merge_time}, {merge_mem}] | [{shell_time}, {shell_mem}]")

def plot_results(table):
    sizes = [row[0] for row in table]
    bubble_times = [row[1] for row in table]
    merge_times = [row[2] for row in table]
    shell_times = [row[3] for row in table]
    bubble_mem = [row[4] for row in table]
    merge_mem = [row[5] for row in table]
    shell_mem = [row[6] for row in table]

    # Gráfico de tiempos de ejecución
    plt.figure(figsize=(10,5))
    plt.plot(sizes, bubble_times, marker='o', label='Bubble Sort')
    plt.plot(sizes, merge_times, marker='s', label='Merge Sort')
    plt.plot(sizes, shell_times, marker='^', label='Shell Sort')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (ms)")
    plt.title("Execution Time of Sorting Algorithms")
    plt.legend()
    plt.grid()
    plt.show()

    # Gráfico de uso de memoria
    plt.figure(figsize=(10,5))
    plt.plot(sizes, bubble_mem, marker='o', label='Bubble Sort')
    plt.plot(sizes, merge_mem, marker='s', label='Merge Sort')
    plt.plot(sizes, shell_mem, marker='^', label='Shell Sort')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Memory Usage (bytes)")
    plt.title("Memory Usage of Sorting Algorithms")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    minimum_size = 1000
    maximum_size = 11000
    step = 2000
    samples_by_size = 7

    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)
    print_results(table)
    plot_results(table)
