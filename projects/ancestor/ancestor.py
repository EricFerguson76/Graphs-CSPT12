
def getParents(ancestors, node):
    parents = []
    for pair in ancestors:
        if pair[1] == node:
            parents.append(pair[0])
    return parents


def dft_recursive(ancestors, node, distance):
    parents = getParents(ancestors, node)

    elder = (node, distance)

    for parent in parents:
        pair = dft_recursive(ancestors, parent, distance + 1)
        if pair[1] > elder[1]:
            elder = pair

    return elder


def earliest_ancestor(ancestors, starting_node, distance=0):
    elder = dft_recursive(ancestors, starting_node, distance)

    if elder[0] == starting_node:
        return -1

    return elder[0]
