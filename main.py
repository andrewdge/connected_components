import sys

"""Returns the root of any given component"""
def findRoot(a):
    if a == parent.get(a, a):
        return a
    parent.update({a: findRoot(parent.get(a))})
    return parent.get(a)


"""Connects component a with component b"""
def connect(a, b):
    x = a
    y = b
    a = findRoot(a)
    b = findRoot(b)
    if x == a and y != b:
        parent.update({a: b})
        return
    if a != b:
        parent.update({b: a})


"""Prints all connected components, and isolated ones"""
def connectedComponents(num_vertices):
    s = set()
    for i in range(1, num_vertices + 1):
        s.add(findRoot(parent.get(i, i)))
    for i in s:
        tmp = []
        for j in parent.keys():
            if parent.get(j) == i:
                tmp.append(j)
        if tmp:
            output.append(sorted(tmp))
        else:
            output.append([i])
    print("OUTPUT: ")
    for i in output:
        if len(i) > 1:
            print(i)
    singles = sum([x for x in output if len(x) == 1], []) # all unconnected vertices
    print(f'Unconnected pieces: {singles}')


"""Runner function"""
def run(num_vertices, edge_list):
    seen = []
    for i in sum(edge_list, []):  # initializes by setting each vertex to itself
        parent[i] = i
    for i in range(len(edge_list)):
        connect(edge_list[i][0], edge_list[i][1]) # connects edges according to the edge list
    for i in parent.keys():
        connect(i, parent.get(i)) # another pass of connections, makes sure everything is connected properly
    connectedComponents(num_vertices)


if __name__ == "__main__":
    file = sys.argv[1]  # get file
    f = open(file, "r")  # open file
    c = f.read()  # get contents
    f.close()
    contents = c.split("\n")
    overhead = contents[:2]
    n_edges = overhead[0]
    n_vertices = overhead[1]
    edges = contents[2:]
    parent = {} # Union-Find data structure
    output = [] # output stored as a 2D list of components
    for j in range(len(edges)):
        nums = [int(x) for x in edges[j].split(" ")]
        edges[j] = [nums[0], nums[1]]
    run(int(n_vertices), edges)
