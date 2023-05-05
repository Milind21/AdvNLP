from deep_translator import GoogleTranslator
to_translate = 'I want to translate this text'
print(to_translate)
translated = GoogleTranslator(source='auto', target='de').translate(to_translate)
print(translated)
translated = GoogleTranslator(source='auto', target='en').translate(to_translate)
print(translated)
