"""
Dijkstra’s Algorithm with PySpark
---------------------------------
Reads a weighted graph, computes shortest paths from a start node, and
writes results to an output file.
"""

import heapq
import argparse
import logging
from pyspark import SparkContext, SparkConf

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def read_graph(file_path: str, sc: SparkContext):
    """Load graph edges from file into adjacency list using Spark."""
    lines = sc.textFile(file_path)
    edges = lines.map(lambda line: tuple(map(int, line.strip().split(",")))).collect()

    # Convert edge list to adjacency list
    graph = {}
    for u, v, w in edges:
        graph.setdefault(u, []).append((v, w))
    return graph

def dijkstra(graph: dict, start_node: int):
    """Compute shortest paths using Dijkstra’s algorithm."""
    distances = {node: float("inf") for node in graph}
    distances[start_node] = 0
    queue = [(0, start_node)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        # Relax edges
        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            if distance < distances.get(neighbor, float("inf")):
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

def save_results(distances, output_file, start, end):
    """Save shortest path results to file."""
    with open(output_file, "w") as file:
        file.write(f"Shortest path from {start} to {end}: {distances.get(end, float('inf'))}\n")
        for node, dist in distances.items():
            file.write(f"Distance to {node}: {dist}\n")
    logging.info(f"Results written to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Dijkstra with Spark")
    parser.add_argument("--input", default="data/question1.txt", help="Input graph file")
    parser.add_argument("--output", default="output_dijkstra.txt", help="Output file")
    parser.add_argument("--start", type=int, default=0, help="Start node")
    parser.add_argument("--end", type=int, default=4, help="End node")
    args = parser.parse_args()

    # Initialize Spark context
    conf = SparkConf().setAppName("Dijkstra").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    # Run Dijkstra
    graph = read_graph(args.input, sc)
    distances = dijkstra(graph, args.start)
    save_results(distances, args.output, args.start, args.end)

    sc.stop()

if __name__ == "__main__":
    main()
