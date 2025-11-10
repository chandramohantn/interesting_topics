import gc

def explain_gc_collect():
    print("=== What gc.collect() Actually Does ===")
    
    # Check current state
    print(f"Before gc.collect():")
    print(f"  GC counts (gen0, gen1, gen2): {gc.get_count()}")
    print(f"  GC thresholds: {gc.get_threshold()}")
    
    # Create some garbage to collect
    def create_garbage():
        # Create objects that will become garbage
        data = []
        for i in range(1000):
            # Create circular references
            obj1 = [f"object_{i}_a"]
            obj2 = [f"object_{i}_b"] 
            obj1.append(obj2)
            obj2.append(obj1)
            data.append(obj1)
        return data
    
    garbage_data = create_garbage()
    print(f"After creating garbage - GC counts: {gc.get_count()}")
    
    # Delete references to make objects unreachable
    del garbage_data
    print(f"After deleting references - GC counts: {gc.get_count()}")
    
    # Now call gc.collect()
    print("\nCalling gc.collect()...")
    collected = gc.collect()
    
    print(f"After gc.collect():")
    print(f"  Collected {collected} objects")
    print(f"  GC counts: {gc.get_count()}")
    print(f"  Objects in gc.garbage: {len(gc.garbage)}")

explain_gc_collect()