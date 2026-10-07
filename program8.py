import heapq


class Node:
    def __init__(self, char=None, frequency=0):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

class HuffmanCoder:

    def __init__(self):
        self.root = None
        self.codes = {}

    def build_tree(self, frequencies):
        heap = []

        # Create a node for every character
        for char, freq in frequencies.items():
            node = Node(char, freq)
            heapq.heappush(heap, node)

        # Build Huffman Tree
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            new_node = Node(
                None,
                left.frequency + right.frequency
            )

            new_node.left = left
            new_node.right = right

            heapq.heappush(heap, new_node)

        self.root = heap[0]

        return self.root

    def generate_codes(self):
        self.codes = {}

        def generate(node, code):
            if node is None:
                return

            # Leaf node
            if node.char is not None:
                self.codes[node.char] = code
                return

            generate(node.left, code + "0")
            generate(node.right, code + "1")

        # Special case: only one character
        if self.root.left is None and self.root.right is None:
            self.codes[self.root.char] = "0"
        else:
            generate(self.root, "")

        return self.codes


# ------Main Program------

print("Huffman Coding")
print("--------------")

n = int(input("Enter number of characters: "))

frequencies = {}

for i in range(n):
    char = input(f"Enter character {i + 1}: ")
    freq = int(input(f"Enter frequency of {char}: "))
    frequencies[char] = freq


# Create Huffman Coder
coder = HuffmanCoder()

# Build Huffman Tree
coder.build_tree(frequencies)

# Generate Huffman Codes
codes = coder.generate_codes()


print("\nHuffman Codes:")

for char, code in codes.items():
    print(char, ":", code)