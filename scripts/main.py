from spellchecker import SpellChecker

spell = SpellChecker(language='uz')

misspelled = spell.unknown(['sen', 'bilan', 'oqshom', 'yaxshii', "o'tdi"])

for word in misspelled:

    print(spell.correction(word))
    print(spell.candidates(word))
