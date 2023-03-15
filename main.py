import sys

def compression(text):
    frequencyCount = {}

    # Build a frequency table for each character in the text
    for ch in text:
        if ch not in frequencyCount:
            frequencyCount[ch] = 1
        else:
            frequencyCount[ch] += 1

    frequencyOrdered = sorted(frequencyCount.items(), key=lambda x:x[1], reverse=True)
    frequencyTable = {ch[0]:i for i, ch in enumerate(frequencyOrdered)}

    compressed = 1

    for ch in text:
        # Get position
        pos = frequencyTable[ch] + 1
        # Inset 0's
        compressed <<= pos
        # Inset the 1 for position
        compressed |= 1

    compressedRatio = (sys.getsizeof(compressed)* 100) / sys.getsizeof(text)
    


    return compressed, [x[0] for x in frequencyOrdered], compressedRatio

def deCompress(bitText, frequencyTable):
    text = ""

    i = 0
    for bit in bin(bitText)[3:]:
        if bit == "1":
            text += frequencyTable[i]
            i = 0
        else:
            i += 1

    return text

def main():
    lore = open("aaa.txt", "r").read()
    bitText, tree, cr = compression(lore)
    print("Compression ratio: ", cr)

    restored = deCompress(bitText, tree)

    print(restored == lore)


    print("Stats")
    print("Original: ", sys.getsizeof(lore))
    print("Compressed: ", sys.getsizeof(bitText))
    print("Tree: ", sys.getsizeof(tree))
if __name__ == "__main__":
    main()