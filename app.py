import streamlit as st
import math
import pandas as pd

# 🎨 Page Configuration
st.set_page_config(
    page_title="Sphere Calculator",
    page_icon="⚫",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 🖤 Custom Dark Theme Styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #000000;
            color: #FFFFFF;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #F39C12;
        }
        .css-1v3fvcr {
            color: white;
        }
        .css-qrbaxs {
            color: white;
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

# 📘 Educational Section
with st.expander("📚 How It Works"):
    st.markdown("""
    - **Surface Area Formula:** $A = 4 \\pi r^2$
    - **Volume Formula:** $V = \\frac{4}{3} \\pi r^3$
    
    Where:
    - $r$ is the radius of the sphere
    - $\\pi \\approx 3.14159$
    
    This tool helps you quickly find how much space a sphere takes up (volume) and how much surface it has (area).
    """)

# ✏️ User Input
st.markdown("### ✨ Enter the radius of your sphere below (in cm):")
radius = st.number_input("Radius", min_value=0.0, step=0.1, format="%.2f")

# ➕ Spacing
st.markdown("---")

# 🚀 Result Calculation
if radius:
    surface_area = calculate_surface_area(radius)
    volume = calculate_volume(radius)

    # 📊 Results
    st.markdown("### ✅ Results:")
    col1, col2 = st.columns(2)
    col1.metric(label="🌐 Surface Area", value=f"{surface_area:.2f} cm²")
    col2.metric(label="📦 Volume", value=f"{volume:.2f} cm³")

    # 📥 Download CSV
    result_df = pd.DataFrame({
        "Radius (cm)": [radius],
        "Surface Area (cm²)": [surface_area],
        "Volume (cm³)": [volume]
    })
    st.download_button("📥 Download Results as CSV", result_df.to_csv(index=False), file_name="sphere_results.csv")

    # 🎈 Animation
    st.success("🎉 Calculations complete!")
    st.balloons()
else:
    st.info("🔍 Please input a radius to begin the calculation.")

# 🙌 Team Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>👨‍💻 Created by <strong>Team Sphere</strong>: Abdullah, Teammate 2, Teammate 3</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>🛠️ Powered by <a href='https://streamlit.io' style='color:#F39C12'>Streamlit</a></p>", unsafe_allow_html=True)
