from nltk.corpus import words
import time
# TODO : add comments, make prints more descriptive
# DONE : dictionary


def noting(data):
    """
    :param data:
    :return:
    """
    data = list(data)
    for i in range(0, len(data)):
        if data[i] == "1":
            data[i] = "0"
        else:
            data[i] = "1"
        print(data[i], end='')


def xoring(data, key):
    """
    :param data:
    :param key:
    :return:
    """
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
    """
    :param data:
    :param key:
    :return:
    """
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
    """
    :param data:
    :param key:
    :return:
    """
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
    """
    :param data:
    :param key:
    :return:
    """
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
    """
    :param data:
    :param key:
    :return:
    """
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
    """
    :param message:
    :return:
    """
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
        try:
            for i in range(0, len(message), 2):
                u = int(message[i])
                t = int(message[i + 1])
                code.append(v[u][t])
            check = False
        except ValueError:
            print("invalid input")
            break
    formatting(code)


def polybius_encode(message):
    """
    :param message:
    :return:
    """
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
    """
    :param arr:
    :return:
    """
    for i in range(0, len(arr)):
        print(arr[i], end='')
    print("\n")


def alt_formatting(arr):
    for i in range(0, len(arr)):
        print(arr[i], end='')
        print("\n")


def shift_encode(message, shift):
    """
    :param message:
    :param shift:
    :return:
    """
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
    """
    :param message:
    :param shift:
    :return:
    """
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
    """
    :param message:
    :return:
    """
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
    """
    :param message:
    :param key:
    :return:
    """
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
    """
    :param message:
    :param key:
    :return: x
    """
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
    # print(x)
    x = ''.join(x)
    return x


def search(sub_string, word_data):
    """
    :param word_data:
    :param sub_string:
    :return:
    """
    matching = []
    file = open('test_data_two.txt', 'a')
    with open(word_data, 'r') as f:
        word_list = f.readlines()
    for i in range(0, len(word_list)):
        current_word = word_list[i]
        current_word = ''.join(ch for ch in current_word if ch.isalnum())
        if current_word in sub_string and len(current_word) > 2:
            matching.append(sub_string)
            file.write("Solution: ")
            file.write(sub_string)
            file.write('\n')
            file.write("Word found: ")
            file.write(current_word)
            file.write('\n')
            file.write('\n')
            break
    return matching


def vignere_brute(message):
    """
    :param message:
    :return:
    """
    x = []
    file = open('test_data.txt', 'r+')
    file.truncate()
    word_list = words.words('en')
    for i in range(0, len(word_list)):
        if len(word_list[i]) > len(message) or '-' in word_list[i]:
            continue
        else:
            l = vignere_decode(message, word_list[i])
            # saving_data(l, word_list[i])
            # s = ''.join(l)
            file.write("Solution:")
            file.write(l)
            file.write('\n')
            file.write("Key:")
            file.write(word_list[i])
            file.write('\n')
            file.write('\n')
            x.append(l)
    print("Data available in test_data.txt")
    print("Showing results containing common english words")
    time.sleep(1)
    check = True
    num_check = 0
    lists = ['word_lists_500.txt', 'word_lists_2500.txt', 'word_lists_5000.txt', 'word_lists_10000.txt']
    while check:
        good_words = []
        for i in range(0, len(x)):
            g = search(x[i], lists[num_check])
        # print(g)
            good_words = good_words + g
        # good_words.append('\n')
        # alt_formatting(good_words)
        print("Data available in test_data_two.txt")
        he = str(input("Continue with wider search parameters? y/n"))
        if he == 'y':
            print('Loading...')
            num_check += 1
            # continue
        else:
            check = False


def vignere_examination_count(message):
    # brute force finds 3 letter repeated sequences and returns as array //DONE
    """
    :param message:
    :return groups:
    """
    groups = []
    for i in range(0, len(message)):
        sequence = str(message[i:i + 3])
        if len(sequence) < 3:
            continue
        else:
            groups.append(sequence)
    return groups


def vignere_examination_distance(groups):
    # use results from vignere_examination_count to get the distance between them //DONE
    """
    :param groups:
    :return repeat:
    :return first_distance:
    """
    count = 0
    repeated = ''
    for i in range(0, len(groups)):
        if groups[count] == 'xxx':
            count += 1
        else:
            break
    repeat = groups[count]

    # start_pos = groups.index(repeat)
    # print(groups, '\n', message)
    return distance


def factorisation(message):
    # given array of 3 letter sequences
    # by calculating difference between identical strings
    # TODO: get most common factor, which is len of key
    groups = vignere_examination_count(message)
    factors = []
    for i in range(0, len(groups)):
        distance = vignere_examination_distance(groups)
        factors.append(distance)
        for k in range(len(groups)):
            groups = ['xxx' if x == groups[k] else x for x in groups]
    print(factors)

# def vignere_examination_crack(distance, start_pos, message):
#     # To be rewritten
#     # cipher_text = []
#     # for i in range(start_pos, len(message), distance):
#     #     cipher_text.append(message[i])
#     # shift_brute(''.join(cipher_text))
#     # for start_pos in range(start_pos, start_pos + distance):
#     #     for i in range():
#     #     cipher_text = message[start_pos]
#     return distance, start_pos


def vignere_examination_main(message):
    factorisation(message)
    # TODO: factor distances, most common factor is key len
    # TODO: implement this into dictionary brute force
    # TODO: divide and shift brute-force depending on key len
    # ignore vignere_examination_crack and _main, currently ded
    # https://en.wikipedia.org/wiki/Kasiski_examination
    # factors = []
    # # nugciloygcmxjeenoakmrpafgilutbnlewntvhxukrksunuxcnwoygcmxkslvienlnpa key: cat
    # groups = vignere_examination_count(message)
    # distance, start_pos = vignere_examination_distance(groups)
    # factors.append(distance)
    # vignere_examination_crack(distance, start_pos, message)
    # for i in range(0, len(groups)):
    #     groups = [x for x in groups if x != key and key > 1]
    #     distance, start_pos = vignere_examination_distance(groups)
    #     vignere_examination_crack(distance, start_pos, message)
    # # for i in range(0, key):


def main():
    file = open('test_data.txt', 'r+')
    file.truncate()
    file_two = open('test_data_two.txt', 'r+')
    file_two.truncate()
    """
    :return:
    """
    fun = True
    while fun:
        begin = str(input("0 = Logic gates 1 = Polybius 2 = Shift/Caeser 3 = Vigenere x = Exit"))
        if begin == "0":
            print("Basic logic gates, input binary and key to get output.")
            x = str(input("0 = NOT 1 = AND 2 = OR 3 = NAND 4 = XOR 5 = NOR"))
            data = str(input("Input data"))
            if x == "0":
                noting(data)
            elif x == "1":
                key = str(input("Input key"))
                anding(data, key)
            elif x == "2":
                key = str(input("Input key"))
                oring(data, key)
            elif x == "3":
                key = str(input("Input key"))
                nanding(data, key)
            elif x == "4":
                key = str(input("Input key"))
                xoring(data, key)
            elif x == "5":
                key = str(input("Input key"))
                noring(data, key)
            else:
                print("Invalid input")
            print('')
        elif begin == "1":
            print('The polybius cipher uses a square of letters to convert a plaintext message to numbers.')
            print("Choose mode 0 = decode 1 = encode")
            hi = str(input())
            print("Input message")
            message = str(input())
            message = ''.join(e for e in message if e.isalnum())
            if hi == "0":
                polybius_decode(message)
            elif hi == "1":
                polybius_encode(message)
            else:
                print("invalid input")
        elif begin == "2":
            print('Caeser or shift cipher, which works by shifting the alphabet a number of positions.')
            yuy = str(input("0 = Encode 1 = Decode 2 = Brute force"))
            message = str(input("Input message"))
            if yuy == "0":
                shift = int(input("Input shift (integer)"))
                shift_encode(message, shift)
            elif yuy == "1":
                shift = int(input("input shift (integer)"))
                shift_decode(message, shift)
            elif yuy == "2":
                shift_brute(message)
            else:
                print("Invalid input")
        elif begin == "3":
            print('Vignere cipher is a polyalphabetic cipher.')
            yuy = str(input("0 = Encode 1 = Decode 2 = Brute"))
            message = str(input("Input message"))
            if yuy == "0":
                key = str(input("Input key"))
                vignere_encode(message, key)
            elif yuy == "1":
                key = str(input("Input key"))
                vignere_decode(message, key)
            elif yuy == "2":
                if len(message) > 8:
                    print('Using cryptanalysis...')
                    vignere_examination_main(message)
                else:
                    print('Using brute-force solution...')
                    vignere_brute(message)
            else:
                print("invalid input")
        elif begin == 'x':
            exit(0)
        elif begin == 't':
            print("Opening test area...")
            message = str(input("Input message"))
            vignere_examination_main(message)
        else:
            print("invalid input")


main()
