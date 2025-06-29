def city_country(city, country):
    print(f'{city}, {country}')



while True:
    print('Digite "q" para sair.')
    
    city = input('Cidade: ').title().strip()
    if city == 'Q':
        break
    
    country = input('País: ').title().strip()
    if country == 'Q':
        break

    city_country(city, country)