import streamlit as st
import time

# Custom CSS for a soothing, modern UI with hover effects
st.markdown(
    """
    <style>
        body {
            background-color: #f0f8ff;
            font-family: 'Poppins', sans-serif;
        }
        .header {
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            padding: 25px;
            text-align: center;
            font-size: 30px;
            color: white;
            font-weight: bold;
            border-radius: 15px;
            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
        }
        .convert-button {
            padding: 15px 25px;
            border: none;
            background: linear-gradient(135deg, #4682b4, #5a9bd5);
            color: white;
            font-size: 22px;
            font-weight: bold;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.3);
        }
        .convert-button:hover {
            background: linear-gradient(135deg, #5a9bd5, #4682b4);
            transform: scale(1.05);
            box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.4);
        }
        .result {
            font-size: 24px;
            font-weight: bold;
            color: #2a5298;
            margin-top: 25px;
            padding: 15px;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
            text-align: center;
        }
        .dropdown-container select {
            padding: 10px;
            font-size: 18px;
            border-radius: 10px;
            border: 2px solid #5a9bd5;
            transition: 0.3s;
            background: white;
        }
        .dropdown-container select:hover {
            border: 2px solid #1e3c72;
            background: #f0f8ff;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown('<div class="header">💰 PKR Currency Converter</div>', unsafe_allow_html=True)

# Currency input (Enter in PKR)
st.markdown("### Enter amount in PKR:")
amount = st.number_input("", value=1.0, min_value=0.0, step=0.5, format="%.2f")

# Currency selection
st.markdown("### Convert to:")
st.markdown('<div class="dropdown-container">', unsafe_allow_html=True)
currency = st.selectbox("Select Currency", ["USD", "GBP (UK)", "INR (India)", "RUB (Russia)", "CNY (China)"])
st.markdown('</div>', unsafe_allow_html=True)

# Dynamic conversion rates (Example rates, can be linked to an API for real-time updates)
def get_conversion_rate(currency):
    rates = {
        "USD": 0.0035,
        "GBP (UK)": 0.0028,
        "INR (India)": 0.29,
        "RUB (Russia)": 0.32,
        "CNY (China)": 0.025
    }
    return rates.get(currency, 1)

# Convert button with enhanced UX
if st.button("💱 Convert", key="convert", help="Click to convert PKR to selected currency"): 
    with st.spinner('🔄 Converting... Please wait...'):
        time.sleep(1.2)  # Simulate processing time
    converted = round(amount * get_conversion_rate(currency), 2)
    st.markdown(f'<div class="result">💰 {amount} PKR = **{converted} {currency}**</div>', unsafe_allow_html=True)
