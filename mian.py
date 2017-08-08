from nltk.corpus import words
import time
# TODO : Brute force solutions for vignere: kasisky and kerckhoffs
# DONE : dictionary


def noting(data):
    data = list(data)
    for i in range(0, len(data)):
        if data[i] == "1":
            data[i] = "0"
        else:
            data[i] = "1"
        print(data[i], end='')


def xoring(data, key):
    key = list(key)
    data = list(data)
    j = 0
    for i in range(0, len(data)):
        if j > len(key) - 1:
            j = 0
        if data[i] == "1" and key[j] == "1":
            data[i] = "0"
        elif data[i] == "1" and key[j] == "0":
            data[i] = "1"
        elif data[i] == "0" and key[j] == "1":
            data[i] = "1"
        else:
            data[i] = "0"
        print(data[i], end='')
        j += 1


def anding(data, key):
    key = list(key)
    data = list(data)
    j = 0
    for i in range(0, len(data)):
        if j > len(key) - 1:
            j = 0
        if data[i] == "1" and key[j] == "1":
            data[i] = "1"
        elif data[i] == "1" and key[j] == "0":
            data[i] = "0"
        elif data[i] == "0" and key[j] == "1":
            data[i] = "0"
        else:
            data[i] = "0"
        print(data[i], end='')
        j += 1


def oring(data, key):
    key = list(key)
    data = list(data)
    j = 0
    for i in range(0, len(data)):
        if j > len(key) - 1:
            j = 0
        if data[i] == "1" and key[j] == "1":
            data[i] = "1"
        elif data[i] == "1" and key[j] == "0":
            data[i] = "1"
        elif data[i] == "0" and key[j] == "1":
            data[i] = "1"
        else:
            data[i] = "0"
        print(data[i], end='')
        j += 1


def nanding(data, key):
    key = list(key)
    data = list(data)
    j = 0
    for i in range(0, len(data)):
        if j > len(key) - 1:
            j = 0
        if data[i] == "1" and key[j] == "1":
            data[i] = "0"
        elif data[i] == "1" and key[j] == "0":
            data[i] = "1"
        elif data[i] == "0" and key[j] == "1":
            data[i] = "1"
        else:
            data[i] = "1"
        print(data[i], end='')
        j += 1


def noring(data, key):
    key = list(key)
    data = list(data)
    j = 0
    for i in range(0, len(data)):
        if j > len(key) - 1:
            j = 0
        if data[i] == "1" and key[j] == "1":
            data[i] = "0"
        elif data[i] == "1" and key[j] == "0":
            data[i] = "0"
        elif data[i] == "0" and key[j] == "1":
            data[i] = "0"
        else:
            data[i] = "1"
        print(data[i], end='')
        j += 1


def polybius_decode(message):
    # done
    a = ["A", "B", "C", "D", "E", "F"]
    b = ["G", "H", "I", "J", "K", "L"]
    c = ["M", "N", "O", "P", "Q", "R"]
    d = ["S", "T", "U", "V", "W", "X"]
    e = ["Y", "Z", "0", "1", "2", "3"]
    f = ["4", "5", "6", "7", "8", "9"]
    v = [a, b, c, d, e, f]
    code = []
    check = True
    while check:
        # try:
        for i in range(0, len(message), 2):
            u = int(message[i])
            t = int(message[i + 1])
            code.append(v[u][t])
        check = False
        # except:
        # print("invalid input")
        # break
    formatting(code)


def polybius_encode(message):
    a = ["A", "B", "C", "D", "E", "F"]
    b = ["G", "H", "I", "J", "K", "L"]
    c = ["M", "N", "O", "P", "Q", "R"]
    d = ["S", "T", "U", "V", "W", "X"]
    e = ["Y", "Z", "0", "1", "2", "3"]
    f = ["4", "5", "6", "7", "8", "9"]
    v = [a, b, c, d, e, f]
    code = []
    out = ""
    for i in range(0, len(message)):
        code.append(
            [(index, row.index(message[i].upper())) for index, row in enumerate(v) if message[i].upper() in row])
        out += str(code[i])
        # out.append(code[i][i+1])
    # formating(out)
    out = out.replace("[(", "")
    out = out.replace(")]", "")
    out = out.replace(", ", "")
    out = ''.join(e for e in out if e.isalnum())
    print(out)
    # or i in range(0,len(code):

    # p = ''.join(str(code[i][i]))


def formatting(arr):
    for i in range(0, len(arr)):
        print(arr[i], end='')
    print("\n")


def shift_encode(message, shift):
    x = []
    if shift >= 26:
        shift = shift % 26
    for i in range(0, len(message)):
        message_int = ord(message[i])
        if message_int + shift > 122:
            message_int = message_int + shift - 26
        else:
            message_int += shift
        x.append(chr(message_int))
    formatting(x)


def shift_decode(message, shift):
    x = []
    if shift >= 26:
        shift = shift % 26
    for i in range(0, len(message)):
        message_int = ord(message[i])
        if message_int - shift < 97:
            message_int = message_int + 26
        message_int -= shift
        x.append(chr(message_int))
    formatting(x)


def shift_brute(message):
    x = []
    for i in range(0, 26):
        for j in range(0, len(message)):
            temp = ord(message[j])
            if temp + i > 122:
                temp = temp + i - 26
            else:
                temp += i
            x.append(chr(temp))
        formatting(x)
        x = []


def vignere_encode(message, key):
    x = []
    dex = 0
    for i in range(0, len(message)):
        if dex % len(key) == 0:
            dex = 0
        temp = ord(message[i])
        temp = temp + (ord(key[dex]) - 97)
        if temp < 97:
            temp = temp + 26
        elif temp > 122:
            temp = temp - 26
        dex += 1
        x.append(chr(temp))
    formatting(x)


def vignere_decode(message, key):
    x = []
    dex = 0
    for i in range(0, len(message)):
        if dex % len(key) == 0:
            dex = 0
        temp = ord(message[i])
        temp = temp - (ord(key[dex]) - 97)
        if temp < 97:
            temp = temp + 26
        elif temp > 122:
            temp = temp - 26
        dex += 1
        x.append(chr(temp))
    formatting(x)
    return x


def search(sub_string):
    # TODO : finish search function, narrow results
    matching = []
    with open('word_lists.txt', 'r') as f:
        word_list = f.readlines()
    for i in range(0, len(word_list)):
        word_list[i].replace('\n', '')
        if word_list[i] in str(sub_string):
            # print('check')
            matching.append(sub_string)
    return matching


def vignere_brute(message):
    good_words = []
    x = []
    file = open('test_data.txt', 'r+')
    file.truncate()
    word_list = words.words('en')
    for i in range(0, len(word_list)):
        if len(word_list[i]) > len(message) or '-' in word_list[i]:
            continue
        else:
            l = vignere_decode(message, word_list[i])
            s = ''.join(l)
            file.write("Solution:")
            file.write(s)
            file.write('\n')
            file.write("Key:")
            file.write(word_list[i])
            file.write('\n')
            file.write('\n')
            x.append(s)
    print("Data available in test_data.txt")
    print("Showing results containing common english words")
    time.sleep(1)
    for i in range(0, len(x)):
        good_words.append(search(x[i]))
        # good_words.append('\n')
    formatting(good_words)


def main():
    fun = True
    while fun:
        begin = str(input("0 = gates 1 = polybius 2 = shift 3 = vignere"))
        if begin == "0":
            x = str(input("0 = NOT 1 = AND 2 = OR 3 = NAND 4 = XOR 5 = NOR"))
            data = str(input("input data"))
            if x == "0":
                noting(data)
            elif x == "1":
                key = str(input("input key"))
                anding(data, key)
            elif x == "2":
                key = str(input("input key"))
                oring(data, key)
            elif x == "3":
                key = str(input("input key"))
                nanding(data, key)
            elif x == "4":
                key = str(input("input key"))
                xoring(data, key)
            elif x == "5":
                key = str(input("input key"))
                noring(data, key)
            else:
                print("invalid input")
            print('')
        elif begin == "1":
            print("choose mode 0 = decode 1 = encode")
            hi = str(input())
            print("input message")
            message = str(input())
            message = ''.join(e for e in message if e.isalnum())
            if hi == "0":
                # return message
                polybius_decode(message)
            elif hi == "1":
                # return message
                polybius_encode(message)
            else:
                print("invalid input")
        elif begin == "2":
            yuy = str(input("0 = encode 1 = decode 2 = brute"))
            message = str(input("input message"))
            if yuy == "0":
                shift = int(input("input shift"))
                shift_encode(message, shift)
            elif yuy == "1":
                shift = int(input("input shift"))
                shift_decode(message, shift)
            elif yuy == "2":
                shift_brute(message)
            else:
                print("invalid input")
        elif begin == "3":
            yuy = str(input("0 = encode 1 = decode 2 = brute"))
            message = str(input("input message"))
            if yuy == "0":
                key = str(input("input key"))
                vignere_encode(message, key)
            elif yuy == "1":
                key = str(input("input key"))
                vignere_decode(message, key)
            elif yuy == "2":
                vignere_brute(message)
            else:
                print("invalid input")
        else:
            print("invalid input")


main()
