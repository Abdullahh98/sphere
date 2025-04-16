import streamlit as st
import math
import pandas as pd

# 🎨 Page Configuration
st.set_page_config(
    page_title="Sphere Calculator",
    page_icon="🟠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 💅 Custom CSS Styling
st.markdown(
    """
    <style>
        .stApp {
            background-image: linear-gradient(135deg, #ece9e6 0%, #ffffff 100%);
            color: #333333;
            font-family: 'Segoe UI', sans-serif;
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

# 🏷️ Custom Title
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🔵 Sphere Surface Area & Volume Calculator</h1>", unsafe_allow_html=True)

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

# 📷 Image Example
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sphere_wireframe.svg/1024px-Sphere_wireframe.svg.png", caption="3D Sphere Representation", use_column_width=True)

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

    # 📥 Download Button
    result_df = pd.DataFrame({
        "Radius (cm)": [radius],
        "Surface Area (cm²)": [surface_area],
        "Volume (cm³)": [volume]
    })
    st.download_button("📥 Download Results as CSV", result_df.to_csv(index=False), file_name="sphere_results.csv")

    # 🎉 Celebration Animation
    st.success("🎉 Calculations complete!")
    st.balloons()
else:
    st.info("🔍 Please input a radius to begin the calculation.")

# 👨‍💻 Team Credits
st.markdown("---")
st.markdown("👨‍💻 Created by **Team Sphere**: Abdullah, Teammate 2, Teammate 3")
st.markdown("🛠️ Powered by [Streamlit](https://streamlit.io)")
