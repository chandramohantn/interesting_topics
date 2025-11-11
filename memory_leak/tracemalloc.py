import tracemalloc


def monitor_memory():
    """
    Monitor memory allocations using tracemalloc.
    """
    tracemalloc.start()
    print("=== Memory Allocation Monitoring with tracemalloc ===")

    snapshots = []

    # Take initial snapshot
    snapshot1 = tracemalloc.take_snapshot()

    # Run your function that might leak memory
    potential_leaky_function()

    # Take another snapshot
    snapshot2 = tracemalloc.take_snapshot()

    # Compare snapshots
    top_stats = snapshot2.compare_to(snapshot1, 'lineno')

    print("Memory allocation differences:")
    for stat in top_stats[:10]:
        print(stat)

    tracemalloc.stop()


def potential_leaky_function():
    """
    Function that simulates memory allocations and potential leaks.
    """
    data = []
    for i in range(1000):
        data.append('x' * 10000)  # Allocate memory

