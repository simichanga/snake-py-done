def foo(number: float) -> float:
    print("before")
    return number + 1
    print("after")

# 0 1 1 2 3 5 8 ...
def fib(nth_term: int) -> int:
    if nth_term == 0 or nth_term == 1:
        return nth_term
    return fib(nth_term - 1) + fib(nth_term - 2)

import sys
sys.setrecursionlimit(10**6)
sys.set_int_max_str_digits(0)
# memoisation
memory = [0, 1]
def fib_mem(nth_term: int) -> int:
    global memory
    if len(memory) <= nth_term:
        for i in range(nth_term - len(memory) + 1):
            memory += [None]
    if memory[nth_term] != None:
        return memory[nth_term]
    memory[nth_term] = fib_mem(nth_term - 1) + fib_mem(nth_term - 2)
    return memory[nth_term]
print(fib_mem(10**5))
