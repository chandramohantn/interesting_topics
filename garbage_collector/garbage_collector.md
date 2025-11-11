# GARBAGE COLLECTION
Automatic memory management system that reclaims memory occupied by objects that are no longer in use by the program. 

## Problem that Garbage Collector Solves
Programmers need to manually manage memory.
```
# Hypothetical manual memory management (like C/C++)
def manual_memory_management():
    # Allocate memory
    data = malloc(1024)  # Get 1KB of memory
    
    # Use the memory
    # ... do work ...
    
    # MUST remember to free it
    free(data)  # If you forget this, memory leak!
```

With garbage collection, this happens automatically.
```
# Python - automatic memory management
def automatic_memory_management():
    data = [1, 2, 3, 4, 5]  # Memory allocated automatically
    # ... do work ...
    # When data goes out of scope, memory is automatically reclaimed
    # No need to manually free anything!
```

## How Python's Garbage Collector Works
Python uses a combination of two techniques:
 - Reference Counting (Primary mechanism)
 - Generational Garbage Collection (For circular references)

## Garbage Collection - Utilities
 - gc.garbage() : Return a list that holds uncollectable objects. Normally, it should be empty. It only contains objects that the garbage collector could not collect because they are in a cycle and have __del__ methods.
 If there are no __del__ methods, then the circular references are collectable and hence gc.garbage would remain empty.
 - gc.get_count() : Returns the number of objects in each generation.
 - gc.collect() : Returns the number of objects that were collected by the garbage collector.
