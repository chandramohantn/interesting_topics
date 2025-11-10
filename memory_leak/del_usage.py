import gc

class LeakyNode:
    def __init__(self, name):
        self.name = name
        self.neighbor = None
        self.large_data = "x" * 1000000  # 1MB of data
        print(f"LeakyNode {name} created")
    
    def __del__(self):
        print(f"LeakyNode {self.name} destroyed")
        # PROBLEMATIC: Accessing neighbor in __del__
        if self.neighbor is not None:
            print(f"  {self.name}'s neighbor is {self.neighbor.name}")

def create_leaky_circular_reference():
    print("=== Creating Leaky Circular Reference ===")
    a = LeakyNode("LeakyA")
    b = LeakyNode("LeakyB")
    
    a.neighbor = b
    b.neighbor = a
    
    return a

# Enable GC debug to see what's happening
gc.set_debug(gc.DEBUG_SAVEALL)

print("Initial state:")
print(f"GC counts: {gc.get_count()}")
print(f"Objects in gc.garbage: {len(gc.garbage)}")

# Create the problematic circular reference
leaky_ref = create_leaky_circular_reference()

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