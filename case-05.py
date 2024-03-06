def inverter_string(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

entrada = input("Digite uma string para inverter: ")
resultado = inverter_string(entrada)
print("String invertida:", resultado)


# CASE 05: Escreva um programa que inverta os caracteres de um string. 

# IMPORTANTE: 

# 	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 

# 	b) Evite usar funções prontas, como, por exemplo, reverse; 
