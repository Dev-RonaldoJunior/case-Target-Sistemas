def pertence_sequencia_fibonacci(numero):
    """
    Verifica se um número pertence à sequência de Fibonacci.
    
    Args:
        numero (int): O número a ser verificado.
        
    Returns:
        bool: True se o número pertencer à sequência de Fibonacci, False caso contrário.
    """
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

def verificar_fibonacci():
    """
    Função principal para verificar se um número pertence à sequência de Fibonacci.
    """
    numero = input("Informe um número para verificar se pertence à sequência de Fibonacci: ")
    
    # Verifica se a entrada é um número inteiro positivo
    if numero.isdigit():
        numero = int(numero)
        if numero >= 0:
            if pertence_sequencia_fibonacci(numero):
                print(f"O número {numero} pertence à sequência de Fibonacci.")
            else:
                print(f"O número {numero} não pertence à sequência de Fibonacci.")
        else:
            print("Por favor, insira um número inteiro positivo.")
    else:
        print("Por favor, insira um número inteiro positivo.")


verificar_fibonacci()


# CASE 02: Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 

# IMPORTANTE:  

# 
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código; 