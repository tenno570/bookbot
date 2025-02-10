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
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lower_contents = file_contents.lower
        print (lower_contents)
        alphabet =[alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']







character_count()
