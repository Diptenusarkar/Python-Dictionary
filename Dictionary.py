print("Welcome To Python Dictionary")
ask_word = input("Enter hare : ")
word_info = {
    # Word information That you want to add in your Dictionary
    "Dog": "Dog is an Animal",
    "Cat": "Cat is an Animal",
    "Elephant": "Elephant is an Animal",
    "Donkey": "Donkey is an Animal",
    "Parrot": "Parrot is an Bard",
}
# If you have any questions please feel free to ask @Diptenusarkar ( Facebook , Twitter (Any Time) , instagram)
print(word_info.get(ask_word.capitalize(), "Sorry master. We couldn't find it."))
# capitalize "Using it means that any way you input your word, it will be collected in DOG, DoG =  Dog"CAT
