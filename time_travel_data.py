import streamlit as st
import math

# Constants
c = 299792458  #speed of light
rest_mass = 70000   #mass
# Header
st.title("🚀 Relativistic Mass & Time Dilation Calculator")
st.markdown("Calculate how speed affects mass and time perception using Einstein’s special relativity.")

# User input
percent = st.slider("Select speed as % of light:", 0.0, 99.99, 50.0)
v = (percent / 100.0) * c

# gamma / Lorentz factor
if v >= c:
    st.error("Speed must be less than the speed of light!")
else:
    gamma = 1 / math.sqrt(1 - (v / c) ** 2)
    new_mass = rest_mass * gamma

    # Output results
    st.write(f"### 🧪 New Relativistic Mass: `{new_mass:,.2f} kg`")

    # Destinations  & time
    destinations = {
        "Alpha Centauri": 4.3,
        "Barnard’s Star": 6.0,
        "Betelgeuse": 309,
        "Andromeda Galaxy": 2000000
    }

    st.write("### 🕒 Time Experienced by Astronauts")
    for star, distance in destinations.items():
        time = distance / gamma
        st.write(f"- **{star}**: `{time:.2f}` years")

    # Optional: Show gamma value
    st.write(f"ℹ️ Lorentz Factor (γ): `{gamma:.4f}`")
st.markdown(
    "<hr style='border:1px solid #ccc;'>"
    "<div style='text-align:center; padding-top:10px;'>"
    "Made with ❤️ by <strong>Azad Bhasme</strong>"
    "</div>",
    unsafe_allow_html=True
)
