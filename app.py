import streamlit as st

st.set_page_config(
    page_title="My Portofolio",
    page_icon="🏡",
    layout = "wide"
) 

st.write("Selamat datang diberanda")
st.write("Welcome to My Apps")

st.page_link(
    "Pages/Home.py",
    label = "Lihat Home",
    icon = "🏡")

st.page_link(
    "Pages/Profil.py",
    label = "Lihat Profile",
    icon = "👤")

st.page_link(
    "Pages/Kemampuan.py",
    label = "Lihat Kemampuan",
    icon = "🧠")

st.page_link(
    "Pages/Sosial_media.py",
    label = "Lihat Sosial_media",
    icon = "❕")