from deep_translator import GoogleTranslator


def translateSinhala(text):
    return GoogleTranslator(source='auto', target='si').translate(text)


def translate(text, target_language):
    return GoogleTranslator(source='auto', target=target_language).translate(text)
