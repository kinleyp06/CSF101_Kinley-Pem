class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths
    def is_connected(self):
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)
    
# Test the Graph class
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()

# Test DFS
print("\nDFS starting from vertex 0:")
g.dfs(0)

# Test finding all paths
print("\nAll paths from vertex 0 to vertex 3:")
all_paths = g.find_all_paths(0, 3)
for path in all_paths:
    print(' -> '.join(map(str, path)))
# Test if the graph is connected
print("\nIs the graph connected?", g.is_connected())

# Add a disconnected vertex and test again
g.add_vertex(4)
print("After adding a disconnected vertex:")
print("Is the graph connected?", g.is_connected())

###########################################

from collections import deque
import heapq

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    def is_connected(self):
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)
    
    # Exercise 1: Find shortest path using BFS
    def shortest_path_bfs(self, start_vertex, end_vertex):
        if start_vertex not in self.graph or end_vertex not in self.graph:
            return None
            
        queue = deque([(start_vertex, [start_vertex])])
        visited = set([start_vertex])
        
        while queue:
            vertex, path = queue.popleft()
            
            if vertex == end_vertex:
                return path
                
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None  # No path exists
    
    # Exercise 2: Detect cycles in the graph
    def has_cycle(self):
        visited = set()
        
        for vertex in self.graph:
            if vertex not in visited:
                if self._has_cycle_dfs(vertex, visited, None):
                    return True
        return False
    
    def _has_cycle_dfs(self, vertex, visited, parent):
        visited.add(vertex)
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                if self._has_cycle_dfs(neighbor, visited, vertex):
                    return True
            elif neighbor != parent:
                return True
                
        return False
    
    # Exercise 3: Dijkstra's algorithm for weighted graphs
    def dijkstra(self, start_vertex, end_vertex, weights):
        # Initialize distances with infinity for all vertices
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start_vertex] = 0
        
        # Priority queue to store (distance, vertex) pairs
        pq = [(0, start_vertex)]
        previous = {}
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            # Early termination if we reached the end vertex
            if current_vertex == end_vertex:
                break
                
            # Skip if we found a better path already
            if current_distance > distances[current_vertex]:
                continue
                
            for neighbor in self.graph[current_vertex]:
                # Get the weight of the edge
                edge_weight = weights.get((current_vertex, neighbor), 1)
                if (neighbor, current_vertex) in weights:
                    edge_weight = weights[(neighbor, current_vertex)]
                
                distance = current_distance + edge_weight
                
                # Only consider this new path if it's better
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))
        
        # Reconstruct the shortest path
        path = []
        current = end_vertex
        while current != start_vertex:
            path.append(current)
            if current not in previous:
                return None  # No path exists
            current = previous[current]
        path.append(start_vertex)
        path.reverse()
        
        return path, distances[end_vertex]
    
    # Exercise 4: Check if the graph is bipartite
    def is_bipartite(self):
        color = {}
        
        for vertex in self.graph:
            if vertex not in color:
                color[vertex] = 0
                queue = deque([vertex])
                
                while queue:
                    current = queue.popleft()
                    
                    for neighbor in self.graph[current]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[current]
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
                            return False
        return True


# Test the complete implementation
if __name__ == "__main__":
    print("=== Testing Graph Implementation ===")
    
    # Create and test the basic graph
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    
    print("Graph structure:")
    g.print_graph()
    
    print("\nDFS starting from vertex 0:")
    g.dfs(0)
    
    print("\n\nBFS starting from vertex 0:")
    g.bfs(0)
    
    print("\n\nAll paths from vertex 0 to vertex 3:")
    all_paths = g.find_all_paths(0, 3)
    for path in all_paths:
        print(' -> '.join(map(str, path)))
    
    print("\nIs the graph connected?", g.is_connected())
    
    # Add a disconnected vertex and test again
    g.add_vertex(4)
    print("After adding a disconnected vertex:")
    print("Is the graph connected?", g.is_connected())
    
    # Test shortest path
    print("\nShortest path from 0 to 3 using BFS:")
    shortest_path = g.shortest_path_bfs(0, 3)
    print(' -> '.join(map(str, shortest_path)) if shortest_path else "No path exists")
    
    # Test cycle detection
    print("\nDoes the graph have a cycle?", g.has_cycle())
    
    # Test bipartite check
    print("Is the graph bipartite?", g.is_bipartite())
    
    # Create a bipartite graph for testing
    bipartite_g = Graph()
    bipartite_g.add_edge(0, 1)
    bipartite_g.add_edge(0, 3)
    bipartite_g.add_edge(1, 2)
    bipartite_g.add_edge(2, 3)
    
    print("\nBipartite graph structure:")
    bipartite_g.print_graph()
    print("Is the bipartite graph actually bipartite?", bipartite_g.is_bipartite())
    
    # Test Dijkstra's algorithm with a weighted graph
    weighted_g = Graph()
    weighted_g.add_edge(0, 1)
    weighted_g.add_edge(0, 2)
    weighted_g.add_edge(1, 2)
    weighted_g.add_edge(2, 3)
    weighted_g.add_edge(1, 3)
    
    weights = {
        (0, 1): 2, (1, 0): 2,
        (0, 2): 3, (2, 0): 3,
        (1, 2): 1, (2, 1): 1,
        (2, 3): 5, (3, 2): 5,
        (1, 3): 3, (3, 1): 3
    }
    
    print("\nWeighted graph shortest path from 0 to 3 using Dijkstra:")
    path, distance = weighted_g.dijkstra(0, 3, weights)
    print(f"Path: {' -> '.join(map(str, path))}, Distance: {distance}")