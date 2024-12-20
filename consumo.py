import requests

BASE_URL = "https://swapi.py4e.com/api/"

def get_arid_planets_movies():
    response = requests.get(f"{BASE_URL}planets/")
    response.raise_for_status()
    planets = response.json()
    
    movies_with_arid_planets = set()

    for planet in planets["results"]:
        if "arid" in planet["climate"]:
            for film_url in planet["films"]:
                movies_with_arid_planets.add(film_url)
    
    return len(movies_with_arid_planets)

def get_number_of_wookies():
    response = requests.get(f"{BASE_URL}species/")
    response.raise_for_status()
    species = response.json()
    
    wookie_species_url = None
    for specie in species["results"]:
        if specie["name"].lower() == "wookiee":
            wookie_species_url = specie["url"]
            break
    
    if not wookie_species_url:
        return 0
    
    response = requests.get(wookie_species_url)
    response.raise_for_status()
    wookie_data = response.json()
    
    return len(wookie_data["people"])

def get_smallest_vehicle_in_first_movie():
    response = requests.get(f"{BASE_URL}films/")
    response.raise_for_status()
    films = response.json()
    
    first_film = None
    for film in films["results"]:
        if film["episode_id"] == 4:
            first_film = film
            break
    
    if not first_film:
        return None
    
    smallest_vehicle = None
    smallest_vehicle_length = float("inf")
    
    for vehicle_url in first_film["vehicles"]:
        response = requests.get(vehicle_url)
        response.raise_for_status()
        vehicle = response.json()
        
        if vehicle["length"].replace(',', '').isdigit():
            vehicle_length = float(vehicle["length"].replace(',', ''))
            if vehicle_length < smallest_vehicle_length:
                smallest_vehicle = vehicle["name"]
                smallest_vehicle_length = vehicle_length
    
    return smallest_vehicle

print(f"Películas con planetas áridos: {get_arid_planets_movies()}")
print(f"Cantidad de Wookies en la saga: {get_number_of_wookies()}")
print(f"Aeronave más pequeña en la primera película: {get_smallest_vehicle_in_first_movie()}")
