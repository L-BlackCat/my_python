
print('Enter  the  English  message  to  translate  into  Pig  Latin:')
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
message = input()

pigLatin = []
for word in message.split():
    #   首先检测前缀或者后缀是否是非字母，保证world是一串字母
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]


    isUpper = word.isupper()
    isTitle = word.istitle()

    word = word.lower()

    suffixConsonant = ''

    while len(word) > 0 and word[0] not in VOWELS:
        suffixConsonant += word[0]
        word = word[1:]



    if suffixConsonant == '':
        word = word + 'yay'
    else:
        word += suffixConsonant + 'ay'

    if isTitle:
        word = word.title()

    if isUpper:
        word = word.upper()

    if len(prefixNonLetters) > 0:
        word = prefixNonLetters + word

    if len(suffixNonLetters) > 0:
        word = word + suffixNonLetters

    pigLatin.append(word)

print(' '.join(pigLatin))
