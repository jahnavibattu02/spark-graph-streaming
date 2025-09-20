"""
Paragraph Generator
-------------------
Generates a random paragraph of sentences and saves to a file.
"""

import random
import argparse
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Word lists for sentence generation
SUBJECTS = ["I", "You", "He", "She", "They", "We", "The cat", "The dog"]
VERBS = ["am", "are", "is", "feel", "look", "seem", "appear"]
OBJECTS = ["happy", "sad", "excited", "tired", "hungry", "calm"]

def generate_sentence():
    """Return a random subject-verb-object sentence."""
    return f"{random.choice(SUBJECTS)} {random.choice(VERBS)} {random.choice(OBJECTS)}."

def main():
    parser = argparse.ArgumentParser(description="Generate random paragraph")
    parser.add_argument("--sentences", type=int, default=50, help="Number of sentences")
    parser.add_argument("--output", type=str, default="paragraph.txt", help="Output file")
    args = parser.parse_args()

    # Generate random sentences
    sentences = [generate_sentence() for _ in range(args.sentences)]
    paragraph = " ".join(sentences)

    with open(args.output, "w") as file:
        file.write(paragraph)
    logging.info(f"Paragraph saved to {args.output}")

if __name__ == "__main__":
    main()
