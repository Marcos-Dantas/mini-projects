def convert_string(string):
    count = len(string) - 1
    string_formated = []

    while count >= 0:
        string_formated.append(string[count])
        count = count - 1
    
    return ''.join(string_formated)

string = str(input("Digite uma string: "))
if len(string) == 1:
    print(f'A string de trás pra frente eh: {string}')
else:
    print(f'A string de trás pra frente eh: {convert_string(string)}')