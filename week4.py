import heapq
graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}
h = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}
def A(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    expanded = []
    processed = []
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if g != best[node]:
            continue
        processed.append(node)
        if node == goal:
            return g, path, expanded, processed
        expanded.append(node)
       
        for nxt, w in graph.get(node, []):
            ng = g + w
            if ng < best.get(nxt, float("inf")):
                best[nxt] = ng
                heapq.heappush(
                    pq,
                    (ng + h[nxt], ng, nxt, path + [nxt])
                )
    return None, [], expanded, processed

cost,path,expanded,processed = A(graph,h,"S","G")
print("Path:", " ".join(path))
print("Path Cost:", cost)
print("Processed Nodes:", processed)
print("Expanded Nodes:", expanded)
print("Expansion Count:", len(expanded))

#UCS

h_zero = {
    "S": 0,
    "A": 0,
    "B": 0,
    "C": 0,
    "G": 0
}
cost, path, expanded, processed = A(
    graph, h_zero, "S", "G"
)
print("UCS Search")
print("Path:", " -> ".join(path))
print("Path Cost:", cost)
print("Processed Nodes:", processed)
print("Expanded Nodes:", expanded)
print("Expansion Count:", len(expanded))



