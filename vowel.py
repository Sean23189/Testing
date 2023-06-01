vowel_count = 0
word = str(input("Enter a word: "))
for letter in word:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowel_count += 1

if vowel_count > 1:
    print(f"{word} has {vowel_count} vowels.")

else:
    print(f"{word} has {vowel_count} vowel.")
