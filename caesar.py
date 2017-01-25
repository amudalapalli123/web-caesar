def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    x = letter.lower()
    if x in alphabet:
        return alphabet.index(x)



def rotate_character(char,rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if char.lower() in alphabet:

        x = alphabet_position(char)
    else:
         return char
    rot_pos = x + rot
    if rot_pos >= 26:
        rot_pos = rot_pos % 26

    if char.isupper():
        return alphabet[rot_pos].upper()
    else:
        return alphabet[rot_pos]




def encrypt(text, rot):
    new_text = ""
    for idx in range(len(text)):
        rot_char  = rotate_character(text[idx], rot )
        new_text = new_text + rot_char
    return new_text
