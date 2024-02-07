import random


# Configuración del juego
INTENTOS_MAXIMOS = 5
CARACTER_INCOGNITO = ("➖")
letras_intentadas = set()
intentos_realizados = 0


def elegir_palabra_a_adivinar():
    """
    Determina que palabra vamos a adivinar en el juego.

    Devuelve un string con la palabra a adivinar.
    :return: str
    """
    lista_palabras = [
        "codigo",
        "juego",
        "python",
        "otorrinolaringologo"
    ]

    return (random.choice(lista_palabras))


def mostrar_estado_del_juego(palabra):
    """
    Muestra en la pantalla el progreso actual del juego.
    Las letras que fueron adivinadas se muestran.
    Las letras que no fueron adivinadas aún permanecen ocultas.
    :param palabra: string
    :return: None
    """
    for letra in palabra:
        if letra in letras_intentadas:
            print(f"{letra}", end="")
        else:
            print(CARACTER_INCOGNITO, end="")
    print("")


def mostrar_vidas():
    """
    Muestra la cantidad de vidas que le quedan en el juego.
    :return: None
    """
    cantidad_vidas = INTENTOS_MAXIMOS - intentos_realizados
    if cantidad_vidas == 0:
        print("No te quedan vidas 💔\n")
    elif cantidad_vidas == 1:
        print("Te queda una vida ❤️\n")
    else:
        print(f"Te quedan {cantidad_vidas} vidas: {"❤️"*cantidad_vidas}\n")


def validar_intento(intento):
    """
    Determina si el intento ingresado es válido.

    Devuelve:
        True si el intento es válido
        False si el intento NO es válido
    :param intento: string
    :return: bool
    """
    return intento.isalpha() and len(intento) == 1


def realizar_intento(palabra_secreta):
    """
    Permite que el usuario pueda realizar un intento usando el teclado.
    :param palabra_secreta: string La palabra a adivinar
    :return: None
    """
    global intentos_realizados

    intento = input("➡️Ingresa una letra: ").lower()

    if validar_intento(intento):
        if intento in letras_intentadas:
            print("🔄Ya has usado esa letra. Intenta con otra.\n")
        elif intento in palabra_secreta:
            letras_intentadas.add(intento)
            print("✅¡Correcto! Has adivinado una letra.\n")
        else:
            letras_intentadas.add(intento)
            intentos_realizados += 1
            print(f"❌Incorrecto. La letra '{intento}' no está en la palabra.")
            mostrar_vidas()
    else:
        print("⚠️Por favor, ingresa una letra válida.\n")


def determinar_si_gano_el_juego(palabra_secreta):
    # Si el conjunto con las letras adivinadas esta
    # contenido en el conjunto de las letras de palabra secreta,
    # entonces gano
    return set(palabra_secreta).issubset(letras_intentadas)


def determinar_si_perdio_el_juego():
    """
    Determina si el usuario perdió el juego.
    :return: bool True si perdió el juego. False si ganó el juego.
    """
    return intentos_realizados == INTENTOS_MAXIMOS


def jugar_ahorcado():
    """
    Maneja la lógica principal del juego del ahorcado.
    :return: None
    """
    palabra_secreta = elegir_palabra_a_adivinar()

    print("▶¡Bienvenid@ al juego del Ahorcado!")

    while True:
        mostrar_estado_del_juego(palabra_secreta)

        realizar_intento(palabra_secreta)

        if determinar_si_gano_el_juego(palabra_secreta):
            print("🎉¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            break
        elif determinar_si_perdio_el_juego():
            print("😵¡Oh no! Has agotado todos tus intentos.")
            print(f"🤫La palabra era: {palabra_secreta}")
            break


if __name__ == "__main__":
    jugar_ahorcado()
