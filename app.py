import streamlit as st
import math

# 🎨 Page Configuration
st.set_page_config(
    page_title="Sphere Calculator",
    page_icon="🟠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 🎀 Custom CSS Styling for background and look
st.markdown(
    """
    <style>
        body {
            background-color: #f2f2f2;
        }
        .stApp {
            background-image: linear-gradient(135deg, #ece9e6 0%, #ffffff 100%);
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🧠 Calculation Functions
def calculate_surface_area(radius):
    return 4 * math.pi * radius ** 2

def calculate_volume(radius):
    return (4 / 3) * math.pi * radius ** 3

# 🏷️ Title
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🔵 Sphere Surface Area & Volume Calculator</h1>", unsafe_allow_html=True)

# ✏️ Input Section
st.markdown("### ✨ Enter the radius of your sphere below (in cm):")
radius = st.number_input("", min_value=0.0, step=0.1, format="%.2f")

st.markdown("---")

# 📊 Results
if radius:
    surface_area = calculate_surface_area(radius)
    volume = calculate_volume(radius)

    st.markdown("### ✅ Results:")
    col1, col2 = st.columns(2)
    col1.metric(label="🌐 Surface Area", value=f"{surface_area:.2f} cm²")
    col2.metric(label="📦 Volume", value=f"{volume:.2f} cm³")
    st.balloons()
else:
    st.info("🔍 Please input a radius to begin the calculation.")
