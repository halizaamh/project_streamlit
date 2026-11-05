import streamlit as st

st.title("Contoh Program Streamlit Dari Nur Haliza Muhayati")
with st.form(key="my_form"):
    nama = st.text_input("Nama Lengkap")
    kelas = st.text_input("Kelas")
    jenis_kelamin = st.radio("Jenis Kelamin", ("Laki-laki", "Perempuan"))
    submit = st.form_submit_button(label="Kirim")