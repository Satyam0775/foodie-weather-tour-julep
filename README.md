# 🍽️ Smart Food Tours with Live Weather

An AI-powered web application that generates personalized food itineraries based on **real-time weather data** and cultural insights.  
Using **Julep AI agents**, **OpenWeatherMap**, and **Google Places**, this project crafts climate-conscious dining experiences across Indian cities.

---

## 🌟 Features

- 📡 **Real-Time Weather Integration** — Get live conditions from OpenWeatherMap API
- 🤖 **Julep AI Agents** — 5 specialized AI agents personalize your tour
- 🍴 **Weather-Adaptive Dining** — Recommends indoor/outdoor options based on forecast
- 🏙️ **Multi-City Support** — Generate food guides for multiple cities in one go
- 📱 **Streamlit UI** — Clean, responsive interface with stylish layout
- 📥 **Markdown Downloads** — Export your tour as a `.md` file
- 🏨 **Google Places API** — Finds real restaurants for your chosen dishes

---

## 🧠 Powered By

- 🔗 **Julep AI** — Multi-agent conversational framework
- ☁️ **OpenWeatherMap** — Real-time weather data
- 🏨 **Google Places API** — Live restaurant search
- 🎨 **Streamlit** — Interactive web app interface
- 🛠️ **Python 3.9+**

---

## 🏗️ Project Structure

multi-agent-food-tour/
├── app.py # Main Streamlit app
├── .env # API keys (OpenWeather, Google, Julep)
├── requirements.txt # Python dependencies
├── styles.css # Custom styling
├── README.md # This file
├── templates/
│ └── components.html # HTML templates (optional)
└── utils/
├── init.py
├── agent_services.py # Julep AI integration
├── dishes.py # Static dishes data
├── julep_ai.py # Narrative generation
├── restaurant_search.py # Google Places API search
├── weather_service.py # Weather API calls
└── utils.py # Helper functions


## 🚀 Example Workflow

1. Select your cities (e.g., Patna, Ranchi).
2. Fetch today's real-time weather data.
3. Suggest indoor or outdoor dining based on temperature & weather.
4. Pick 3 iconic dishes from the selected city.
5. Search Google Places API for **real top-rated restaurants** that serve those dishes.
6. Create a one-day foodie itinerary:
   - 🥐 **Breakfast**: dish + restaurant + weather reason
   - 🍛 **Lunch**: dish + restaurant + weather reason
   - 🍲 **Dinner**: dish + restaurant + weather reason
7. Display beautifully on Streamlit.
8. Download the tour as a Markdown file.

---

## ✅ Example Output

📍 Ranchi
☁️ Weather: Overcast clouds | 28.28°C
Suggested Dining: 🌤️ Outdoor Dining Recommended

🍴 One-Day Foodie Tour
Welcome to Ranchi! 🌆
The weather today is overcast clouds with a temperature of 28.28°C — 🍽️ Outdoor Dining Recommended – Enjoy the beautiful weather outside.

🥐 Breakfast: Start your day with Handi Mutton at Angithi, a local favorite.
🍛 Lunch: Head over to Sweet House and try the iconic Thekua, perfect for overcast clouds days.
🍲 Dinner: Wrap up your culinary journey at Kaveri Restaurant with a comforting plate of Chana Samosa.

Enjoy your one-day foodie tour with climate-conscious dining decisions. Bon appétit! 😋


## ℹ️ Notes

- If Google Places API doesn't find a matching restaurant, a fallback message is shown.
- API keys are stored securely in the `.env` file.
- Fully open-source and easy to customize for new cities or cuisines.

---

## 🔑 API Setup

Create a `.env` file like this:

```env
# Julep AI API Key
JULEP_API_KEY=your_julep_api_key

# OpenWeatherMap API Key
OPENWEATHER_API_KEY=your_openweather_api_key

# Google Places API Key
GOOGLE_PLACES_API_KEY=your_google_places_api_key
🤝 Contributing
Fork the repository

Create a new branch: git checkout -b feature/your-feature

Commit your changes: git commit -m 'Add some feature'

Push to the branch: git push origin feature/your-feature

Open a Pull Request

📥 Installation

git clone https://github.com/your-username/Food-Tour-Julep-master.git
cd Food-Tour-Julep-master
pip install -r requirements.txt
streamlit run app.py

✨ License
MIT License — Free to use and modify.
