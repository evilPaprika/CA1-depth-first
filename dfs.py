from sortedcontainers import SortedSet


def find_all_in_component_recursive(nodes, node, visited, result=None):
    if not result: result = SortedSet()
    print(node)
    result.add(node)
    for child in nodes[node - 1]:
        if child not in visited | result:
            result = find_all_in_component_recursive(nodes, child, visited, result)
    return result


def dfc_find_components(nodes):
    all_nodes = set(range(1, len(nodes) + 1))
    node = 1
    visited = set()
    result = SortedSet()
    while True:
        curr_result = find_all_in_component_recursive(nodes, node, visited)
        visited.update(curr_result)
        result.add(tuple(curr_result))
        if not all_nodes - visited:
            return result
        node = (all_nodes - visited).pop()





if __name__ == '__main__':
    nodes = [[int(b) for b in a.split()[:-1:]]
                       for a in open("in.txt").read().splitlines()[1::]]
    components = dfc_find_components(nodes)
    # print("\n".join([''.join(str(i) + " " for i in s) + "0" for s in components]))
    open("out.txt", "w").write("\n".join([''.join(str(i) + " " for i in s) + "0" for s in components]))
