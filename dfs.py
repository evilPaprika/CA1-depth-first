from sortedcontainers import SortedSet


def find(nodes):
    stack = [1]
    result = [SortedSet()]
    while stack:
        vertex = stack.pop() - 1
        for child in nodes[vertex]:
            if child not in result[len(result)-1]:
                stack.append(child)
                result[len(result)-1].add(child)
        if len(stack) == 0 and sum(len(s) for s in result) < len(nodes):
            stack.append((set(range(1, len(nodes) + 1)) -
                          set(item for sublist in result for item in sublist)).pop())
            result.append(SortedSet())

    return result


if __name__ == '__main__':
    components = find([[int(b) for b in a.split()[:-1:]]
                       for a in open("in.txt").read().splitlines()[1::]])
    # print("\n".join([''.join(str(i) + " " for i in s) + "0" for s in components]))
    open("out.txt", "w").write("\n".join([''.join(str(i) + " " for i in s) + "0" for s in components]))
