
#Convert Morse_code

class Morse(object):
    def __init__(self,dot='.',dash='-'):
        self.morse_table=self.MORSE_TABLE
        self.dot=dot
        self.dash=dash

    def convert(self, data):
        result=''
        for i in data:
            result+=self.morse_table.get(i,i) + ' '
        result = result[:-1].replace('.', self.dot).replace('-', self.dash)
        print(result)
        return result

    def convert_exact(self,data):
        result=''
        for i in data:
            result += (' '*self.INTER_GAP).join(list(self.morse_table.get(i,i)))+' '*self.LETTERS_GAP
        print(result)
        result = result[:-self.LETTERS_GAP].replace('.', self.dot).replace('-',  self.dash)
        print(result)
        return result

    DOT_DURATION = 1
    DAH_DURATION = 3 * DOT_DURATION
    INTER_GAP = DOT_DURATION
    LETTERS_GAP = 3 * DOT_DURATION
    WORDS_GAP = 7 * DOT_DURATION

    MORSE_TABLE={
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',

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

        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',

        '.': '.-.-.-',
        ',': '--..--',
        '?': '..--..',
        "'": '.----.',
        '!': '-.-.--',
        '/': '-..-.',
        '(': '-.--.',
        ')': '-.--.-',
        '&': '.-...',
        ':': '---...',
        ';': '-.-.-.',
        '=': '-...-',
        '+': '.-.-.',
        '-': '-....-',
        '_': '..--.-',
        '"': '.-..-.',
        '$': '...-..-',
        '@': '.--.-.',
    }