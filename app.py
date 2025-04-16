import streamlit as st
import math

# 🎨 Page Configuration
st.set_page_config(
    page_title="Sphere Calculator",
    page_icon="🟠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 🎨 Custom Styling
st.markdown(
    """
    <style>
        .stApp {
            background-image: linear-gradient(135deg, #ece9e6 0%, #ffffff 100%);
            padding: 2rem;
        }
        h1 {
            font-size: 2.5rem;
            color: #4B8BBE;
        }
        .metric-label {
            font-weight: bold;
            color: #2c3e50;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🧠 Functions
def calculate_surface_area(radius):
    return 4 * math.pi * radius ** 2

def calculate_volume(radius):
    return (4 / 3) * math.pi * radius ** 3

# 🏷️ Title
st.markdown("<h1 style='text-align: center;'>🔵 Sphere Surface Area & Volume Calculator</h1>", unsafe_allow_html=True)

# ✏️ Input
st.markdown("### ✨ Enter the radius of your sphere below (in cm):")
radius = st.number_input("", min_value=0.0, step=0.1, format="%.2f")

st.markdown("---")  # Separator

# 📊 Output
if radius:
    surface_area = calculate_surface_area(radius)
    volume = calculate_volume(radius)

    st.markdown("### ✅ Results:")
    col1, col2 = st.columns(2)
    col1.metric(label="🌐 Surface Area", value=f"{surface_area:.2f} cm²")
    col2.metric(label="📦 Volume", value=f"{volume:.2f} cm³")

    # 🎉 Confetti Animation
    st.markdown(
        """
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.4.0/dist/confetti.browser.min.js"></script>
        <script>
        confetti({
          particleCount: 120,
          spread: 90,
          origin: { y: 0.6 }
        });
        </script>
        """,
        unsafe_allow_html=True
    )
else:
    st.info("🔍 Please input a radius to begin the calculation.")
