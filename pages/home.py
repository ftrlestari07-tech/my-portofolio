import streamlit as st

st.title("🏠 Selamat Datang!")
st.subheader("Halo, saya [FITRI LESTARI]")

st.write(
    """
    Selamat datang di website portofolio pribadi saya.
    Di sini kamu bisa mengenal lebih jauh tentang saya, melihat
    kemampuan yang saya miliki, dan terhubung lewat sosial media.
    """
)

st.divider()

st.markdown("### 📌 Menu")
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/profil.py", label="Profil", icon="👤")
with col2:
    st.page_link("pages/kemampuan.py", label="Kemampuan", icon="💡")
with col3:
    st.page_link("pages/sosial_media.py", label="Sosial Media", icon="🌐")

st.info("Gunakan menu di sidebar atau tombol di atas untuk berpindah halaman.")