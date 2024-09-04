def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

entrada = input("Digite a string a ser invertida: ")

print(f"String invertida: {inverter_string(entrada)}")
