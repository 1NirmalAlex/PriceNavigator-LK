import streamlit as st
import pandas as pd
import plotly.express as px
import re

# --- 1. Page Configuration ---
st.set_page_config(page_title="Ikman PriceSpy Dashboard", page_icon="📱", layout="wide")

# --- 2. Load and Clean Data ---
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('phone_market_data.csv')
        def extract_capacity(name):
            match = re.search(r'(\d+)\s*(GB|TB|gb|tb)', str(name))
            return match.group(0).upper() if match else "Standard"
        df['Capacity'] = df['Name'].apply(extract_capacity)
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    except FileNotFoundError:
        st.error("❌ Data file not found!")
        return pd.DataFrame()

df = load_data()

# --- 3. Dashboard Header ---
st.title("📱 Smart Mobile Market Analyzer")
st.markdown("Professional Dashboard for tracking used mobile prices and finding the best deals.")
st.divider()

if not df.empty:
    # --- 4. Sidebar Controls ---
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/518/518286.png", width=80)
    st.sidebar.title("Dashboard Controls")
    
    st.sidebar.markdown("### 💰 Budget Settings")
    user_budget = st.sidebar.number_input("Maximum Budget (Rs.):", min_value=10000, max_value=1000000, value=150000, step=5000)
    top_n = st.sidebar.slider("Number of Phones to Show:", min_value=5, max_value=150, value=15, step=5)
    
    # 🔥 ALUTH FIX EKA: User ta sort karana widiha thoranna denna
    sort_preference = st.sidebar.radio(
        "How do you want to find phones?",
        ["Closest to Budget (Best Specs)", "Cheapest First"]
    )
    
    st.sidebar.divider()
    st.sidebar.markdown("### 📈 Trend Settings")
    search_phone = st.sidebar.text_input("Search Phone Model:", "Realme C11")

    # --- 5. Main UI Layout ---
    tab1, tab2, tab3 = st.tabs(["💰 Budget Analyzer", "📈 Price Trend Tracker", "📋 Raw Market Data"])

    # ----- TAB 1: Budget Analyzer -----
    with tab1:
        st.subheader(f"Best Deals Under Rs. {user_budget:,}")
        
        # Filter entire dataset based on budget first
        budget_friendly = df[df['Price'] <= user_budget].copy()
        
        if not budget_friendly.empty:
            st.metric(label="Total Matching Models Found in Market", value=len(budget_friendly['Name'].unique()))
            
            # Grouping
            avg_prices = budget_friendly.groupby(['Name', 'Capacity'])['Price'].mean().reset_index()
            
            # 🔥 GLOBAL SORTING FIX: 
            # User "Closest to Budget" thoruwoth ascending=False wenawa (150k idan pallahata).
            # "Cheapest First" thoruwoth ascending=True wenawa (0 idan ihalaata).
            is_ascending = True if sort_preference == "Cheapest First" else False
            avg_prices = avg_prices.sort_values(by='Price', ascending=is_ascending).head(top_n)

            # Dynamic height for large lists
            calculated_height = max(400, (len(avg_prices) * 30) + 100)

            fig1 = px.bar(
                avg_prices, x='Price', y='Name', color='Capacity', orientation='h',
                labels={'Price': 'Average Price (Rs.)', 'Name': ''},
                color_discrete_sequence=px.colors.qualitative.Pastel,
                height=calculated_height
            )
            # Fix Y-axis order to look clean visually based on selection
            if not is_ascending:
                fig1.update_layout(template="plotly_dark", yaxis={'categoryorder': 'total ascending'})
            else:
                fig1.update_layout(template="plotly_dark", yaxis={'categoryorder': 'total descending'})
                
            st.plotly_chart(fig1, use_container_width=True)
        else:
            st.warning("No phones found under this budget.")

    # ----- TAB 2: Price Trend -----
    with tab2:
        st.subheader(f"Price Trend for '{search_phone.upper()}'")
        phone_data = df[df['Name'].str.contains(search_phone, case=False, na=False)]
        
        if not phone_data.empty:
            m1, m2 = st.columns(2)
            m1.metric("Highest Price", f"Rs. {phone_data['Price'].max():,}")
            m2.metric("Lowest Price", f"Rs. {phone_data['Price'].min():,}")

            trend_data = phone_data.groupby(['Date', 'Capacity'])['Price'].mean().reset_index()
            fig2 = px.line(trend_data, x='Date', y='Price', color='Capacity', markers=True)
            fig2.update_layout(template="plotly_dark", hovermode="x unified")
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("Enter a valid phone model to see trends.")

    # ----- TAB 3: Raw Data -----
    with tab3:
        st.subheader("Complete Market Dataset")
        st.dataframe(df, use_container_width=True, height=500)

    st.divider()
    st.caption("Developed by Umesh Alexander | Professional Python Web Scraping & Data Analysis")