#!/usr/bin/env python3


def print_fibonacci(length):
    if length <= 0:
        print("[]")
    elif length == 1:
        print("[0]")
    else:
        fib_seq = [0, 1]
        for i in range(2, length):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        print(fib_seq)
