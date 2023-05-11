import streamlit as st
from model import *

st.title('Prediksi obat yang akan diberikan')

st.subheader('Anda harus mengisi data berupa umur,\
             jenis kelamin, level tekanan darah,\
             level kolesterol, dan rasio Na terhadap Potasium')

data = [[0]*5]


# section untuk mengisi form umur
age = st.slider('Umur :', 15, 74, 15)
data[0][0] = (age)


# section untuk mengisi form kelamin
gender = st.radio(
    "Jenis kelamin :",
    ('Pria', 'Wanita'))

if gender == 'Pria':
    data[0][1] = (encode_input(['M'], 'Sex'))

if gender == 'Wanita':
    data[0][1] = (encode_input(['F'], 'Sex'))


# section untuk mengisi form level tekanan darah
sis = st.slider('Sistolik :', 0, 200, 0)
dias = st.slider('Diastolik :', 0, 125, 0)

if sis >= 140 and dias >= 90:
    data[0][2] = (encode_input(['HIGH'], 'BP'))
    st.markdown('Tekanan darah anda tinggi')

if sis < 90 and dias < 60:
    data[0][2] = (encode_input(['LOW'], 'BP'))
    st.markdown('Tekanan darah anda rendah')

else:
    data[0][2] = (encode_input(['NORMAL'], 'BP'))
    st.markdown('Tekanan darah anda normal')


# section untuk mengisi form level kolesterol
chole = st.slider('Kadar kolesterol :', 0, 500, 0)

if chole >= 200:
    data[0][3] = (encode_input(['HIGH'], 'Cholesterol'))
    st.markdown('Level kolesterol anda tinggi')

else:
    data[0][3] = (encode_input(['NORMAL'], 'Cholesterol'))
    st.markdown('Level kolesterol anda normal')


# section untuk mengisi form rasio Na terhadap Potasium
nat = st.slider('Rasio Na terhadap Potasium :', 6.00, 39.00, 6.00, step=0.01)
data[0][4] = (nat)


# section untuk menampilkan prediksi
st.header(f'Obat yang harus diminum adalah {reverse_output(data)[0]}')