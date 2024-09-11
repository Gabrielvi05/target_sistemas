"Inverte os caracteres de uma String"

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

string = input("Digite a string que deseja inverter: ")
print("String invertida:", reverse_string(string))

