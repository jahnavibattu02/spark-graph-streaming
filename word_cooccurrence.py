"""
Word Co-Occurrence with Spark Streaming
---------------------------------------
Streams text data over TCP, generates word bigrams, counts them in a sliding window,
and prints results in real time.
"""

import re
import argparse
import logging
from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def clean_text(text):
    """Preprocess line: remove punctuation, lowercase, split into words."""
    return re.sub(r"[^\w\s]", "", text).lower().split()

def create_bigrams(words):
    """Generate bigrams (pairs of consecutive words)."""
    return list(zip(words, words[1:]))

def main():
    parser = argparse.ArgumentParser(description="Word Co-Occurrence with Spark Streaming")
    parser.add_argument("--host", default="localhost", help="TCP host")
    parser.add_argument("--port", type=int, default=9999, help="TCP port")
    args = parser.parse_args()

    # Initialize Spark streaming context (batch size = 5 sec)
    conf = SparkConf().setAppName("CoOccurrenceBigrams").setMaster("local[2]")
    sc = SparkContext(conf=conf)
    ssc = StreamingContext(sc, 5)

    # Stream text from TCP
    stream = ssc.socketTextStream(args.host, args.port)

    # Tokenize → bigrams → count
    words = stream.flatMap(clean_text)
    bigrams = words.transform(lambda rdd: rdd.mapPartitions(
        lambda part: [create_bigrams(list(part))]).flatMap(lambda x: x))
    counts = bigrams.map(lambda b: (b, 1)).reduceByKey(lambda a, b: a + b)

    # Print bigram counts
    counts.pprint()

    # Start streaming
    ssc.start()
    ssc.awaitTermination()

if __name__ == "__main__":
    main()
