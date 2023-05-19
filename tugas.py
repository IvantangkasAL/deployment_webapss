import streamlit as st

st.title(':greens[Aplikasi Perhitungan Sampling Sampah Motode Quartering]')
st.write('Aplikasi ini dibuat oleh Kelompok 4 dari kelas IF Pengolahan Limbah Industri beranggotakan:')
st.write("1.Affan Usman (2230423)")
st.write("2.Annafia Naila Kartika Putri (2230434)")
st.write("3.Ivan Tangkas Alfareza (2230446)")
st.write("4.Mutiara Eirene Lahira Lumban T (2230457)")
st.write("5.Salwa Haura Sujana (2230469)")


tab1, tab2, tab3, tab4, tab5 = st.tabs(['Halaman Utama', 'Bobot Sampel (kg)', 'Volume(m³)', 'Nilai Berat Jenis(kg/m³)', 'Komposisi Jenis Sampah(%)'])

with tab1:
    st.header("Selamat Datang")
    st.markdown("""
       Sampah adalah sisa kegiatan sehari-hari manusia atau proses alam yang berbentuk padat atau semi padat berupa zat organik atau anorganik bersifat dapat terurai atau tidak dapat terurai yang dianggap sudah tidak berguna lagi.

   Metode quartering adalah metode percontohan yaitu memasukkan bahan yang akan diambil sampelnya lalu disebar menjadi segiempat atau lingkaran kemudian dibagi menjadi 4 bagian lalu diambil ¼ bagian. Dimana dari ¼ bagian tersebut sudah mewakili keseluruhan.

   Wadah adalah tempat untuk mengukur volume sampah yang telah dilakukan penyeleksian dengan teknik Quartering, pada umumnya wadah yang digunakan berbentuk balok karena mudah untuk menentukan volume sampah.""")

with tab2:
    st.header("Bobot Sampel (Kg)")
    st.write("Bobot sampel = W1 – Wo")
    st.write(" Ket :")
    st.write("W1 = Bobot total")
    st.write("Wo = Bobot kosong wadah")
    kosong = st.number_input(f"Masukkan bobot kosong wadah(kg)")
    total = st.number_input("Masukkan bobot total(kg)")

        
    if st.button("Hitung"):
            bst = total - kosong
            st.success(f"Bobot sampel total sebesar {bst:.4f} kg")

with tab3:
    st.header("Volume (m³)")
    st.write("Volume (m3) = p × l × t")
    st.write("Ket :")
    st.write("P = Panjang (cm)")
    st.write("l = Lebar (cm)")
    st.write("t = Tinggi (cm)")
    panjang = st.number_input("Masukkan panjang sampah (cm)")
    lebar = st.number_input("Masukkan lebar sampah (cm)")
    tinggi = st.number_input("Masukkan tinggi sampah (cm)")
   
    if st.button("Hitung volume"):
        volume = (panjang * lebar * tinggi) / 1000
        st.success(f"Volume sampah sebesar {volume:.2f} m³")

        
with tab4:
    st.header("Nilai Berat Jenis (kg/m³)")
    st.write("Berat jenis (Kg/m3) = M / V")
    st.write("Ket :")
    st.write("M = Bobot sampel (Kg)")
    st.write("V = Volume (m3)")
    massa = st.number_input(f"Masukkan bobot sampel (Kg)")
    v = st.number_input("Masukkan volume (m³)")
    
    if st.button("Hitung nilai berat jenis"):
        nbj = massa / v
        st.success(f"Nilai berat jenis sebesar {nbj:.4f} Kg/m³")

with tab5:
    st.header("Komposisi Jenis Sampah (%)")
    st.write("Komposisi jenis sampah (%) = Bobot sampah perjenis / Bobot sampel × 100%")
    st.write("Ket :")
    st.write("Bobot sampah perjenis (Kg)")
    st.write("Bobot sampel (Kg)")
    jns = st.number_input("Masukkan bobot sampah perjenis (Kg)")
    bst = st.number_input("Masukkan bobot sampel total (Kg)")
    
    if st.button("Hitung komposisi jenis sampah"):
        kjs = jns / bst * 100
        st.success(f"Komposisi jenis sampah sebesar {kjs:.2f} %")

