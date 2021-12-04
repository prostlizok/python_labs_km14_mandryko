with open('gadsby.txt', 'r') as f:
    lines = f.readlines()
lines = [line.lower() for line in lines]

alphabet = {"a":0, "b":0, "c":0,"d":0, "e":0, "f":0,"g":0, "h":0, "i":0,"j":0, "k":0, "l":0,"m":0, "n":0, "o":0,"p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0,"y":0, "z":0}
all_letters = 0 

def letter_count(l):
    global lines
    count = 0
    for i in lines:
        for c in i:
            if c == l:
                count += 1
    return count

for i in alphabet.keys():
    alphabet[i] = letter_count(i)

alphabet = {i: d for i, d in sorted(alphabet.items(), key=lambda item: item[1], reverse=True)}

for i in alphabet.values():
    all_letters += i

val = list(alphabet.values())
key = list(alphabet.keys())

print("Most used letters:")
for i in range(5):
    print(f"{key[i]} - {val[i]} {round(((val[i]*100)/all_letters), 3)}%")
print("----------------")
print("Less used letters:")
for i in range(-5, 0):
    print(f"{key[i]} - {val[i]} {round(((val[i]*100)/all_letters), 3)}%")




