def is_fibonacci_number(n):
    # Função para verificar se um número pertence à sequência de Fibonacci
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

def main():
    # Solicita o número ao usuário
    num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    
    # Verifica se o número pertence à sequência de Fibonacci
    if is_fibonacci_number(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} NÃO pertence à sequência de Fibonacci.")

# Chama a função principal
if __name__ == "__main__":
    main()
  
