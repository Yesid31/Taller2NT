from datetime import datetime
import random
import math

# Definir cuántos cupos tiene el parqueadero para carros y motos
print('////BIENVENIDO AL SISTEMA DE PARQUEADERO TORO////')
print('----------------------------------------------------')
camp_cars = int(input('Ingresa la cantidad de parqueaderos para carros: '))
camp_motorcycles = int(input('Ingresa la cantidad de parqueaderos para motos: '))

# Definir los campos del parqueadero
name_camp_cars = [{'place': input('Ingresa el nombre del campo del parqueadero de carro:'), 'available': True} for _ in range(camp_cars)]
name_camp_moto = [{'place': input('Ingresa el nombre del campo del parqueadero de moto:'), 'available': True} for _ in range(camp_motorcycles)]

# Definir tarifa de cobro por tiempo
cost_frac_car = 2000
cost_frac_moto = 1000

# Diccionarios para mantener un registro rápido de vehículos
register_car = {}
register_motorcycle = {}

def register_entry(vehicle_type, name_camp, register, cost_frac):
    if len(name_camp) > 0:
        placa = input('POR FAVOR INGRESA LA PLACA DEL VEHÍCULO:')
        hour_inside = datetime.now().strftime('%Y-%m-%d %H:%M')
        place_random = random.choice(name_camp)
        register[placa] = {'place': place_random, 'hour_inside': hour_inside, 'Action': 'Entro'}
        name_camp.remove(place_random)
        print(f'El registro de vehículos es el siguiente: {register}')
    else:
        print(f'PARQUEADERO DE {vehicle_type}S LLENO')

def calculate_payment(vehicle_type, register, name_camp, cost_frac):
    placa_pay = input('POR FAVOR DIGITA LA PLACA A COBRAR:')
    if placa_pay in register and register[placa_pay]['Action'] == 'Entro':
        hour_inside = datetime.strptime(register[placa_pay]['hour_inside'], '%Y-%m-%d %H:%M')
        hour_now = datetime.now()
        total = math.ceil((hour_now - hour_inside).total_seconds() / 3600) * cost_frac
        print('Tu valor a pagar de parqueo es:', total)
        name_camp.append(register[placa_pay]['place'])
        register[placa_pay]['hour_out'] = hour_now.strftime('%Y-%m-%d %H:%M')
        register[placa_pay]['pay_all'] = total
        register[placa_pay]['Action'] = 'salio'
        print(f'Los vehículos {vehicle_type} registrados son los siguientes: {register}')
    else:
        print('LA PLACA CONSULTADA NO FUE ENCONTRADA')

while True:
    place_free_moto = [x['place'] for x in name_camp_moto if x['available']]
    place_free_car = [x['place'] for x in name_camp_cars if x['available']]

    print('Lugares disponibles:', place_free_car, place_free_moto)

    print('¿QUÉ OPCIÓN DESEAS REALIZAR?')
    options = input('1. Registrar nuevo vehiculo\n2. Registrar salida de vehiculo\nOpción: ')

    if options not in ['1', '2']:
        print('NO SE ADMITEN LETRAS, SOLO LAS OPCIONES 1 o 2')
    elif options == '1':
        type_vehicle = input('QUE TIPO DE VEHICULO DESEAS REGISTRAR?\n1. Moto\n2. Carro\nOpción: ')
        if type_vehicle not in ['1', '2']:
            print('NO SE ADMITEN LETRAS, SOLO LAS OPCIONES 1 o 2')
        elif type_vehicle == '1':
            register_entry('Moto', place_free_moto, register_motorcycle, cost_frac_moto)
        elif type_vehicle == '2':
            register_entry('Carro', place_free_car, register_car, cost_frac_car)
    elif options == '2':
        option_cash = input('POR FAVOR DIGITA EL TIPO DE VEHÍCULO A COBRAR\n1. Moto\n2. Carro\nOpción: ')
        if option_cash not in ['1', '2']:
            print('NO SE ADMITEN LETRAS, SOLO LAS OPCIONES 1 o 2')
        elif option_cash == '1':
            calculate_payment('motorizado', register_motorcycle, place_free_moto, cost_frac_moto)
        elif option_cash == '2':
            calculate_payment('carro', register_car, place_free_car, cost_frac_car)
