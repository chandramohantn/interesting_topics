# Memory Leak
A memory leak occurs when a program allocates memory but fails to release it back to the system when its no longer needed. Over time, this causes the program to consume increasingly more memory, potentially leading to performance degradation or crashes.

## Python Memory Management Basics
Python uses reference counting and garbage collection to manage memory.
 - Reference counting: Objects are deleted when their reference count reaches zero. 
 - Garbage collector: Handles circular references that reference counting cant resolve.

## Common Memory Leak Scenarios

