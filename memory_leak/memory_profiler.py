from memory_profiler import profile

@profile
def leaky_function():
    """
    Function that simulates memory allocations and potential leaks.
    """
    data = []
    for i in range(1000):
        data.append('x' * 10000)  # Allocate memory
    return data

if __name__ == "__main__":
    leaky_function()
