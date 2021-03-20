Wybierz losowo wierzchołki startowe dla cycleA oraz cycleB
for i in range(98):
    wybierz co drugi cykl do rozbudowy:
        minDistance = np.inf
        for vertex in range(100):
            if vertex w użyciu:
                contine
            distance, newCycle = findNewCycle(vertex)
            if distance < minDistance:
                minDistance = distance
                minCycle = newCycle
        Podmień cycle na minCycle w aktualnie rozbudowywanym cyklu


Funkcja - findNewCycle(vertex):
    minDistance = np.inf
    for i in range(długość rozbudowywanego cyklu + 1):
        wstaw sprawdzany vertex w miejsce "i" do aktualnego cyklu
        distance = obliczDługośćCyklu()
        if distance < minDistance:
            minDistance = distance
            minVertex = vertex
            minPath = path
    return minDistance, minPath