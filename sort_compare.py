
import random
import time


def insertion_sort(alist):
    start_time = time.perf_counter()

    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = current_value

    time_taken = time.perf_counter() - start_time
    return time_taken


def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        current_value = alist[i]
        position = i

        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position -= gap

        alist[position] = current_value


def shell_sort(alist):
    start_time = time.perf_counter()

    sublist_count = len(alist) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(alist, start_position, sublist_count)

        sublist_count = sublist_count // 2

    time_taken = time.perf_counter() - start_time
    return time_taken


def python_sort(alist):
    start_time = time.perf_counter()

    alist.sort()

    time_taken = time.perf_counter() - start_time
    return time_taken


def main():
    sizes = [500, 1000, 5000]
    number_of_lists = 100

    algorithms = [
        ("Insertion Sort", insertion_sort),
        ("Shell Sort", shell_sort),
        ("Python Sort", python_sort)
    ]

    for size in sizes:
        print(f"\nList size: {size}")
        print("-" * 60)

        total_times = {name: 0 for name, function in algorithms}

        for _ in range(number_of_lists):
            original_list = [
                random.randint(1, 100000) for _ in range(size)
            ]

            for name, function in algorithms:
                alist = original_list.copy()

                time_taken = function(alist)
                total_times[name] += time_taken

                assert alist == sorted(original_list)

        for name, function in algorithms:
            time_taken = total_times[name] / number_of_lists
            print(
                f"{name} took {time_taken:10.7f} seconds to run, on average"
            )


if __name__ == "__main__":
    main()
