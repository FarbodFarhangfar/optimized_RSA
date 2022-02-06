def blocking_text(text, block_size):
    """making Block in text"""
    block_list = list()
    if len(text) % block_size == 0:
        for i in range(0, len(text), block_size):
            block_list.append(text[i:i + block_size])
    else:
        for i in range(0, (len(text) - len(text) % block_size), block_size):
            block_list.append(text[i:i + block_size])
        block_list.append(text[i + block_size:].ljust(block_size, '|'))

    return block_list


def text2code(text, block_size):
    """convert text to code"""
    text = blocking_text(text, block_size)
    letters_code = list()
    for block in text:
        temp = []
        for letter in block:
            temp.append(str(ord(letter) + 11))
        letters_code.append(temp)
    return letters_code


def openning_file(adress, block_size):
    """Opens test files"""
    f = open(adress, "r")
    return text2code(f.read(), block_size)


def encrypting_method(text, public_key):
    """"""
    e, n = public_key
    e = int(e)
    n = int(n)
    encrypted_code = list()
    for code in text:
        temp = []
        for letters in code:
            letters = int(letters)

            temp.append(str(pow(letters, e, n)))
        encrypted_code.append(temp)
    return encrypted_code


def getting_public_key(text_address, public_key_address):
    """making a public key"""
    block_s = 7
    textr = openning_file(text_address, block_s)
    with open(public_key_address, "r") as text_file:
        public_keyr = text_file.read()
    return public_keyr.split(), textr


public_key, text = getting_public_key("new_text.txt", "public_key.txt")
encrypted_text = encrypting_method(text, public_key)

store = '\n'.join([str(elem) for elem in encrypted_text])
store = store.replace("['", "")
store = store.replace("']", "")
store = store.replace("', '", " ")
with open("encrypted_text.txt", "w") as text_file:
    text_file.write(store)

