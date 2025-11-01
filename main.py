import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Page configuration
st.set_page_config(page_title="Currency Comparison", layout="wide")

# ============= DATA PROCESSING & MATH =============
@st.cache_data
def load_currency_data(file_path):
    """Load currency data and return the most recent closing value"""
    # Read CSV - first column (Price) actually contains dates
    df = pd.read_csv(file_path, skiprows=3)  # Skip 3 rows to get to actual data
    df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date', ascending=False)
    most_recent = df.iloc[0]
    return {
        'close': float(most_recent['Close']),
        'date': most_recent['Date']
    }

# Load all currencies and get most recent values
currencies = {
    'BRL': load_currency_data('Price-Data/BRL_Brazilian-Real.csv'),
    'EUR': load_currency_data('Price-Data/EUR_European-Euro.csv'),
    'JPY': load_currency_data('Price-Data/JPY_Japanese-Yen.csv'),
    'ZAR': load_currency_data('Price-Data/ZAR_South-African-Rand.csv'),
}

# Calculate percentages: divide 1 USD by the currency rate
# This shows what percentage of a dollar the foreign currency is worth
# Lower rate = stronger USD (good for US travelers)
for code in currencies:
    rate = currencies[code]['close']
    currencies[code]['rate'] = rate
    # Calculate: 1 / rate = how much USD per 1 unit of foreign currency
    # Then multiply by 100 to get percentage
    currencies[code]['percentage'] = (1 / rate) * 100

# ============= DONUT CHART FUNCTION =============
def create_donut_chart(percentage, color='#90EE90'):
    """Create a donut chart showing percentage"""
    fig = go.Figure(data=[go.Pie(
        values=[percentage, 100-percentage],
        hole=0.7,
        marker=dict(colors=[color, '#E8E8E8']),
        textinfo='none',
        hoverinfo='skip',
        showlegend=False
    )])
    
    fig.update_layout(
        annotations=[dict(
            text=f'{percentage:.1f}%', 
            x=0.5, y=0.5, 
            font_size=40, 
            showarrow=False,
            font=dict(weight='bold')
        )],
        height=280,
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

# ============= UI LAYOUT =============

# Title
st.title("US Dollar compared to international currency")
st.subheader("How your dollar will transfer for your next vacation abroad")

# Top section
col_text, col_map = st.columns([1, 2])

with col_text:
    st.write("### This info will tell you best conversion rate to the US dollar")
    st.write("")
    st.write("**Green is good red is bad**")
    
    # ====== INSERT TEXT CONTENT HERE ======
    pass
    # ======================================

with col_map:
    # ====== INSERT WORLD MAP CODE HERE ======
    # Example: st.image('path/to/map.png')
    # Or use plotly/folium for interactive map
    pass
    # ========================================

st.write("")
st.markdown("---")

# ============= DONUT CHARTS (IMPLEMENTED) =============
st.write("### Currency Exchange Rates")

# Create 4 columns for donut charts
cols = st.columns(4)

# Display BRL
with cols[0]:
    # Lower percentage = weaker BRL = good for USD holders (green)
    color = '#90EE90' if currencies['BRL']['percentage'] < 25 else '#FFB6C6'
    fig = create_donut_chart(currencies['BRL']['percentage'], color)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(f"**BRL - Brazilian Real**")
    st.caption(f"1 USD = {currencies['BRL']['rate']:.2f} BRL")

# Display EUR - Special handling for values over 100%
with cols[1]:
    # EUR is over 100% (stronger than USD) - show overflow with darker red
    eur_pct = currencies['EUR']['percentage']
    
    if eur_pct > 100:
        # Show 100% in light red, overflow in darker red
        overflow = eur_pct - 100
        fig = go.Figure(data=[go.Pie(
            values=[100, overflow, max(0, 100 - overflow)],
            hole=0.7,
            marker=dict(colors=['#FFB6C6', '#CC0000', '#E8E8E8']),
            textinfo='none',
            hoverinfo='skip',
            showlegend=False,
            direction='clockwise',
            sort=False
        )])
    else:
        fig = go.Figure(data=[go.Pie(
            values=[eur_pct, 100 - eur_pct],
            hole=0.7,
            marker=dict(colors=['#FFB6C6', '#E8E8E8']),
            textinfo='none',
            hoverinfo='skip',
            showlegend=False
        )])
    
    fig.update_layout(
        annotations=[dict(
            text=f'{eur_pct:.1f}%', 
            x=0.5, y=0.5, 
            font_size=40, 
            showarrow=False,
            font=dict(weight='bold')
        )],
        height=280,
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(f"**EUR - European Euro**")
    st.caption(f"1 USD = {currencies['EUR']['rate']:.2f} EUR")

# Display JPY
with cols[2]:
    # Lower percentage = weaker JPY = good for USD holders (green)
    jpy_pct = currencies['JPY']['percentage']
    color = '#90EE90' if jpy_pct < 1 else '#FFB6C6'
    fig = create_donut_chart(jpy_pct, color)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(f"**JPY - Japanese Yen**")
    st.caption(f"1 USD = {currencies['JPY']['rate']:.2f} JPY")

# Display ZAR - Show as percentage with green color
with cols[3]:
    # Lower percentage = weaker ZAR = good for USD holders (green)
    zar_pct = currencies['ZAR']['percentage']
    color = '#90EE90' if zar_pct < 10 else '#FFB6C6'
    fig = create_donut_chart(zar_pct, color)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(f"**ZAR - South African Rand**")
    st.caption(f"1 USD = {currencies['ZAR']['rate']:.2f} ZAR")

st.markdown("---")

# ====== INSERT ADDITIONAL SECTIONS HERE ======
# Add any footer, details, or extra content
pass
# =============================================