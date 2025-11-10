import gc
import time

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        print(f"Node {self.value} created.")

    # def __del__(self):
    #     print(f"Node {self.value} deleted.")

def create_circular_reference():
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node2.next = node1  # Creates a circular reference
    return node1

# Enable GC debug to see what's happening
gc.set_debug(gc.DEBUG_SAVEALL)

print("Initial state:")
print(f"GC counts: {gc.get_count()}")
print(f"Objects in gc.garbage: {len(gc.garbage)}")

# Create the problematic circular reference
leaky_ref = create_circular_reference()

print(f"After creation - GC counts: {gc.get_count()}")

# Delete the external reference
del leaky_ref
print(f"After deletion - GC counts: {gc.get_count()}")

# Try to collect garbage
print("Attempting garbage collection...")
collected = gc.collect()
print(f"GC collected {collected} objects")

print(f"After gc.collect() - GC counts: {gc.get_count()}")
print(f"Objects in gc.garbage: {len(gc.garbage)}")

# Check if objects are still hanging around
if gc.garbage:
    print("MEMORY LEAK DETECTED!")
    for obj in gc.garbage:
        print(f"  Uncollectable: {obj} (type: {type(obj)})")

gc.set_debug(0)  # Disable debug mode
