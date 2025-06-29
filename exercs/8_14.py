def make_car(manufacturer, model, **kargs):
    car = {'manufacturer': manufacturer, 'model': model}

    for key, value in kargs.items():
        car[key] = value

    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)