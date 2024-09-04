# Função para inverter uma string
def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

# Entrada do usuário
entrada = input("Digite a string a ser invertida: ")

# Inverter a string e exibir o resultado
print(f"String invertida: {inverter_string(entrada)}")
