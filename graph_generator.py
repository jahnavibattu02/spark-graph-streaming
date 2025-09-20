"""
Graph Generator
---------------
Generates a random directed graph and saves:
1. Link data to a text file
2. Graph visualization as an image
"""

import random
import argparse
import logging
import networkx as nx
import matplotlib.pyplot as plt

# Setup logging for clean output
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def generate_link_data(num_nodes: int):
    """Generate random directed graph link data."""
    link_data = {}
    for node in range(num_nodes):
        # Each node gets 1–10 random links (excluding itself)
        num_links = random.randint(1, min(10, num_nodes - 1))
        links = random.sample(range(num_nodes), num_links)
        links = [link for link in links if link != node]
        link_data[node] = links
    return link_data

def write_link_data_to_file(link_data, filename: str):
    """Save graph edges to a text file."""
    with open(filename, "w") as file:
        for node, links in link_data.items():
            file.write(f"{node}: {links}\n")
    logging.info(f"Graph data written to {filename}")

def save_graph_image(link_data, filename: str):
    """Save a circular layout graph image."""
    graph = nx.DiGraph(link_data)
    labels = {n: str(n) for n in graph.nodes()}
    # Draw circular graph with labels
    nx.draw_circular(graph, labels=labels, with_labels=True,
                     node_size=500, node_color="lightblue")
    plt.savefig(filename)
    plt.close()
    logging.info(f"Graph visualization saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Generate random graph link data")
    parser.add_argument("--nodes", type=int, default=20, help="Number of nodes")
    parser.add_argument("--output", type=str, default="graph_data.txt", help="Output text file")
    parser.add_argument("--image", type=str, default="graph.png", help="Graph image file")
    args = parser.parse_args()

    # Generate graph data and save outputs
    link_data = generate_link_data(args.nodes)
    write_link_data_to_file(link_data, args.output)
    save_graph_image(link_data, args.image)

if __name__ == "__main__":
    main()
