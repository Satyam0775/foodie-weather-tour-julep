# utils/restaurant_search.py

import requests
import os

def find_top_restaurants(dish_name, city, max_results=1):
    # Load the API key inside the function for fresh environment access
    GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")

    if not GOOGLE_PLACES_API_KEY:
        raise ValueError("Missing Google Places API Key in .env file")

    query = f"{dish_name} restaurant in {city}"
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    params = {
        "query": query,
        "key": GOOGLE_PLACES_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "OK":
        return [f"No restaurant found for '{dish_name}' in {city}."]

    restaurants = []
    for result in data.get("results", [])[:max_results]:
        name = result.get("name")
        address = result.get("formatted_address", "Address not available")
        rating = result.get("rating", "N/A")
        restaurants.append(f"{name} ({address}, ⭐ {rating})")

    return restaurants
