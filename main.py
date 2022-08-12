import unicodedata

# Dictionary with the relationship between word-code
# Dicionário contendo a relação letra-código
WORD_MORSE = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}


def encode(normal_text):
    # Cleaning the text to have no difference in the dictionary
    # Limpando o text para não ter diferença no dicionário
    text = unicodedata.normalize('NFD', normal_text).encode(
        'ascii', 'ignore').decode("utf-8").lower()

    morse = ''

    for word in text:
        # To not have problem with symbols out the standart of morse code
        # Para não ter problemas com símbolos fora do padrão do código morse
        if word in WORD_MORSE:
            morse += WORD_MORSE[word] + ' '

    return f'\nMorse Code\n{morse}'


to_morse = encode(input('Text: '))
print(to_morse)
