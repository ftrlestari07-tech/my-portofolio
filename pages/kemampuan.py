import streamlit as st

st.title("💡 Kemampuan")

st.markdown("### Hard Skills")
skills = {
    "Python": 80,
    "HTML & CSS": 70,
    "Streamlit": 65,
    "Microsoft Office": 85,
}

for nama, level in skills.items():
    st.write(f"**{nama}**")
    st.progress(level / 100, text=f"{level}%")

st.divider()

st.markdown("### Soft Skills")
col1, col2, col3 = st.columns(3)
col1.success("🤝 Kerja Sama Tim")
col2.success("🗣️ Komunikasi")
col3.success("⏱️ Manajemen Waktu")

st.divider()

st.markdown("### Proyek")
with st.expander("Proyek 1 - Website Portofolio"):
    st.write("Website portofolio pribadi menggunakan Streamlit.")
with st.expander("Proyek 2 - (isi proyekmu)"):
    st.write("Deskripsi proyek.")