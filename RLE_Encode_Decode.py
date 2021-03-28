#  ------------- RLE encoding and decoding functions
def encode(input_text):
    prev_symbol = ""
    encoded_text = ""
    counter = 1

    for symbol in input_text:
        if symbol != prev_symbol:
            if counter > 1:
                encoded_text += str(counter)
            encoded_text += symbol
            counter = 1
        else:
            counter += 1
        prev_symbol = symbol

    if counter > 1:
        encoded_text += str(counter)

    return encoded_text


def decode(input_text):
    prev_symbol = ""
    decoded_txt = ""
    digit_ = ""

    for symbol in input_text:

        if symbol.isdigit():
            digit_ += symbol
        else:
            if digit_:
                decoded_txt += prev_symbol * (int(digit_) - 1)
            decoded_txt += symbol
            digit_ = ""
            prev_symbol = symbol

    if digit_:
        decoded_txt += prev_symbol * (int(digit_) - 1)

    return decoded_txt


txt1 = "aaaaaaaabbbbbbbbbaaaaaaaaaaaa"  # a8b9a12
txt2 = "aabbbaaa"
txt3 = "AABBCCDD"
txt4 = "sdfdfggdfjj"

enc_txt1 = "a8b9a12"
enc_txt2 = "a2b3a3"
enc_txt3 = "A2B2C2D2"
enc_txt4 = "sdfdfg2dfj2"

txt = txt4
if txt != decode(encode(txt)):
    print("Wrong")
    print("txt =    " + txt)
    print("encode = " + encode(txt))
    print("decode = " + decode(txt))
else:
    print("Success")
