def get_local_dishes(city):
    dishes_data = {
        "Patna": [
            {"dish": "Litti Chokha", "restaurant": "Bansi Vihar"},
            {"dish": "Khaja", "restaurant": "Bihar Sweets Corner"},
            {"dish": "Dal Pitha", "restaurant": "Pind Balluchi"}
        ],
        "Ranchi": [
            {"dish": "Handi Mutton", "restaurant": "Angithi"},
            {"dish": "Thekua", "restaurant": "Sweet House"},
            {"dish": "Chana Samosa", "restaurant": "Kaveri Restaurant"}
        ],
        "Raipur": [
            {"dish": "Chana Samosa", "restaurant": "GT Star Cafe"},
            {"dish": "Sabudana Khichdi", "restaurant": "Shyam Bhojnalaya"},
            {"dish": "Bafauri", "restaurant": "Mocha Raipur"}
        ]
    }

    return dishes_data.get(city, [])
