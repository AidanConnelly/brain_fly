from colorama import Fore
from colorama import Style


def inc(ins_tape, ins_ptr, mem_tape, mem_ptr, stack):
    mem_tape[mem_ptr.get()] += 1


def dec(ins_tape, ins_ptr, mem_tape, mem_ptr, stack):
    mem_tape[mem_ptr.get()] -= 1


def ptr_inc(ins_tape, ins_ptr, mem_tape, mem_ptr, stack):
    mem_ptr.set(mem_ptr.get()+1)


def ptr_dec(ins_tape, ins_ptr, mem_tape, mem_ptr, stack):
    mem_ptr.set(mem_ptr.get()-1)


def output_at_ptr(ins_tape, ins_ptr, mem_tape, mem_ptr, stack):
    print("\n")
    print(chr(mem_tape[mem_ptr.get()]))


def input_at_ptr(ins_tape, ins_ptr, mem_tape, mem_ptr, stack):
    mem_tape[mem_ptr.get()] = ord(input())


def general_loop(ins_tape, ins_ptr, mem_tape, mem_ptr, direction):
    depth = 1
    while depth > 0:
        ins_ptr.set(ins_ptr.get() + direction)
        at_ins = ins_tape[ins_ptr.get()]
        if at_ins == "]":
            depth -= direction*1
        if at_ins == "[":
            depth += direction*1


def open_loop(ins_tape, ins_ptr, mem_tape, mem_ptr, direction):
    if mem_tape[mem_ptr.get()]==0:
        general_loop(ins_tape, ins_ptr, mem_tape, mem_ptr, +1)


def close_loop(ins_tape, ins_ptr, mem_tape, mem_ptr, direction):
    if mem_tape[mem_ptr.get()]!=0:
        general_loop(ins_tape, ins_ptr, mem_tape, mem_ptr, -1)


class Ptr:
    def __init__(self, to_set):
        self.val = [to_set]

    val = []

    def get(self):
        return self.val[0]

    def set(self, to_set):
        self.val[0] = to_set


def one_it(ins_tape, ins_ptr, mem_tape, mem_ptr, stack):
    for item in mem_tape:
        # c = Fore.BLACK + (item % 10)
        # print(f"{c}")
        print (str(item).zfill(2), end=' ')
    print("\n")

    current_ins = ins_tape[ins_ptr.get()]
    char_to_ins = dict()
    char_to_ins["+"] = inc
    char_to_ins["-"] = dec
    char_to_ins[">"] = ptr_inc
    char_to_ins["<"] = ptr_dec
    char_to_ins["["] = open_loop
    char_to_ins["]"] = close_loop
    char_to_ins["."] = output_at_ptr
    char_to_ins[","] = input_at_ptr
    f = char_to_ins[current_ins]
    f(ins_tape, ins_ptr, mem_tape, mem_ptr, stack)


def run_bf(ins_tape):
    mem_tape = [0 for _ in range(64)]
    stack = []
    ins_ptr = Ptr(0)
    mem_ptr = Ptr(0)
    while True:
        one_it(ins_tape, ins_ptr, mem_tape, mem_ptr, stack)
        ins_ptr.set(ins_ptr.get()+1)


run_bf(list(",>,<[->+<]>>+[]"))
