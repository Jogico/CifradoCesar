import sys

def main():
    mensaje = input("Introducir Mensaje a Cifrar: ")
    if mensaje == "":
        print("No puede ir Vacio ¡¡INTENTA MAS TARDE BUEN DIA Good Luck !!")
        sys.exit(0)
    
    espaciocifrado = int(input("Espacios a Cifrar [0-26]: "))
    while espaciocifrado < 0 or espaciocifrado > 26:
        print("El numero debe estar entre 0 y 26")
        espaciocifrado = int(input("espacio Cifrado [0-26]: "))
               
    cifdesc = input("Cifrar o Decifrar [c/d]: ") 
    
    if cifdesc.lower().startswith('c'):
        cifdesc = "cifrar"
    elif cifdesc.lower().startswith('d'):
        cifdesc = "descifrar"
        
    transformar = encdec(mensaje, espaciocifrado, cifdesc)
    if cifdesc == "cifrar":
        print()
        print("MENSAJE CIFRADO: ", transformar)
    elif cifdesc == "descifrar":
        print(("mensaje Descifrar:", transformar))
        
def encdec(mensaje, espaciocifrado, cifdesc):
    
    transformar = ""
    alfabeto = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for symbol in mensaje:
        if symbol in alfabeto:
          num = alfabeto.find(symbol)
          if cifdesc == "cifrar":
            num = num + espaciocifrado
          elif cifdesc == "descifrar":
            num = num - espaciocifrado
            
          if num >= len(alfabeto):
            num -= len(alfabeto)
          elif num <= 0:
            num += len(alfabeto)
            
          transformar += alfabeto[num]
        else:
            transformar += symbol
    return transformar

if __name__ == '__main__':
    main()
    print()
    print("GRACIAS POR USAR EL PROGRAMA DE CIFRADO ¡¡ HAVE A NICE DAY !!")
    print()
    input("Presionar Enter para TERMINAR")
    sys.exit(0)
    