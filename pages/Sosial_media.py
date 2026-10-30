import streamlit as st

st.title("🌐 Sosial Media")
st.write("Ayo terhubung dengan saya lewat platform berikut:")

st.divider()

# Ganti URL dengan akun milikmu
akun = [
    ("📸 Instagram", "https://www.instagram.com/usernamekamu"),
    ("🎵 TikTok", "https://www.tiktok.com/@usernamekamu"),
    ("💼 LinkedIn", "https://www.linkedin.com/in/usernamekamu"),
    ("🐙 GitHub", "https://github.com/usernamekamu"),
    ("▶️ YouTube", "https://www.youtube.com/@usernamekamu"),
]

for nama, url in akun:
    st.link_button(nama, url, use_container_width=True)

st.divider()

st.markdown("### 📩 Kirim Pesan")
with st.form("form_kontak"):
    nama = st.text_input("Nama")
    pesan = st.text_area("Pesan")
    kirim = st.form_submit_button("Kirim")

if kirim:
    if nama and pesan:
        st.success(f"Terima kasih, {nama}! Pesanmu sudah terkirim.")
    else:
        st.warning("Mohon isi nama dan pesan terlebih dahulu.")