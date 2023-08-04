from textblob import TextBlob

words = input('Enter words').split()
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("All Words :", words)
print("Corrected Words are :")
for i in corrected_words:
    print(i.correct(), end=" ")
