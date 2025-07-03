import streamlit as st

def load_css(file_path):
    """
    Load and apply custom CSS from a file.
    """
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_weather_emoji(description):
    """
    Return a weather-related emoji based on description.
    """
    desc = description.lower()
    if "cloud" in desc:
        return "☁️"
    elif "rain" in desc or "storm" in desc:
        return "🌧️"
    elif "clear" in desc:
        return "☀️"
    elif "snow" in desc:
        return "❄️"
    else:
        return "🌤️"

def get_weather_image_url(description):
    """
    Return a relevant weather icon URL for visual UI.
    """
    desc = description.lower()
    if "cloud" in desc:
        return "https://cdn-icons-png.flaticon.com/512/1163/1163624.png"
    elif "rain" in desc or "storm" in desc:
        return "https://cdn-icons-png.flaticon.com/512/1163/1163657.png"
    elif "clear" in desc:
        return "https://cdn-icons-png.flaticon.com/512/869/869869.png"
    elif "snow" in desc:
        return "https://cdn-icons-png.flaticon.com/512/642/642102.png"
    else:
        return "https://cdn-icons-png.flaticon.com/512/1163/1163624.png"

def validate_api_key(key, name):
    """
    Check if an API key is present and valid.
    """
    if not key or key.startswith("your_"):
        return False, f"❌ {name} API key is missing or invalid in `.env` file."
    return True, "✅ Valid"

def show_progress_with_message(progress, message):
    """
    Show Streamlit progress bar with a status message.
    """
    return st.progress(progress), st.empty()

def clear_progress(bar, msg):
    """
    Clear both progress bar and message placeholder.
    """
    bar.empty()
    msg.empty()

def create_download_content(tour):
    """
    Generate markdown content from a tour dictionary for download.
    """
    text = f"# Foodie Tour for {tour['city']}\n\n"
    for section in [
        "🌦️ Weather Analysis",
        "🍽️ Iconic Dishes",
        "🏨 Top Restaurants",
        "🗺️ Tour Plan",
        "📘 Final Guide"
    ]:
        if section in tour:
            text += f"## {section}\n{tour[section]}\n\n"
    return text

def clean_response_text(text):
    """
    Clean response text by removing excessive line breaks or whitespace.
    """
    return text.strip().replace('\n\n', '\n')
