# Exercice 14 . Compression de données
# Implémente la compression RLE (Run-Length Encoding) : "aaabbcccc" → "a3b2c4"

text = input("Chaîne : ").lower()

def rle(text) :

    current_char = text[0]
    count = 1
    compressed = ""


    for letter in text[1:]:

        if letter == current_char:
            count += 1
        
        else:
            compressed += current_char + str(count)
            current_char = letter
            count = 1

    compressed += current_char + str(count)

    print(compressed)

rle(text)