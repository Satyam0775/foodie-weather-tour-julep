import os
from utils.restaurant_search import search_restaurant
from dotenv import load_dotenv

# Load your .env file
load_dotenv()

# Example test
if __name__ == "__main__":
    city = "Patna"
    dish = "Litti Chokha"

    print(f"Searching restaurants in {city} for {dish}...")
    results = search_restaurant(city, dish)

    if not results:
        print("❌ No results found or API key is invalid.")
    else:
        for idx, r in enumerate(results, start=1):
            print(f"{idx}. {r['name']} (⭐ {r.get('rating', 'N/A')})")
