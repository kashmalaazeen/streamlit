import streamlit as st
from datetime import datetime

# Custom CSS for styling
st.markdown(
    """
    <style>
        .header {
            background-color: #232F3E;
            padding: 10px;
            text-align: center;
            font-size: 24px;
            color: white;
            font-weight: bold;
            border-radius: 8px;
        }
        .calculate-button {
            padding: 8px 15px;
            border: none;
            background-color: #FF9900;
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
st.markdown('<div class="header">📅 Age Calculator</div>', unsafe_allow_html=True)

# Date of Birth Input
dob = st.date_input("Enter your Date of Birth:")

# Calculate button
if st.button("🧮 Calculate Age"):
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.success(f"🎉 You are **{age}** years old!")