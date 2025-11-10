# Memory Leak
A memory leak occurs when a program allocates memory but fails to release it back to the system when its no longer needed. Over time, this causes the program to consume increasingly more memory, potentially leading to performance degradation or crashes.

## Python Memory Management Basics
Python uses reference counting and garbage collection to manage memory.
 - Reference counting: Objects are deleted when their reference count reaches zero. 
 - Garbage collector: Handles circular references that reference counting cant resolve.

## Common Memory Leak Scenarios
 - Circular references with __del__ methods
 - Global lists/dictionaries accumulating data
 - Unclosed resources (files, database connections)
 - Event listeners and callbacks

## Detect Memory Leaks
 - Using tracemalloc
 - Using memory_profiler
 - Using objgraph

## Preventing Memory Leaks
 - Use context managers for resources
 - Break circular references
 - Implement proper cache management
 - Monitor and limit data structures
 - Regular garbase collection

## Best Practices Summary
 - Use context managers for files, connections and resources
 - Avoid global mutable state whenever possible
 - Use weak references for circular dependencies
 - Set bounds for cache and data structures
 - Explicitly close resources when context managers are not available
 - Monitor memory usage during development and testing
 - Use memory profiling tools regularly
 - Break circular references in complex object graphs
 - Clear caches periodically or use TTL based caching
 - Test with large datasets to identify scaling issues
