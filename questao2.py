def fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    if n in fib:
        print(f"{n} pertence a sequencia de Fibonacci.")
    else:
        print(f"{n} não pertence a sequencia de Fibonacci.")

# Testando com o número 21
entrada = input(f'Digite um numero: ')      
fibonacci(int(entrada))
