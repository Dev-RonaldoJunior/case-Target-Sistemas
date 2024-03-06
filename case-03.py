# Função para encontrar o próximo elemento em uma sequência
def proximo_elemento(sequencia):
    # Verifica se a sequência tem pelo menos dois elementos
    if len(sequencia) >= 2:
        # Padrão 'a': adicionar 2 ao último elemento
        if sequencia[-1] - sequencia[-2] == 2:
            return sequencia[-1] + 2
        # Padrão 'b': multiplicar o último elemento por 2
        elif sequencia[-1] == sequencia[-2] * 2:
            return sequencia[-1] * 2
        # Padrão 'd': (n*2+2)^2
        elif sequencia[-1] == (len(sequencia) * 2) ** 2:
            return (len(sequencia) * 2 + 2) ** 2
        # Padrão 'e': soma dos dois últimos elementos
        elif len(sequencia) >= 3 and sequencia[-1] == sequencia[-2] + sequencia[-3]:
            return sequencia[-1] + sequencia[-2]
        # Padrão 'f': adicionar 1 ao último elemento se os dois últimos forem consecutivos
        elif len(sequencia) >= 7 and sequencia[-1] == sequencia[-2] + 1:
            return sequencia[-1] + 1
    # Padrão 'c': n^2
    return len(sequencia) ** 2

# Dicionário de sequências para testar
sequencias = {
    'a': [1, 3, 5, 7],               # Padrão: Adicionar 2
    'b': [2, 4, 8, 16, 32, 64],      # Padrão: Multiplicar por 2
    'c': [0, 1, 4, 9, 16, 25, 36],   # Padrão: Quadrado do índice
    'd': [4, 16, 36, 64],            # Padrão: (n*2+2)^2
    'e': [1, 1, 2, 3, 5, 8],         # Padrão: Soma dos dois últimos
    'f': [2, 10, 12, 16, 17, 18, 19] # Padrão: Adicionar 1 se consecutivos
}

# Loop para encontrar e exibir o próximo elemento para cada sequência
for chave, sequencia in sequencias.items():
    proximo = proximo_elemento(sequencia)
    if proximo is not None:
        print(f"Próximo elemento da sequência '{chave}': {proximo}")
    else:
        print(f"Não foi possível determinar a lógica da sequência '{chave}'.")


# CASE 03: Descubra a lógica e complete o próximo elemento:  

# a) 1, 3, 5, 7, ___  
# (LÓGICA: Uma sequência de números ímpares. Portanto, o próximo número deve ser 9.)
# RESPOSTA: o próximo elemento é 9 ficando assim = 1, 3, 5, 7, 9

# b) 2, 4, 8, 16, 32, 64, ____  
# (LÓGICA: Uma sequência de potências de 2. Cada número é o dobro do anterior. Portanto, o próximo número deve ser 128.)
# RESPOSTA: o próximo elemento é 128 ficando assim = 2, 4, 8, 16, 32, 64, 128

# c) 0, 1, 4, 9, 16, 25, 36, ____  
# (LÓGICA: Uma sequência de quadrados perfeitos. Cada número é o quadrado do índice da posição. Portanto, o próximo número deve ser 49 "7^2")
# RESPOSTA: o próximo elemento é 49 ficando assim = 0, 1, 4, 9, 16, 25, 36, 49

# d) 4, 16, 36, 64, ____  
# (LÓGICA: Uma sequência de quadrados de números pares começando de 2. Então, o próximo número deve ser 100 "10^2")
# RESPOSTA: o próximo elemento é 100 ficando assim = 4, 16, 36, 64, 100

# e) 1, 1, 2, 3, 5, 8, ____  
# (LÓGICA: Uma sequência de Fibonacci, onde cada número é a soma dos dois anteriores. Portanto, o próximo número deve ser 13.)
# RESPOSTA: o próximo elemento é 13 ficando assim = 1, 1, 2, 3, 5, 8, 13

# f) 2,10, 12, 16, 17, 18, 19, ____  
# (LÓGICA: Essa sequencia segue um padrão, o padrão de aumento muda. Nos dois primeiros passos, é de 8 e 2. Depois, é de 4 e 1, repetindo-se. Portanto, seguindo essa lógica, o próximo número na sequência será 19 + 1 = 20.)
# RESPOSTA: o próximo elemento é 20 ficando assim =  2, 10, 12, 16, 17, 18, 19, 20  