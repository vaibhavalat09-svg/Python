def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count += 1

    print("Total vowels =", count)

count_vowels("Python Programming")