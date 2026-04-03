# 📱 PriceNavigator-LK: Smart Mobile Market Analyzer

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**PriceNavigator-LK** is a professional data-driven dashboard designed to track, analyze, and visualize the used mobile phone market in Sri Lanka. It helps users find the absolute best deals by processing large datasets and applying advanced sorting logic.

---

## ✨ Key Features

- 🔍 **Global Best-Deal Sorting:** Unlike basic filters, our algorithm scans the entire dataset to find the absolute cheapest prices for specific models.
- 💰 **Interactive Budget Analyzer:** Set your maximum budget and instantly see the top-rated models within that range.
- 📈 **Price Trend Tracking:** Visualize how prices for specific models (like iPhone, Samsung, Realme) fluctuate over time.
- 📊 **Dynamic Data Visualizations:** Beautiful, interactive charts powered by **Plotly** that adjust their height based on data volume.
- 📱 **Clean UI/UX:** A sleek, dark-themed dashboard built with **Streamlit** for a professional user experience.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Streamlit (Web UI)
- **Data Handling:** Pandas (Data Cleaning & Analysis)
- **Visualization:** Plotly (Interactive Charts)
- **Regex:** For intelligent capacity (GB/TB) extraction from raw text.

---

## 🚀 Installation & Local Setup

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/1NirmalAlex/PriceNavigator-LK.git](https://github.com/1NirmalAlex/PriceNavigator-LK.git)
   cd PriceNavigator-LK
   
2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Run the application:**

      # streamlit run app.py 


📁 Project Structure
├── app.py                   # Main Streamlit application
├── phone_market_data.csv    # Scraped market dataset
├── requirements.txt         # List of Python dependencies
└── README.md                # Project documentation


👨‍💻 Developed By
Umesh Alexander AI & Python Developer / Data Scientist

GitHub: @1NirmalAlex

LinkedIn: [www.linkedin.com/in/umesh-alexander-026ba2317]

Disclaimer: Data is sourced from public marketplaces for educational and analytical purposes.
   
