from typing import List
import random

def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    # Build LPS array
    lps = [0] * len(needle)
    length = 0
    i = 1

    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    # KMP search
    i = j = 0

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1

            if j == len(needle):
                return i - j

        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return -1


class Randomizer:
    def __init__(self, stream=None):
        self.stream = iter(stream) if stream is not None else None
        self.count = 0
        self.sample = None

    def getRandom(self) -> int:
        if self.stream is None:
            return random.randint(0, 2**31 - 1)

        for item in self.stream:
            self.count += 1

            if random.randint(1, self.count) == 1:
                self.sample = item

        return self.sample

# Main program: KMP
haystack = "hello"
needle = "ll"

print("KMP Index:", strStr(haystack, needle))

# Main program: Randomizer
data = [10, 20, 30, 40, 50]
obj = Randomizer(data)

print("Random Sample:", obj.getRandom())