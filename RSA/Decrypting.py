from .utils.extended_euclidean import chineseremaindertheorem


def openning_text(text_address):
    """Opens a text file"""
    with open(text_address, "r") as text_file:
        textr = text_file.readlines()
    result = list()
    for blocks in textr:
        blocks = blocks.replace("\n", "")
        blocks = blocks.split(" ")
        result.append(blocks)
    return result


def getting_massage(code):
    """decrypting massage out of text file"""
    massage = ''
    for block in code:
        temp = ''
        for letters in block:
            temp += chr(int(letters) - 11)
        massage += temp
    if massage[-1] == "|":
        for i in range(len(massage) - 1, 0, -1):
            if not massage[i] == "|":
                massage = massage[:i + 1]
                break
    return massage


def decrypting_method(code, private_key):
    """Using decrypting method"""
    d, n, p, q, dp, dq, qinv = private_key
    d, n, p, q, dp, dq, qinv = int(d), int(n), int(p), int(q), int(dp), int(dq), int(qinv)
    decrypted_code = list()

    for blocks in code:
        temp = []
        for codes in blocks:
            codes = int(codes)

            temp.append(str(chineseremaindertheorem(dq, dp, p, q, qinv, codes)))
        decrypted_code.append(temp)
    return decrypted_code


def getting_private_key():
    """making a private key"""
    text = openning_text("encrypted_text.txt")
    with open("private_key.txt", "r") as text_file:
        private_key = text_file.read()

    return private_key.split(), text


