from time import sleep;

cars_available = ['subaru', 'honda', 'nissan', 'mercedes']

desired_car = input('Qual tipo de carro você gostaria? ').lower()

print(f'Vou ver se consigo um {desired_car} para você.')
sleep(1)    
if desired_car in cars_available:
    print(f'Temos {desired_car.title()} para você.')
else:
    print(f'Infelizmente não temos um {desired_car.title()} para você.')
    print(f'mas temos os seguintes: ' + ', ' .join(x.title() for x in cars_available))