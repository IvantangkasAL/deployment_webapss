import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title='aplikasi perhitungan sampling sampah (metode quartering)', page_icon=':computer:')

#sidebar
with st.sidebar:
    selected = st.sidebar.selectbox('aplikasi perhitungan nilai bobot jenis sampah', 
                                   ['kelompok 4','latar belakang','perhitungan sampling sampah'], index=0)


        
#kelommpok 2
if selected == 'kelompok 4':
    st.title('kelompok 4')
    st.write('Oleh Kelompok 4 :')
    st.write('Affan Usman (2230423)')
    st.write('Annafia Naila Kartika Putri(2230434)')
    st.write('Ivan Tangkas Alfareza(2230446)')
    st.write('Mutiara Eirene Lahira Lumban T (2230457)')
    st.write('Salwa Haura Sujana (2230469)')#
    
    
#latar belakang 
if selected=='latar belakang':
    st.subheader('Project Webapps Kelompok 4 :computer:')
    st.title('Selamat Datang :wave:')
    st.header('latar belakang')
    st.write('teknik sub sampling yang berdasarkan pada reduksi jumlah sampel homogenisasi. teknik ini dilakukan karena sampel sulit untuk homogenisasi dengan pengadukan karena jumlah sampel yang terlampau banyak dan ukuran partikelnya relatif besar dan tidak seragam. sampel sampah hasil sampling dimasukkan ke wadah sementara untuk dilakukan pengukuran tinggi dan komposisinya. dalam perhitungan sampling sampah sering ditemukan kesulitan saat perhitungan karena banyaknya data yang harus dihitung dan waktu yang sedikit. dengan adanya perkembangan teknologi aplikasi perhitungan,maka akan sangat mempermudah pengolahan data perhitungan,maka akan sangat mempermudah pengolahan data perhitungan pada saat sampling. dengan memanfaatkan aplikasi perhitungan maka akan lebih mudah untuk mengolah data perhitungan.')

#perhitungan sampling sampah
if  selected=='perhitungan sampling sampah':
        st.title ('perhitungan sampling sampah')
        option=st.selectbox(
    'Silahkan pilih satuan konsentrasi yang ingin dicari ',
    ('bobot sampel (kg)','volume(m³)','nilai berat jenis (kg/m³)','komposisi jenis sampah (%)'))
        
        if option=='bobot sampel (kg)':
            ksng=st.number_input('Masukkan bobot kosong wadah(kg)')
            total=st.number_input('Masukkan bobot total(kg)')
            if st.button('Hitung'):
                bst=total-ksng
                st.success(f'bobot sampel total sebesar {bst} kg')
        elif option=='volume(m³)':
            pjng=st.number_input('Masukan panjang sampah (m)')
            lbr=st.number_input('Masukan lebar sampah (m)')
            tng=st.number_input('Masukan tinggi sampah (m)')
            if st.button('Hitung'):
                Volume=pjng*lbr*tng
                st.success(f'Volume sampah sebesar {Volume} m³')
        elif option=='nilai berat jenis (kg/m³)':
            massa=st.number_input('Masukkan bobot sampel')
            v=st.number_input('Masukkan volume sampah')
            if st.button('Hitung'):
                nbj=massa/v
                st.success(f'nilai berat jenis sebesar {nbj}kg/m³')
        elif option=='komposisi jenis sampah (%)':
            jns=st.number_input('Masukkan bobot sampah perjenis')
            bst=st.number_input('Masukkan bobot sampel total')
            if st.button('Hitung'):
                kjs=jns/bst*100
                st.success(f'komposisi jenis sampah sebesar {kjs}%')
    
       
       
