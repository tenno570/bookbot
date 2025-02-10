def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print (file_contents)

def words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lower_contents = file_contents.lower
        words = file_contents.split()
        counts = len(words)
        print (counts)

def character_count():
    counts = {}
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lower_contents = file_contents.lower()
        for x in lower_contents:
            if x in counts :
                counts[x] += 1
            else :
                counts[x] = 1
            
                
    print (counts)


character_count()
