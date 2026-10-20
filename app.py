import streamlit as st

# Pengaturan Halaman
st.set_page_config(page_title="CV | Aima Ledyana Sari", page_icon="👩‍💻", layout="centered")

# Bagian Header / Kontak
st.title("Aima Ledyana Sari")
st.markdown("**D3 Sistem Informasi | Universitas Bina Sarana Informatika**")
st.write("📍 Bedoyo, Pereng, Mojogedang | 📞 0821-3288-1821 | ✉️ ledyanaaima@gmail.com")

st.markdown("---")

# Bagian Ringkasan Profil
st.header("👤 Ringkasan Profil")
st.write(
    "Lulusan D3 Sistem Informasi dengan pencapaian akademis yang sangat memuaskan (IPK 3,8). "
    "Memiliki pengalaman magang di instansi pemerintahan dengan keterlibatan langsung dalam "
    "pengembangan web, pelayanan publik (Kartu BST), dan manajemen acara. Memiliki minat besar "
    "di bidang teknologi informasi dan administrasi."
)

# Bagian Pendidikan
st.header("🎓 Pendidikan")
st.subheader("Universitas Bina Sarana Informatika (UBSI)")
st.write("**D3 Sistem Informasi**")
st.write("🏆 IPK: 3,8")

# Bagian Pengalaman
st.header("💼 Pengalaman Magang")
st.subheader("Dinas Perhubungan (Dishub)")
st.write(
    """
    - **Pembuatan Website:** Turut membantu dalam proses perancangan dan pembuatan website untuk kebutuhan instansi.
    - **Pelayanan Publik:** Membantu proses pembuatan dan administrasi kartu BST (Batik Solo Trans).
    - **Kepanitiaan Acara:** Membantu menjadi panitia dan memastikan kelancaran berbagai acara yang diselenggarakan oleh Dishub.
    """
)

# Bagian Keahlian
st.header("🛠️ Keahlian")
col1, col2 = st.columns(2)
with col1:
    st.write("**Hard Skills:**")
    st.write("- Pembuatan & Pengembangan Web")
    st.write("- Analisis Sistem Informasi")
    st.write("- Manajemen Basis Data")
    st.write("- Microsoft Office (Word, Excel)")
with col2:
    st.write("**Soft Skills:**")
    st.write("- Kerja Sama Tim (Teamwork)")
    st.write("- Komunikasi & Pelayanan Publik")
    st.write("- Pemecahan Masalah (Problem Solving)")
    st.write("- Manajemen Acara")

st.markdown("---")
st.caption("Dibuat menggunakan Streamlit 🚀")
