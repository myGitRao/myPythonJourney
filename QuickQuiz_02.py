# Small Dictionary

mydictionary = {'baffle' : "be a mystery or bewildering to",
                'baleful' : 'deadly or sinister',
                'balk' : 'refuse to comply',
                'ban' : 'prohibit especially by law or social pressure'}
word = input("Enter the word to know its meaning : ").lower()
print(word + ": " + mydictionary.get(word))
