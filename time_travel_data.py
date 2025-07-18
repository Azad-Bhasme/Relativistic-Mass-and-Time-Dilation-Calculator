import streamlit as st
import math

# Constants
c = 299792458  # Speed of light in m/s
rest_mass = 70000  # Rest mass in kg

# Page configuration
st.set_page_config(page_title="Relativistic Calculator", page_icon="🚀", layout="centered")

# Sidebar Navigation
st.sidebar.title("📂 Menu")
selected_page = st.sidebar.selectbox("Go to", ["Home", "About"])

# ---------------- HOME PAGE ------------------
if selected_page == "Home":
    st.title("🚀 Relativistic Mass & Time Dilation Calculator")
    st.markdown("Explore how velocity near the speed of light affects mass and time using Einstein’s special relativity.")

    # Speed input
    percent = st.slider("Select speed as % of light:", 0.0, 99.99, 50.0)
    v = (percent / 100.0) * c

    if v >= c:
        st.error("Speed must be less than the speed of light!")
    else:
        # Lorentz factor (γ)
        gamma = 1 / math.sqrt(1 - (v / c) ** 2)
        new_mass = rest_mass * gamma

        # Display results
        st.write(f"### 🧪 New Relativistic Mass: `{new_mass:,.2f} kg`")

        # Distances to stars
        destinations = {
            "🌟 Alpha Centauri": 4.3,
            "🪐 Barnard’s Star": 6.0,
            "🔥 Betelgeuse": 309,
            "🌌 Andromeda Galaxy": 2_000_000
        }

        st.write("### 🕒 Time Experienced by Astronauts")
        for star, distance in destinations.items():
            time_experienced = distance / gamma
            st.write(f"- **{star}** ({distance} light-years): `{time_experienced:.2f}` years")

        st.write(f"ℹ️ Lorentz Factor (γ): `{gamma:.4f}`")

# ---------------- ABOUT PAGE ------------------
elif selected_page == "About":
    st.title("📘 About This App")
    st.markdown("""
This interactive app demonstrates concepts from **Einstein’s Theory of Special Relativity**, such as how mass increases and time slows down as speed approaches the speed of light.

---

### 🔍 Features:
- Calculate **relativistic mass** based on selected speed
- Simulate **time dilation** effects for interstellar journeys
- Compare time passed for astronauts vs Earth observers

---

### 🧠 Formula Used:
Lorentz Factor (γ):
\\[
\\gamma = \\frac{1}{\\sqrt{1 - \\left(\\frac{v}{c}\\right)^2}}
\\]

Relativistic Mass:
\\[
m = m_0 \\times \\gamma
\\]

Experienced Time:
\\[
t' = \\frac{d}{\\gamma}
\\]

---

### 👨‍💻 Developer
Made with ❤️ by **Azad Bhasme**  
Built using **Python** and **Streamlit**
""", unsafe_allow_html=True)

# ---------------- FOOTER ------------------
st.markdown(
        "<div style='text-align: center; margin-top: 3rem;'>"
        "Made with <span style='color:red; animation: blink 1.5s infinite;'>❤️</span> by <strong>Azad Bhasme</strong> | Relativistic Calculator © 2025"
        "</div><style>@keyframes blink {0%{opacity:1;}50%{opacity:0.3;}100%{opacity:1;}}</style>",
        unsafe_allow_html=True,
)
