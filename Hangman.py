import random

words_bank = ["tree", "book", "blue", "sky", "woman", "man", "freedom"]
user_mistakes = 0

good_chars = []
bad_chars = []

x = random.randint(0, len(words_bank)-1)
word = words_bank[x]

while user_mistakes < 6:    
    for i in range(len(word)):
        if word[i] in good_chars:
            print(word[i], end=" ")

        else:
            print("_", end=" ")

    for i in range(len(word)):
        if word[i] == good_chars:
            len(good_chars) +1

        if len(word) == len(good_chars):        
            print("--------------------")
            print("👏   Good Work   👏")
            print("--------------------")
            break

    user_char = input("  write your guess: ")
    if len(user_char) == 1:

        if user_char in word:
            good_chars.append(user_char)
            print("✅")
        else:
            user_mistakes += 1
            bad_chars.append(user_char)
            print("❌")
    else:
        print("=== hoy!!  ye harf faqat ===")      

if user_mistakes == 6:
        print("---------------------")
        print("..... Game Over .....")  
        print("---------------------")

    