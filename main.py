import sys
import pickle

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
    # Use the terminal to run this file
    # First paramethor can be compress or decompress
    # Second paramethor is the file name

    if sys.argv[1] == "compress" or sys.argv[1] == "c":
        inputFile = open(sys.argv[2], "r").read()
        print("Compressing file...")
        bitText, tree, cr = compression(inputFile)
        print("Compression ratio: ", cr)
        print("Writing to file...")

        filename = sys.argv[2].split(".")[0]

        pickle.dump(bitText, open(filename + ".cp", "wb"))
        pickle.dump(tree, open(filename + ".cp.tree", "wb"))

        print("Done!")

    elif sys.argv[1] == "decompress" or sys.argv[1] == "d":
        filename = sys.argv[2].split(".")[0]

        bitText = pickle.load(open(filename + ".cp", "rb"))
        tree = pickle.load(open(filename + ".cp.tree", "rb"))

        print("Decompressing file...")

        text = deCompress(bitText, tree)

        print("Writing to file...")

        open("restored_" + filename + ".txt", "w").write(text)

        print("Done!")
if __name__ == "__main__":
    main()