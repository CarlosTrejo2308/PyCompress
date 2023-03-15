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

    return compressed, [x[0] for x in frequencyOrdered]

def deCompress(bitText, frequencyTable):
    text = ""

    getSize = lambda x: len(bin(x)) - 2

    i = 0
    for bit in bin(bitText)[3:]:
        if bit == "1":
            text += frequencyTable[i]
            i = 0
        else:
            i += 1

    return text

def main():
    text, lst = compression("Hello World")
    print(deCompress(text, lst))

if __name__ == "__main__":
    main()

# (45226278521089, ['l', 'o', 'H', 'e', ' ', 'W', 'r', 'd'])
# 001  0001   1     1    01
# H      e      l    l    o   