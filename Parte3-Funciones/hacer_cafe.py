def hacer_cafe(granos_de_cafe, leche, agua):
    """
    Función que prepara un café.

    Parámetros:
    - granos_de_cafe (en gramos): float
    - leche (en mililitros): float
    - agua (en mililitros): float
    """
    print(f"⏳Moliendo {granos_de_cafe} gramos de granos de café...")
    print("⏳Calentando", leche, "ml de leche...")
    print("⏳Calentando", agua, "ml de agua...")
    print("⏳Preparando filtro...")
    print(f"⏳Agregando {granos_de_cafe} gramos de café molido al filtro...")
    print("⏳Vertiendo", agua, "ml de agua caliente sobre el café...")
    print("⏳Esperando a que el café se prepare...")
    print("⏳Vertiendo café en la taza...")
    print("⏳Añadiendo", leche, "ml de leche al café...")
    print("☕¡Café listo para disfrutar!")

# Invocamos a la función con valores específicos para los ingredientes
hacer_cafe(20, 50, 200)