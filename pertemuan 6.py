import streamlit as st

st.set_page_config(page_title="Form Biodata", page_icon="🩺")

# ---------- Latar belakang bertema dokter (CSS) ----------
medical_pattern = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='80' height='80'>"
    "<path d='M32 20h16v12h12v16H48v12H32V48H20V32h12z' "
    "fill='%23ffffff' fill-opacity='0.35'/></svg>"
)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #bfe9e4;
        background-image: url("{medical_pattern}"),
                          linear-gradient(135deg, #d9f3f0 0%, #8fd3cc 100%);
        background-attachment: fixed;
    }}
    [data-testid="stForm"] {{
        background: rgba(255, 255, 255, 0.92);
        border: 2px solid #1b9aaa;
        border-radius: 16px;
        padding: 24px;
    }}
    h1 {{ color: #0b5563; }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🩺 Contoh Program Streamlit Dari Nur Haliza Muhayati")

with st.form(key="my_form"):
    nama = st.text_input("Nama Lengkap")
    kelas = st.text_input("Kelas")
    jenis_kelamin = st.radio("Jenis Kelamin", ("Laki-laki", "Perempuan"))
    cita_cita = st.text_input("Cita-cita")
    hobi = st.text_input("Hobi")
    gambar = st.file_uploader("Upload Gambar", type=["png", "jpg", "jpeg"])
    submit = st.form_submit_button(label="Kirim")

if submit:
    if not nama:
        st.warning("Nama Lengkap wajib diisi.")
    else:
        st.success("Data berhasil dikirim! ✅")
        st.subheader("Hasil Input")
        st.write(f"**Nama Lengkap:** {nama}")
        st.write(f"**Kelas:** {kelas}")
        st.write(f"**Jenis Kelamin:** {jenis_kelamin}")
        st.write(f"**Cita-cita:** {cita_cita}")
        st.write(f"**Hobi:** {hobi}")
        if gambar is not None:
            st.image(gambar, caption="Gambar yang diupload", width=250)