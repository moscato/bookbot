with open('books/frankenstein.txt') as f:
  file_contents = f.read()
  
countVar = file_contents.split()
count = len(countVar)

print("--- Begin report: ")

print("Word Count = " + str(count))
# print(file_contents)
# ~~~~~~____~~~~~~~~~~~~~~~~~~~~~~~____~~~>>

char_count = {}

for char in file_contents.lower():
    if char.isalpha():
        char_count[char] = char_count.get(char, 0) + 1

for char, count in char_count.items():
    print(f"The '{char}' character was found {count} time{'s' if count > 1 else ''}")

print("--- End report ---")


