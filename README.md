# 🔥 Spark Graph & Streaming Projects  

This repository **`spark-graph-streaming`** showcases classic **graph algorithms** and **real-time streaming analytics** implemented in **PySpark**.  
It is designed as a **portfolio project for Data Engineering / Big Data roles**, demonstrating your ability to work with distributed systems, graph data, and streaming pipelines.  

---

## 📌 Projects Included  

### 1. **Graph Generator (`graph_generator.py`)**  
- Generates a random directed graph.  
- Saves:  
  - Graph edges to `data/question2.txt`  
  - Visualization to `output/graph.png`.  

➡️ Used as input for **PageRank**.  

---

### 2. **Dijkstra’s Algorithm (`dijkstra.py`)**  
- Computes shortest paths from a source node using **Dijkstra’s algorithm**.  
- Input: weighted graph (`data/question1.txt`)  
- Output: shortest path + distances (`output/output_dijkstra.txt`).  

---

### 3. **PageRank (`pagerank.py`)**  
- Implements **Google’s PageRank algorithm** in PySpark.  
- Input: graph link data (`data/question2.txt`)  
- Output: ranked pages with scores (`output/pagerank_results.txt`).  

---

### 4. **Paragraph Generator (`paragraph_generator.py`)**  
- Generates random sentences to form a paragraph.  
- Example of **synthetic text generation** for testing.  
- Output: `output/paragraph.txt`.  

---

### 5. **Word Co-Occurrence Streaming (`word_cooccurrence.py`)**  
- Real-time streaming with PySpark.  
- Reads text from a TCP socket and computes **word bigrams with counts** in sliding windows.  
- Example use case: **real-time log/text analytics**.  

---
