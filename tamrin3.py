def direct_flights(n, m, flights):

  """Calculates direct flights between cities.



  Args:

    n: Number of cities.

    m: Number of flights.

    flights: A list of tuples, where each tuple represents a flight (source, destination).



  Returns:

    A dictionary where each key is a city and the value is a list of cities it has direct flights to.

  """



  graph = {}

  for i in range(n):

    graph[i] = []



  for src, dest in flights:

    graph[src].append(dest)



  return graph



def print_results(graph):

  for city, destinations in graph.items():

    print(city)

    print(len(destinations))

    print(*destinations)




n, m = map(int, input().split())

flights = []

for _ in range(m):

  src, dest = map(int, input().split())

  flights.append((src, dest))




result = direct_flights(n, m, flights)



print_results(result)
