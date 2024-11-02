def inverter_string(s):
    
    string_invertida = ""
    
   
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]  
        
    return string_invertida  


entrada = "Olá, este é um teste para meu primeiro emprego."
resultado = inverter_string(entrada)

print(f'String original: {entrada}')
print(f'String invertida: {resultado}')