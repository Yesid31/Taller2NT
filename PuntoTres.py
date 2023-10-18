import random

departamentos = {
    "Amazonas": "Leticia", "Antioquia": "Medellin", "Arauca": "Arauca", "Atlantico": "Barranquilla",
    "Bogota": "Bogota", "Bolivar": "Cartagena", "Boyaca": "Tunja", "Caldas": "Manizales"
}

def juego_departamentos():
    # Escoge un departamento al azar (random)
    departamento = random.choice(list(departamentos.keys()))
    capital = departamentos[departamento]
    
    print(f'Cual es la capital del Departamento de {departamento}?')

    contador = 0
    while contador < 3:
        contador += 1
        respuesta = input('Respuesta: ')
        if respuesta.lower() == 'salir':
            print('Gracias por participar, hasta pronto!')
            break
        if respuesta == capital:
            print('¡Felicitaciones, es correcto!')
            break
        else:
            print('Estás equivocado, inténtalo nuevamente')
        if contador == 3:
            print('¡HASTA LUEGO! ... Intentos máximos superados (3)')

# Ejecutar la función lambda
juego_departamentos()
