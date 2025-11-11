# Memory Leak: Files not closed properly
def read_files_leaky(filenames):
    contents = []
    for filename in filenames:
        f = open(filename, 'r')
        contents.append(f.read())
        # Missing f.close() leads to memory leak
    return contents

# Fixed Version: Using context manager to ensure files are closed
def read_files_fixed(filenames):
    contents = []
    for filename in filenames:
        with open(filename, 'r') as f:
            contents.append(f.read())
    return contents
