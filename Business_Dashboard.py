import streamlit as st
import pandas as pd
import altair as alt


st.set_page_config(layout='wide', initial_sidebar_state='expanded',)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown("""
<style>
.big-font {
    font-size:46px !important;
    text-align: center; 
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.med-font {
    font-size:40px !important;
    text-align: center; 
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.text-font {
    font-size:20px !important;
    text-align: center; 
}
</style>
""", unsafe_allow_html=True)

#st.markdown("<h1 style='text-align: center; color: black;' >Business Insider</h1>", unsafe_allow_html=True)
st.markdown('<p class="big-font"><strong>UMKM Roda Perekonomian:</strong></p>', unsafe_allow_html=True)
st.markdown('<p class="med-font"><strong>Potensi Besar Yang Terhambat</strong></p>', unsafe_allow_html=True)
st.markdown('<p class="text-font">Indonesia saat ini berada pada posisi ke-16 terbesar dalam urutan GDP dunia. Hal ini menunjukan posisi ekonomi Indonesia yang semakin dekat pada posisi penting ekonomi dunia. Bahkan ditambah lagi dengan prediksi dari mckinsey dimana indonesia diprediksikan akan naik menjadi ke-7 terbesar pada tahun 2030. Hal ini tentunya dapat menjadi refleksi bagi Indonesia untuk memaksimalkan potensi yang ada guna mencapai masa depan yang maju. Data menunjukkan bahwa 61 persen domestik bruto (PDB) nasional  disumbangkan oleh UMKM. Hal ini menunjukkan bahwa UMKM berpotensi dalam memberikan dampak pada ekonomi Indonesia di masa depan. Namun pada kenyataannya saat ini UMKM mengalami hambatan dalam kegiatan bisnis yang dilakukan. Hal ini tentunya dapat menurunkan kemungkinan tercapainya masa depan yang diinginkan sehingga perlu untuk diperhatikan. </p>', unsafe_allow_html=True)
# Row A
st.markdown('### Indonesia di 2030')
col1, col2, col3 = st.columns(3)
col1.metric("Konsumen", "135 M", "45 M")
col2.metric("Posisi Ekonomi", "7 th", "7")
col3.metric("Market Opportunity", "1.8$ M", "1.3$ M")
st.caption(":grey[Sumber Data : Mckinsey]")
# Define the data
data = {
    'Year': ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'],
    'Jumlah UMKM': ['52,764,750', '54,114,821', '55,206,444', '56,534,592', '57,895,721', '59,262,772', '61,651,177', '62,922,617', '64,194,057']
}

# Create the DataFrame
Data_2 = pd.DataFrame(data)
Data_2['Jumlah UMKM'] = Data_2['Jumlah UMKM'].str.replace(',', '').astype(int)

# Create the bar chart using Altair
chart = alt.Chart(Data_2).mark_bar().encode(
    x='Year',
    y='Jumlah UMKM'
)

# Display the chart using Streamlit
st.altair_chart(chart, use_container_width=True)
st.caption(":grey[Sumber Data : Asean Development Bank]")
st.divider()



st.sidebar.markdown('<p class="med-font"><strong>Business Insight</strong></p>', unsafe_allow_html=True)
st.sidebar.markdown('<p class="text-font">Storytelling</p>', unsafe_allow_html=True)
st.sidebar.header("Dashboard  `Beta Version`")
st.sidebar.divider()
st.sidebar.title('Capstone Project')
st.sidebar.subheader(':blue[with]')
from PIL import Image
import requests
image = Image.open(requests.get('https://dqlab.id/files/dqlab/cache/6b8c33bdec694a9af1b696bef97d2d25_x_Thumbnail800.png',stream=True).raw)
st.sidebar.image(image)



st.markdown("# Hambatan")
st.markdown('<p class="text-font">Hambatan yang dialami sering kali berupa bisnis yang dijalankan tidak menggunakan kaidah bisnis yang tepat. Selain itu, faktor-faktor utama bisnis tidak dijalankan dengan baik dari mulai operasional, manajemen, finansial, sampai marketing. Hal ini karena kebanyakan bisnisnya berasal dari jenis bisnis yang sulit dijalankan dasar-dasar bisnis yang ada. </p>', unsafe_allow_html=True)
# Define the data
data = {
    'Year': [2010, 2011, 2012],
    'Agriculture': [50.0, 49.6, 48.8],
    'Manufacturing': [6.2, 6.4, 6.4],
    'Transportation': [6.5, 6.5, 6.9],
    'Wholesale and Retail Trade': [29.4, 29.6, 28.8],
    'Other Services': [6.3, 6.4, 6.9],
    'Others': [1.6, 1.6, 2.1]
}

# Create a data frame
df = pd.DataFrame(data)

# Create a select box to choose the year
selected_year = st.selectbox('Select Year', df['Year'])

# Filter the data frame based on the selected year
filtered_df = df[df['Year'] == selected_year]

# Reshape the data for Altair visualization
melted_df = filtered_df.melt(id_vars='Year', var_name='Sector', value_name='Percentage')

# Create the donut chart using Altair
chart = alt.Chart(melted_df).mark_arc().encode(
    theta='Percentage:Q',
    color='Sector:N',
    tooltip=['Sector', 'Percentage']
).properties(
    width=400,
    height=400,
    title=f"MSMEs by sector (% share) - {selected_year}"
)

# Display the chart
st.altair_chart(chart)
st.caption(":grey[Sumber Data : Asean Development Bank]")

st.markdown('<p class="text-font">UMKM sebagai bisnis tidak lepas dari aktivitas pengelolaan bisnis. Kenyataannya saat ini UMKM masih kurang mampu dalam melaksanakan hal ini dengan baik. Manajemen operasi yang tidak baik hingga perhitungan finansial menjadi masalah yang dihadapi UMKM. Hal ini dapat kita lihat lewat indikator NPL(Non Performing Loan) lewat bank. Indikator ini digunakan untuk melihat bagaimana UMKM sebagai pelaku kredit bermasalah atau tidak. Semakin besar maka semakin tidak baik. </p>', unsafe_allow_html=True)
# Row B



Data= {
    'Year': ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],
    'Rasio NPL': [2.2, 1.9, 1.7, 2.2, 2.5, 3.0, 2.6, 2.4, 2.5]
}

# Create the DataFrame
Data_1 = pd.DataFrame(Data)
chart = alt.Chart(Data_1).mark_line().encode(
    x='Year',
    y='Rasio NPL'
)

# Display the chart using Streamlit
st.altair_chart(chart, use_container_width=True)

st.caption(":grey[Sumber Data : Asean Development Bank]")

st.divider()
st.markdown('<p class="med-font"><strong>Lalu</strong> apa yang bisa dilakukan para pelaku <strong>UMKM</strong> untuk menjawab <strong>hambatan</strong> ini?</p>', unsafe_allow_html=True)
st.divider()
st.markdown("# Rekomendasi")
st.markdown('<p class="text-font"> Dengan permasalahan yang ada maka dibutuhkan solusi yang tepat sesuai dengan keadaan UMKM itu sendiri. Salah satu solusi yang tepat adalah dengan melakukan adaptasi digital terhadap proses-proses bisnis yang dilakukan. Hal ini sejalan dengan cita-cita untuk melakukan transformasi digital pada UMKM. Dalam melakukan transformasi maka perlu untuk memperhatikan hal-hal berikut.</p>', unsafe_allow_html=True)
st.markdown('<p class="text-font">1.) UMKM dengan tingkat kematangan digital yang tinggi: memanfaatkan teknologi digital untuk mendigitalkan organisasi;</p>', unsafe_allow_html=True)
st.markdown('<p class="text-font">2.) UMKM yang mengalami kendala likuiditas namun memiliki tingkat kematangan digital yang rendah: memanfaatkan teknologi digital hanya untuk tujuan penjualan dan pemasaran, dan;</p>', unsafe_allow_html=True)
st.markdown('<p class="text-font">3.) UMKM dengan literasi digital terbatas tetapi modal sosial tinggi: memanfaatkan teknologi digital untuk berkolaborasi dengan pihak lain yang memiliki literasi digital tinggi.</p>', unsafe_allow_html=True)
st.markdown('<p class="text-font"> Sehingga transformasi yang dilakukan dapat maksimal dan menghilangkan hambatan yang ada untuk kemajuan UMKM.</p>', unsafe_allow_html=True)
st.caption(":grey[Sumber : Mckinsey,Republika.id,COORDINATING MINISTRY FOR ECONOMIC AFFAIRS REPUBLIC OF INDONESIA Press Release:HM.4.6/178/SET.M.EKON.3/3/2022,Priyono., Moin,A., and Putri, V. (2020). Identifying Digital Transformation Paths In The Business Model of SMEs During The Covid-19 Pandemic. Journal of Open Innovation: Technology, Market, and Complexity 6(4): 1–22.]")