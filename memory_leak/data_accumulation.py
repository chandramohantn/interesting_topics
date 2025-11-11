# Problematic global cache that accumulates data over time
CACHE = {}

def process_data(data):
    """
    Process incoming data and store results in a global cache.
    This function simulates a memory leak by continuously adding to the CACHE.
    """
    if data in CACHE:
        return CACHE[data]
    
    result = expensive_computation(data)
    CACHE[data] = result # this keeps growing indefinitely
    return result

def expensive_computation(data):
    """
    Simulate an expensive computation by performing some operations.
    """
    return data ** 2


# Better: Use weak references or limit cache size to prevent memory leaks
import weakref

class SmartCache:
    def __init__(self, max_size=1000):
        self._cache = {}
        self.max_size = max_size

    def get(self, key):
        return self._cache.get(key)
    
    def set(self, key, value):
        if len(self._cache) >= self.max_size:
            self._cache.pop(next(iter(self._cache)))  # Remove oldest item
        self._cache[key] = value
