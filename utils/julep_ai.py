# utils/julep_ai.py

def generate_foodie_story(city, dishes_with_restaurants, weather):
    description = weather.get('description', 'clear')
    temp = float(weather.get('temperature', 25))

    # Determine dining recommendation based on weather
    if "rain" in description.lower() or temp < 20:
        dining_type = "Indoor Dining Recommended – Stay cozy and dry today."
    elif temp > 30:
        dining_type = "Indoor Dining Recommended – Beat the heat indoors."
    else:
        dining_type = "Outdoor Dining Recommended – Enjoy the beautiful weather outside."

    # Generate the final story with proper formatting
    return f"""
Welcome to {city}! 🌆

The weather today is **{description}** with a temperature of **{temp}°C** — 🍽️ {dining_type}

🥐 **Breakfast**: Start your day with **{dishes_with_restaurants[0]['dish']}** at _{dishes_with_restaurants[0]['restaurant']}_, a local favorite.

🍛 **Lunch**: Head over to _{dishes_with_restaurants[1]['restaurant']}_ and try the iconic **{dishes_with_restaurants[1]['dish']}**, perfect for {description.lower()} days.

🍲 **Dinner**: Wrap up your culinary journey at _{dishes_with_restaurants[2]['restaurant']}_ with a comforting plate of **{dishes_with_restaurants[2]['dish']}**.

Enjoy your one-day foodie tour with climate-conscious dining decisions. Bon appétit! 😋
"""
