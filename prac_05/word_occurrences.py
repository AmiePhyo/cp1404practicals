"""
Word Occurrences
Estimate: 30 minutes
Actual:   45 minutes
"""

text = input("Enter text: ").lower()
words = text.split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

sorted_words = sorted(word_counts.items())

max_word_length = max(len(word) for word, count in sorted_words)

for word, count in sorted_words:
    print(f"{word:<{max_word_length}} : {count}")
