import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic = df.set_index('letter')['code'].to_dict()
print(nato_phonetic)

while True:

    user_word = input("Enter a word: ").upper()
    try:
        user_word_list = [word for word in user_word]
        result = [nato_phonetic[letter] for letter in user_word_list]

        print(result)
        break

    except KeyError:
        print("Sorry, only letters in the alphabet please.")


