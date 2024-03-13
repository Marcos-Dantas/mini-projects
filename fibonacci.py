def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def check_if_in_fibonacci_sequence(number):
    fib_sequence = fibonacci_sequence(number)
    if number in fib_sequence:
        return True
    else:
        return False

number = int(input("Digite um número para checar se está dentro da sequência de Fibonacci: "))
if check_if_in_fibonacci_sequence(number):
    print(f"O número {number} pertence à sequência")
else:
    print(f"O número {number} não pertence à sequência")