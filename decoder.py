import base64

def base64_decode(data):
    try:
        decoded_bytes = base64.b64decode(data)
        return decoded_bytes.decode('utf-8')
    except:
        return "No se pudo decodificar como base64"

def base32_decode(data):
    try:
        decoded_bytes = base64.b32decode(data)
        return decoded_bytes.decode('utf-8')
    except:
        return "No se pudo decodificar como base32"

def ascii_decode(data):
    try:
        decoded_str = ""
        parts = data.split()
        for part in parts:
            decoded_str += chr(int(part))
        return decoded_str
    except:
        return "No se pudo decodificar como ASCII"

def hex_decode(data):
    try:
        decoded_bytes = bytes.fromhex(data)
        return decoded_bytes.decode('utf-8')
    except:
        return "No se pudo decodificar como hexadecimal"

def octal_decode(data):
    try:
        decoded_str = ""
        parts = data.split()
        for part in parts:
            decoded_str += chr(int(part, 8))
        return decoded_str
    except:
        return "No se pudo decodificar como octal"

def binary_decode(data):
    try:
        decoded_str = ""
        parts = data.split()
        for part in parts:
            decoded_str += chr(int(part, 2))
        return decoded_str
    except:
        return "No se pudo decodificar como binario"

def main():
    data = input("Por favor, pegue el texto a decodificar: ")

    print("Seleccione el tipo de decodificación:")
    print("1. Base64")
    print("2. Base32")
    print("3. ASCII")
    print("4. Hexadecimal")
    print("5. Octal")
    print("6. Binario")

    choice = input("Ingrese el número de la opción deseada: ")

    decoded_text = ""
    if choice == "1":
        decoded_text = base64_decode(data)
    elif choice == "2":
        decoded_text = base32_decode(data)
    elif choice == "3":
        decoded_text = ascii_decode(data)
    elif choice == "4":
        decoded_text = hex_decode(data)
    elif choice == "5":
        decoded_text = octal_decode(data)
    elif choice == "6":
        decoded_text = binary_decode(data)
    else:
        print("Opción no válida")

    print("Texto decodificado:")
    print(decoded_text)

if __name__ == "__main__":
    main()

