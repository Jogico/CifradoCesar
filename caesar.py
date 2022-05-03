import sys

def main():
    message = input("Introducir Mensaje a Cifrar: ")
    if message == "":
        print("No puede ir Vacio ¡¡INTENTA MAS TARDE BUEN DIA Good Luck !!")
        sys.exit(0)
    
    key = int(input("key [0-26]: "))
    while key < 0 or key > 26:
        print("El numero debe estar entre 0 y 26")
        key = int(input("key [0-26]: "))
               
    mode = input("Cifrar o Decifrar [c/d]: ") 
    
    if mode.lower().startswith('c'):
        mode = "cifrar"
    elif mode.lower().startswith('d'):
        mode = "descifrar"
        
    transformar = encdec(message, key, mode)
    if mode == "cifrar":
        print()
        print("MENSAJE CIFRADO: ", transformar)
    elif mode == "descifrar":
        print(("mensaje Descifrar:", transformar))
        
def encdec(message, key, mode):
    # message = message.upper()
    transformar = ""
    LETTERS = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for symbol in message:
        if symbol in LETTERS:
          num = LETTERS.find(symbol)
          if mode == "cifrar":
            num = num + key
          elif mode == "descifrar":
            num = num - key
            
          if num >= len(LETTERS):
            num -= len(LETTERS)
          elif num <= 0:
            num += len(LETTERS)
            
          transformar += LETTERS[num]
        else:
            transformar += symbol
    return transformar

   
    

if __name__ == '__main__':
    main()
    print()
    print("GRACIAS POR USAR EL PROGRAMA DE CIFRADO")
    print()
    input("Presionar Enter para TERMINAR")
    sys.exit(0)
    