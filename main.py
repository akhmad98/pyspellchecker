# from spellchecker import SpellChecker

# spell = SpellChecker(language=None)

# # spell.word_frequency.load_text_file('uz_full.txt', encoding='utf-8')

# t = spell.word_frequency.load_dictionary("./pyspellchecker/scripts/data/sample.json")
# spell.word_frequency.load_text_file('uz.txt')
# # spell.word_frequency.load_words(['keyn', 'usmoniylar', "yo'q"])
# s = spell.known(['usmoniylar', 'keyn'])  # will return both now!
# print(s)
# spell.word_frequency.load_text_file('ttsuzbot.txt', encoding='utf-8')


# spell.remove(["sike", "sikaman", "sskee", "traxa", "viiiiiiiiiiii", "yibanlarim"]) # I don't like 'the'
from collections import Counter
import re
import pandas as pd
fields = ['content']

# csv filelar uchun
df = pd.read_csv('./pyspellchecker/daryo_contents.csv', skipinitialspace=True, usecols=fields)
#text file lar uchun
dp = pd.read_csv('uz.txt')
matn = (df.content).to_string(index=False)
# text file lar uchun
matn1 = (dp).to_string(index=False)
kichik_matn = str(matn + matn1).lower()
kichik_matn = re.sub("[^\w ]", "", kichik_matn)

# print("Cleaned sentence is:", kichik_matn)

words = kichik_matn.split(" ")
s = Counter(words)
print(type(s))
print(s['keng'])
lss = []
obj = {}
for i in s:
    obj[i] = s[i]

print(obj)    
import json
with open("sample.json", "w") as outfile:
    json.dump(obj, outfile)
