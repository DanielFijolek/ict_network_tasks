import binascii
import random


def read():
    with open("img.png", "rb") as f:
        text = f.read()
    str_bin = []
    for x in text:
        str_bin.append(str(bin(x).lstrip('0b')).zfill(8))
    return arr_to_str(str_bin)


def write(name, source):
    with open(name, "w") as wr:
        wr.write(source)


def check_if_even(byte_check):
    y = 0
    check_even = 0
    for x in byte_check:
        y += int(x)
    if y % 2 == 0:
        check_even = 1
    print(check_even)
    byte_check += str(check_even)
    return byte_check


def check_modulo(byte_check):
    y = 0
    modulo = 0
    for x in byte_check:
        y += int(x)
    modulo = y % 128
    str_modulo = str(bin(modulo).lstrip('0b')).zfill(8)
    print(str_modulo)
    byte_check += str(str_modulo)
    return byte_check


def sending_message(str_bit):
    list_bit = list(str_bit)
    n = len(list_bit) % 1000
    for x in range(n):
        i = random.randint(0, len(list_bit))
        if list_bit[i] == 0:
            list_bit[i] = '1'
        else:
            list_bit[i] = '0'
    return (''.join(list_bit))


def crc(crc, str_bit):
    p = []
    for x in str_bit:
        p.append(int(x))
    crc = 0xffffffff & ~crc
    for i in range(len(p)):
        crc = crc ^ p[i]
    for j in range(8):
        crc = (crc >> 1) ^ (0xedb88320 & -(crc & 1))
    return str_to_bit(0xffffffff & ~crc)


def arr_to_str(arr):
    str_bin = ""
    for x in arr:
        str_bin += x
    return str_bin


def str_to_bit(str_b):
    str_b = str(str_b)
    str_bit = []
    for x in str_b:
        str_bit.append(str(bin(int(x)).lstrip('0b')).zfill(8))
    return arr_to_str(str_bit)


def test():
    arr_str_bin = read()
    case_x = int(input("1. even \n2.modulo \n3. crc\n"))
    if case_x == 1:
        x = check_if_even(arr_str_bin)
        write("first.txt", x)
        y = sending_message(x)
        z = check_if_even(x)
        write("second.txt", z)
    elif case_x == 2:
        x = check_modulo(arr_str_bin)
        write("first.txt", x)
        y = sending_message(x)
        z = check_modulo(y)
        write("second.txt", z)
    else:
        crc_x = crc(0, arr_str_bin)
        print(crc_x)
        x = str(arr_str_bin) + crc_x
        write("first.txt", x)
        y = sending_message(x)
        crc_z = crc(0, y)
        print(crc_z)
        z = str(arr_str_bin) + crc_z
        write("second.txt", z)


test()
