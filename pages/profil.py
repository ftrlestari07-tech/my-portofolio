import streamlit as st

st.title("👤 Profil Saya")

col1, col2, col3 = st.columns([1, 2, 3])

with col1:
    st.image(
        "pages/fitri.png",
        caption="Foto Profil",
        use_container_width=True
    )

with col2:
    st.header("Biodata")

    st.write("**Nama:** Fitri lestari")
    st.write("**Tempat Tinggal:** Jambi")
    st.write("**Status:** Mahasiswa")
    st.write("**Program Studi:** Sistem Informasi")
    st.write("**Hobi:** Nongkrong")

st.divider()

st.subheader("Tentang Saya")

st.write("""
Sebagai mahasiswa komputer, aku harus terus belajar, berusaha, dan tidak takut menghadapi kesulitan. 
Tidak apa-apa jika belum memahami semuanya sekarang, karena setiap kesalahan adalah bagian dari proses belajar. 
Aku percaya, kerja keras hari ini adalah langkah menuju masa depan yang sukses. 💻✨
""")