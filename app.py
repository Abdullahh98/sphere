import streamlit as st
import math

def calculate_surface_area(radius):
    return 4 * math.pi * radius ** 2

def calculate_volume(radius):
    return (4 / 3) * math.pi * radius ** 3

st.title("🔵 Sphere Surface Area & Volume Calculator")

st.write("Enter the radius of the sphere to calculate its surface area and volume.")

radius = st.number_input("Radius (in cm)", min_value=0.0, step=0.1)

if radius:
    surface_area = calculate_surface_area(radius)
    volume = calculate_volume(radius)

    st.success(f"🌐 Surface Area: {surface_area:.2f} cm²")
    st.success(f"📦 Volume: {volume:.2f} cm³")
