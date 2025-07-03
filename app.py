import streamlit as st
import os
from dotenv import load_dotenv

from utils.weather_service import WeatherService
from utils.dishes import get_local_dishes
from utils.julep_ai import generate_foodie_story
from utils.utils import (
    load_css, get_weather_emoji, get_weather_image_url,
    validate_api_key, show_progress_with_message, clear_progress,
    create_download_content
)

# Load environment variables
load_dotenv()
weather_key = os.getenv("OPENWEATHER_API_KEY")

# Set up Streamlit page
st.set_page_config(
    page_title="🍽️ Weather-Aware Culinary Journeys",
    page_icon="🍽️",
    layout="wide"
)

# Load optional custom styles
if os.path.exists("styles.css"):
    load_css("styles.css")

# Initialize session state
if "tours" not in st.session_state:
    st.session_state["tours"] = {}

# Sidebar UI
st.sidebar.title("🌆 Select Your Cities")
cities = st.sidebar.multiselect(
    "Choose Cities for Food Tour",
    ["Patna", "Ranchi", "Raipur"],
    default=["Patna"]
)

# Validate API key
valid, validation_msg = validate_api_key(weather_key, "OpenWeather")
if not valid:
    st.error(validation_msg)
    st.stop()

# Initialize Weather Service
weather_service = WeatherService(weather_key)

# Page Header
st.title("🍽️ Regional Foodie Tour with AI & Weather")
st.markdown("Plan the perfect culinary day based on the live weather! 🌤️")

# Action Button
if st.button("🚀 Generate Foodie Tours"):
    st.session_state["tours"].clear()

    for city in cities:
        st.markdown(f"## 📍 {city}")
        bar, msg = show_progress_with_message(0, f"Fetching weather for {city}...")

        # Get weather
        weather = weather_service.get_weather_data(city)
        if not weather:
            st.error(f"❌ Couldn't fetch weather for {city}")
            continue

        emoji = get_weather_emoji(weather["description"])
        image_url = get_weather_image_url(weather["description"])

        st.markdown(f"### {emoji} Weather: {weather['description'].capitalize()} | {weather['temperature']}°C")
        st.image(image_url, width=100)

        recommendation = weather_service.get_dining_recommendation(weather)
        st.markdown(f"**Suggested Dining:** {recommendation}")

        # Get dishes and story
        dishes = get_local_dishes(city)
        story = generate_foodie_story(city, dishes, weather)

        st.markdown("### 🍴 One-Day Foodie Tour")
        st.markdown(story)

        # Prepare dish names for display
        dish_names = ", ".join(d["dish"] for d in dishes)

        # Save tour info to session state
        st.session_state["tours"][city] = {
            "city": city,
            "weather": weather,
            "🌦️ Weather Analysis": f"{weather['description'].capitalize()}, {weather['temperature']}°C",
            "🍽️ Iconic Dishes": dish_names,
            "🏨 Top Restaurants": "🔍 Top-rated restaurant suggestions for this city.",
            "🗺️ Tour Plan": story,
            "📘 Final Guide": story
        }

        # Download Button
        st.download_button(
            "📥 Download Tour",
            create_download_content(st.session_state["tours"][city]),
            file_name=f"{city}_foodie_tour.md"
        )

        clear_progress(bar, msg)
