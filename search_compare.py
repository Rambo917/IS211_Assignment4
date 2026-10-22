
import random
import time


def sequential_search(alist, item):
    start_time = time.perf_counter()

    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    time_taken = time.perf_counter() - start_time
    return found, time_taken


def ordered_sequential_search(alist, item):
    start_time = time.perf_counter()

    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
            stop = True
        else:
            pos += 1

    time_taken = time.perf_counter() - start_time
    return found, time_taken


def binary_search_iterative(alist, item):
    start_time = time.perf_counter()

    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if alist[midpoint] == item:
            found = True
        elif item < alist[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    time_taken = time.perf_counter() - start_time
    return found, time_taken


def binary_search_recursive(alist, item):
    start_time = time.perf_counter()

    def search(first, last):
        if first > last:
            return False

        midpoint = (first + last) // 2

        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            return search(first, midpoint - 1)
        else:
            return search(midpoint + 1, last)

    found = search(0, len(alist) - 1)

    time_taken = time.perf_counter() - start_time
    return found, time_taken


def main():
    sizes = [500, 1000, 5000]
    number_of_lists = 100
    search_item = 99999999

    algorithms = [
        ("Sequential Search", sequential_search),
        ("Ordered Sequential Search", ordered_sequential_search),
        ("Binary Search Iterative", binary_search_iterative),
        ("Binary Search Recursive", binary_search_recursive)
    ]

    for size in sizes:
        print(f"\nList size: {size}")
        print("-" * 60)

        total_times = {name: 0 for name, function in algorithms}

        for _ in range(number_of_lists):
            alist = [random.randint(1, 100000) for _ in range(size)]

            found, time_taken = sequential_search(alist, search_item)
            assert not found
            total_times["Sequential Search"] += time_taken

            sorted_list = alist.copy()
            sorted_list.sort()

            for name, function in algorithms[1:]:
                found, time_taken = function(sorted_list, search_item)
                assert not found
                total_times[name] += time_taken

        for name, function in algorithms:
            time_taken = total_times[name] / number_of_lists
            print(
                f"{name} took {time_taken:10.7f} seconds to run, on average"
            )


if __name__ == "__main__":
    main()
