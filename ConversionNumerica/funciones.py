def binario_a_decimal(binario):
    """
    Convierte un número binario (str) a decimal (int).
    """
    return int(binario, 2)

def decimal_a_binario(decimal):
    """
    Convierte un número decimal (int) a binario (str).
    """
    return bin(decimal)[2:]

def verificar_positivo(numero):
    while numero <= 0:
        numero = int(input(f"Error. Vuelva a ingresar un numero positivo: "))
    return numero

def numero_de_rondas(rondas):
        while True:
            if rondas != int(rondas):
                print("ERROR. Ingrese un numero tipo entero positivo")
                rondas = int(input("No se permiten caracteres o simbolos, ingrese un numero: "))
            return rondas