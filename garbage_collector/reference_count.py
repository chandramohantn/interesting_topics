import gc
import sys

def demonstrate_reference_counting():
    print("=== Reference Counting Demonstration ===")

    # Create an object and check its reference count
    sample_list = [1, 2, 3, 4, 5]
    print(f"Initial reference count of sample_list: {sys.getrefcount(sample_list)}")

    # Create additional references to the same object
    alias1 = sample_list
    alias2 = sample_list
    print(f"Reference count after creating alias1 and alias2: {sys.getrefcount(sample_list)}")

    # Delete one reference
    del alias1
    print(f"Reference count after deleting alias1: {sys.getrefcount(sample_list)}")

    # Delete the second reference
    del alias2
    print(f"Reference count after deleting alias2: {sys.getrefcount(sample_list)}")

    # Finally, delete the original reference
    del sample_list
    print("Deleted sample_list; it should be garbage collected if no references remain.")

demonstrate_reference_counting()
