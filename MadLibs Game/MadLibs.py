print("*"*30)
print("\tMad Libs Game")
print("*"*30)
excl = str(input("\nEnter any exclamation word : "))
adverb = str(input("Enter any adverb : "))
noun = str(input("Enter any noun : "))
adj = str(input("Enter any adjective : "))

sentence = "\n{}! he said {} as he jumped into his convertible {} and drove off with his {} wife."

print(sentence.format(excl,adverb,noun,adj))

# Ouch! he said stupidly as he jumped into his convertible cat and drove off with his brave wife.