import gc
import sys


def step_by_step_gc_working():
    print("=== Step-by-Step Garbage Collection Working ===")

    class Trackable:
        instances = []

        def __init__(self, name):
            self.name = name
            self.next = None
            self.data = "X" * 1000000  # Allocate some memory
            Trackable.instances.append(self)
            print(f"Created: {self.name}")

        def __del__(self):
            print(f"Deleted: {self.name}")
            if self in Trackable.instances:
                Trackable.instances.remove(self)

    def create_complex_scenario():
        """
        Create a mix of collectable and reference-cycled objects to demonstrate
        """
        # Object A: Will be garbage collected immediately
        a = Trackable("A_Garbage_Collectable")

        # Objects B and C: Circular reference (garbage)
        b = Trackable("B_Circular")
        c = Trackable("C_Circular")
        b.next = c
        c.next = b

        # Remove references from the Trackable.instances list
        Trackable.instances.remove(a)
        Trackable.instances.remove(b)
        Trackable.instances.remove(c)

        # Object D: Will be kept (referenced)
        d = Trackable("D_Kept")

        return d # Only return d, making a, b, c unreachable
    
    print("Creating complex scenario...")
    kept_object = create_complex_scenario()

    print(f"Before GC - Active instances: {len(Trackable.instances)}")
    for obj in Trackable.instances:
        print(f"  - {obj.name}")

    print("Running garbage collector...")
    collected = gc.collect()

    print(f"After GC - Collected {collected} objects.")
    print(f"After GC - Active instances: {len(Trackable.instances)}")
    for obj in Trackable.instances:
        print(f"  - {obj.name} (still alive)")

    # Clean up the kept object to see final deletions
    del kept_object
    gc.collect()
    print(f"Final Active instances: {len(Trackable.instances)}")

step_by_step_gc_working()

