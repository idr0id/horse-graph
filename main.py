import string

import matplotlib.pyplot as plt
import networkx as nx

symbols: dict[int, str] = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}


def empty_table(n: int) -> nx.Graph:
    graph = nx.empty_graph()
    graph.add_nodes_from((row, col) for row in (range(1, n+1)) for col in (range(1, n+1)))
    return graph


def square_to_tuple(square: string) -> tuple[int, int]:
    symbol, number = square[0], square[1]
    keys = list(symbols.keys())
    values = list(symbols.values())
    return keys[values.index(symbol)], int(number)


def tuple_to_square(t: tuple[int, int]) -> string:
    return f'{symbols[t[0]]}{t[1]}'


def adjacency(i, j: int) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    m = [
        (i + 2, j + 1),
        (i + 2, j - 1),
        (i - 2, j + 1),
        (i - 2, j - 1),
        (i + 1, j + 2),
        (i + 1, j - 2),
        (i - 1, j + 2),
        (i - 1, j - 2),
    ]
    t = (i, j)
    return [(t, z) for z in m if 0 < z[0] <= 8 and 0 < z[1] <= 8]


if __name__ == '__main__':
    adj = empty_table(8)

    for i, j in adj.nodes():
        adj.add_edges_from(adjacency(i, j))

    result: nx.DiGraph = empty_table(8).to_directed()

    sourceSquare = square_to_tuple("B1")
    targetSquare = square_to_tuple("E3")

    path = nx.shortest_path(adj, sourceSquare, targetSquare)
    nx.add_path(result, path)

    pos = dict((n, n) for n in result.nodes())
    labels = dict(((i, j), tuple_to_square((i, j))) for (i, j) in result.nodes())
    nx.draw_networkx(result, node_size=500, node_color="tab:orange", pos=pos, labels=labels)
    plt.show()
