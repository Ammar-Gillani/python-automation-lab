filename = input("Enter file name: ")
file = open(filename, "r")

text = file.read()
file.close()

words = text.split()
total_words = len(words)

print("Total words:", total_words)
