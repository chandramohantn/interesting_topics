import gc
import sys

def demonstrate_generational_garbage_collection():
    print("=== Generational Garbage Collection Demonstration ===")

    class Node:
        def __init__(self, name):
            self.name = name
            self.next = None
            print(f"Node {self.name} created.")

        def __del__(self):
            print(f"Node {self.name} deleted.")

    def create_circular_reference():
        """
        Create nodes and form a circular reference
        """
        node1 = Node("Node1")
        node2 = Node("Node2")
        node1.next = node2
        node2.next = node1  # Circular reference
        return node1

    print("Creating circular reference...")
    circular_node = create_circular_reference()

    print(f"Reference count of circular_node: {sys.getrefcount(circular_node)}")
    print(f"Reference count of circular_node.next: {sys.getrefcount(circular_node.next)}")

    # Even if we delete the reference to circular_node, the nodes won't be deleted immediately 
    # because they reference each other (circular reference).
    del circular_node
    print("Deleted circular_node reference.")
    print("External references to the nodes still exist due to circular reference.")

    # Generational garbage collection should eventually clean this up.
    print("Forcing garbage collection...")
    gc.collect()
    print("Circular references should be cleaned up now if no external references exist.")

demonstrate_generational_garbage_collection()
