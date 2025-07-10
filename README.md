# 🌍 Cost of Living Scraper (with Selenium + Firefox)

This project performs automated web scraping on the Numbeo website to extract average cost-of-living data in any city worldwide, including rent prices, restaurants, internet, gym, transportation, and more.

The application is built in Python using Selenium with the Firefox browser (via GeckoDriver).

---

## 🚀 Features

- Automated cost of living search by city
- Real-time data extraction from Numbeo
- Headless mode compatible (runs without opening browser window)
- Prepared for future integration with database or API

---

## 🧱 Project Structure

cost_of_living_scraper/
├── scraper.py         # Main script using Selenium + Firefox  
├── requirements.txt   # Project dependencies  
└── README.md          # This documentation  

---

## 📦 Requirements

- Python 3.8+
- GeckoDriver installed (https://github.com/mozilla/geckodriver/releases)
- Firefox browser installed

---

## 🔧 Installation

1. Clone the repository:

   git clone https://github.com/yourusername/cost-of-living-scraper.git  
   cd cost-of-living-scraper

2. Create a virtual environment (optional but recommended):

   python -m venv venv  
   source venv/bin/activate   (Linux/macOS)  
   venv\Scripts\activate      (Windows)

3. Install the dependencies:

   pip install -r requirements.txt

4. Set the path to GeckoDriver:

   In the `scraper.py` file, update the `GECKODRIVER_PATH` variable with your actual path.

---

## 🖥️ How to Use

Run the script and enter the name of the city you want to check:

   python scraper.py

After a few seconds, it will display the average cost-of-living items for the city.

---

## ✅ Example Output

Cost of living in Madrid:  
Apartment (1 bedroom) in City Centre: € 1,100.00  
Meal, Inexpensive Restaurant: € 13.00  
Internet (60 Mbps or more): € 30.00  
...

---

## 🛠️ Future Ideas

- Save results to PostgreSQL database  
- Price forecast for future months  
- City-to-city comparison  
- REST API for integration with frontend or dashboard  

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements, suggestions, or fixes.

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## 👤 Author

Developed by **Kauan Barbosa Rezende**  
📧 kauanbrezende82@gmail.com  
🔗 https://www.linkedin.com/in/kauan-barbosa-5b8133268/  
🔗 https://github.com/kauan02
