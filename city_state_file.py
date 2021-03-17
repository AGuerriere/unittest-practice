def city_state(city, country, population=''):
    if population:
        return (city.title() + ', ' + country.title() + ' population: '+ population)
    else:
        return (city + ', ' + country).title()
