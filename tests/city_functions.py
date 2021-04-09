def country_city(country, city, population=''):
    "returns formatted city country"
    if population:
        city_country = (f"{city}, {country} - population {population}")
    else:
        city_country = (f"{city}, {country}")
    return city_country.title()


# print (country_city('russia', 'kirov', 500000))