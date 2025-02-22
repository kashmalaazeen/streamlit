import streamlit as st

# Custom CSS
st.markdown(
    """
    <style>
        .header {
            background-color: #1E90FF;
            padding: 10px;
            text-align: center;
            font-size: 24px;
            color: white;
            font-weight: bold;
            border-radius: 8px;
        }
        .convert-button {
            padding: 8px 15px;
            border: none;
            background-color: #FFA500;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown('<div class="header">🌡️ Temperature Converter</div>', unsafe_allow_html=True)

# Temperature input
temp = st.number_input("Enter temperature:", value=0.0)

# Conversion choice
option = st.radio("Convert to:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

# Convert button
if st.button("🔄 Convert"):
    if option == "Celsius to Fahrenheit":
        result = (temp * 9/5) + 32
        st.success(f"🌡️ {temp}°C = **{result}°F**")
    else:
        result = (temp - 32) * 5/9
        st.success(f"🌡️ {temp}°F = **{result}°C**")