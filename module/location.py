import heapq

dijkstra_graph = {
    "Kibagabaga": {"Nyarutarama": [3.7, 8], "Kanombe": [2.9, 7]},
    "Nyarutarama": {"Kibagabaga": [3.7, 8], "Kanombe": [6.0, 14], "Remera KFC": [4.0, 8], "Gishushu": [2.1, 5],
                    "Kacyiru": [3.8, 10]},
    "Remera KFC": {"Nyarutarama": [4.8, 8], "Gishushu": [2.9, 5], "Kacyiru": [6.3, 10]},
    "Kanombe": {"Nyarutarama": [6.0, 14], "Kibagabaga": [2.9, 5]},
    "Gishushu": {"Remera KFC": [2.9, 5], "Nyarutarama": [2.1, 5]},
    "Kacyiru": {"Remera KFC": [6.3, 10], "Nyarutarama": [3.7, 8]}
}


def choose_location():
    src = None
    print("Select your current location")
    print("1.Kibagabaga\n2.Nyarutarama\n3.Kanombe\n4.Gishushu\n5.Kacyiru")
    while True:
        try:
            choice = int(input("Enter the choice of your current location: "))
            while choice > 5 or choice < 1:
                print("Invalid choice try again")
                choice = int(input("Enter the choice of your current location: "))
            break
        except ValueError:
            print("Invalid choice. Try again")

    if choice == 1:
        src = "Kibagabaga"
        distances = dijkstra(dijkstra_graph, "Remera KFC")
        print("\nRemera KFC to " + src)
        printing(distances, "Remera KFC", src)

    elif choice == 2:
        src = "Nyarutarama"
        distances = dijkstra(dijkstra_graph, "Remera KFC")
        print("\nRemera KFC to " + src)
        printing(distances, "Remera KFC", src)

    elif choice == 3:
        src = "Kanombe"
        distances = dijkstra(dijkstra_graph, "Remera KFC")
        print("\nRemera KFC to " + src)
        printing(distances, "Remera KFC", src)

    elif choice == 4:
        src = "Gishushu"
        distances = dijkstra(dijkstra_graph, "Remera KFC")
        print("\nRemera KFC to " + src)
        printing(distances, "Remera KFC", src)

    elif choice == 5:
        src = "Kacyiru"
        distances = dijkstra(dijkstra_graph, "Remera KFC")
        print("\nRemera KFC to " + src)
        printing(distances, "Remera KFC", src)

    return src


def printing(distances, start_node, target_node):
    print("The total distance from Remera KFC to your destination is:  " + str(distances[target_node][0]) + " km")
    print("The total time it will take for the  for the delivey is:  " + str(distances[target_node][1]) + " minutes")


def dijkstra(graph, start):
    """Visit all nodes and calculate the shortest paths to each from start"""
    queue = [(0, start)]
    distances = {start: [0, 0]}
    visited = set()

    while queue:
        _, node = heapq.heappop(queue)  # (distance, node), ignore distance
        if node in visited:
            continue
        visited.add(node)
        dist = distances[node][0]
        for neighbour, neighbour_dist in graph[node].items():
            if neighbour in visited:
                continue
            neighbour_dist[0] += dist
            neighbour_dist1 = distances.get(neighbour, [999999, 999999])
            if neighbour_dist < neighbour_dist1:
                heapq.heappush(queue, (neighbour_dist, neighbour))
                distances[neighbour] = neighbour_dist

    return distances


if __name__ == "__main__":
    choose_location()

