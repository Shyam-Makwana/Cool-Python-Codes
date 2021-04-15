phrase = str(input("Enter a Phrase : "))
phrase_split = phrase.split(" ")
acronym = ""
for i in phrase_split:
    acronym += i[0].upper()
print(acronym)
