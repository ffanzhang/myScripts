#!/usr/bin/env python3
import random
import sys
import re
from datetime import datetime
last_number = 0
generated_number = 0

class Host():
    _q_title = ""
    _q_generator = None

    def __init__(self, q, title):
        self._q_generator = q
        self._q_title = title

    def ask_question(self):
        sys.stdout.write(self._q_title + '\n')
        q, a = self._q_generator.gen_question()

        sys.stdout.write(q + '\n')
        guess = None 
        while not self._q_generator.equals(guess, a):
            guess = sys.stdin.readline()

        sys.stdout.write('\n')

class QuestionGenerator():
    _gen_func = None
    _equals = None

    def __init__(self, gen_func, equals):
        self._gen_func = gen_func
        self._equals = equals

    def gen_question(self):
        return self._gen_func()

    def equals(self, a, b):
        return self._equals(a, b)
    
def bin_equals(a, b):
    try:
        return int(a, 2) == int(b, 2)
    except:
        return False

def hex_equals(a, b):
    try:
        return int(a, 16) == int(b, 16)
    except:
        return False

def gen_hex_bin_question():
    num = random.randrange(1, 16)
    q = str(hex(num))[2:]
    a = str(bin(num))[2:]
    return q, a

def gen_bin_hex_question():
    num = random.randrange(1, 16)
    q = str(bin(num))[2:]
    a = str(hex(num))[2:]
    return q, a 

if __name__ == "__main__":
    random.seed(datetime.now())
    last_question = None
    new_question = None
    hex_bin_gen = QuestionGenerator(gen_hex_bin_question, bin_equals)
    bin_hex_gen = QuestionGenerator(gen_bin_hex_question, hex_equals)
    host1 = Host(hex_bin_gen, "hex to bin")
    host2 = Host(bin_hex_gen, "bin to hex")
    while True:
        coin = random.randrange(0, 2)
        if coin > 0:
            host1.ask_question()
        else:
            host2.ask_question()
