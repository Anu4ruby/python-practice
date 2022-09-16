#pip install googletrans
#https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group
#https://stackabuse.com/text-translation-with-google-translate-api-in-python/
#https://stackabuse.com/text-translation-with-google-translate-api-in-python/

import googletrans
from googletrans import Translator

print(googletrans.LANGUAGES)

translator = Translator()

text = input("enter the text to translate-  ")

result = translator.translate(text)

print(result.src)
print(result.dest)
print(result.origin)
print("The default translated language is english and the result is ", result.text)
print(result.pronunciation)

response = input("would you like to convert from source lang to destination lang ? press any key to continue else press enter")

if response:
    source = input("enter source language name like english, urdu, turkish etc ")
    input_text = input ("enter text to be converted- ")
    destination = input("enter destination language name like hindhi, spanish, turkish etc- ")
    result1 = translator.translate(input_text, source, destination)
    print("source language -  ", result1.src)
    print("converted to-  " , result1.dest)
    print("translated text is -  ", result1.text)
