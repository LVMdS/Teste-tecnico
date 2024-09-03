def count_letter_a(s):
    # Converte a string para minúsculas para facilitar a contagem
    s_lower = s.lower()
    
    # Conta o número de vezes que 'a' aparece na string
    count = s_lower.count('a')
    
    # Verifica se a letra 'a' está presente
    if count > 0:
        print(f"A letra 'a' aparece {count} vezes na string.")
    else:
        print("A letra 'a' não está presente na string.")

def main():
    # Solicita a string ao usuário
    user_string = input("Informe uma string para verificar a presença da letra 'a': ")
    
    # Chama a função para verificar e contar a letra 'a'
    count_letter_a(user_string)

# Chama a função principal
if __name__ == "__main__":
    main()
  
