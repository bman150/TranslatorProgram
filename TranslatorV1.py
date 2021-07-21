# Written by Alexander Baker on 07/16/2021
from googletrans import Translator

translator = Translator()
usertext = input('Enter a word or sentence: ')
translations = translator.translate(usertext, dest='en')
print(translations.origin, ' -> ', translations.text)