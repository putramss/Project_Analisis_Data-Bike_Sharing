# **Import Semua Packages/Library yang Digunakan**
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import plotly.express as px
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# Memuat data tabel day
import pandas as pd

day_df = pd.read_csv("https://raw.githubusercontent.com/putramss/Proyek_Analisis_Data-Bike_Sharing/main/Dashboard/cleaned_dataset_bikesharing.csv")
day_df.head()

# Memuat data tabel hour
import pandas as pd

hr_df = pd.read_csv("https://raw.githubusercontent.com/putramss/Proyek_Analisis_Data-Bike_Sharing/main/Dashboard/cleaned_dataset_bikesharing.csv")
hr_df.head()

# Menghapus kolom yang tidak digunakan
drop_col = ['instant', 'windspeed']

for i in day_df.columns:
  if i in drop_col:
    day_df.drop(labels=i, axis=1, inplace=True)

day_df.head()

# Mengubah informasi pada kolom
day_df.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weather_status',
    'cnt': 'count'
}, inplace=True)

day_df.head()

# Mengubah angka menjadi keterangan
day_df['month'] = day_df['month'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day_df['weekday'] = day_df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})
day_df['weather_status'] = day_df['weather_status'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

# Mengubah tipe data ke datetime
day_df['dateday'] = pd.to_datetime(day_df['dateday'])

# **Mengubah tipe data ke categorical**
day_df['season'] = day_df.season.astype('category')
day_df['year'] = day_df.year.astype('category')
day_df['month'] = day_df.month.astype('category')
day_df['holiday'] = day_df.holiday.astype('category')
day_df['weekday'] = day_df.weekday.astype('category')
day_df['workingday'] = day_df.workingday.astype('category')
day_df['weather_status'] = day_df.weather_status.astype('category')

day_df.head()

# Menpersiapkan filter components (komponen filter)
min_date = day_df["dateday"].min()
max_date = day_df["dateday"].max()

# Menampilkan logo Pedal Bikeshare pada sidebar
import pandas as pd
import streamlit as st

st.sidebar.image("https://media.istockphoto.com/id/1199831184/vector/public-city-bicycle-sharing-business-vector-flat-illustration-modern-automated-bike-rental.jpg?s=612x612&w=0&k=20&c=Ln20cn_A_xHqJ56iNBhbN8PEXl1ZBal5cwGpfbyWo2Q=")
st.sidebar.header("Filter:")

# Memilih rentang tanggal dengan date_input pada sidebar
start_date, end_date = st.sidebar.date_input(
    label="Date",
    min_value=day_df["dateday"].min(),
    max_value=day_df["dateday"].max(),
    value=[day_df["dateday"].min(), day_df["dateday"].max()],
    key="unique_key_date_input"
)

# Menampilkan header "Connect with me" pada sidebar
import pandas as pd
import streamlit as st

st.sidebar.header("Let's Connect:")

# Menginput icon media sosial pada sidebar
import pandas as pd
import streamlit as st

st.sidebar.markdown("[Profile](https://www.linkedin.com/in/putra-ramdhani-8a2b18218/)")


# Menambahkan tautan LinkedIn pada sidebar
col1 = st.sidebar
with col1:
    st.markdown("[Website](https://www.rodalink.com/id/bike-rent)")

# Menambahkan teks promosi pada sidebar
import pandas as pd
import streamlit as st

st.sidebar.markdown("Let's support Rodalink as an Indonesian product and get a better understanding of rental patterns, favorite weather categories, and more!")

# Menampilkan teks tagline pada sidebar
import pandas as pd
import streamlit as st

st.sidebar.markdown("Ride Beyond Boundaries: Your Journey, Your Bike – Seamless Bike Rental Experience for Every Adventure!")

# Menambahkan pemisah horizontal pada sidebar
import pandas as pd
import streamlit as st

st.sidebar.markdown("---")

# Menampilkan tautan dataset
import pandas as pd
import streamlit as st

st.sidebar.markdown("[Dataset](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view)")

# Hubungkan filter dengan main_df
main_df = day_df[
    (day_df["dateday"] >= str(start_date)) &
    (day_df["dateday"] <= str(end_date))
]

# Menampilkan judul "PedalMetrics: Bike Sharing Dashboard" di halaman utama
import pandas as pd
import streamlit as st

st.title("PedalMetrics: Bike Sharing Dashboard")
st.markdown("##")

# Membagi layar menjadi 3 kolom
col1, col2, col3 = st.columns(3)

# Menampilkan total rides di kolom pertama
with col1:
    total_all_rides = main_df['count'].sum()
    st.metric("Total Rides", value=total_all_rides)

# Menampilkan total casual rides di kolom kedua
with col2:
    total_casual_rides = main_df['casual'].sum()
    st.metric("Total Casual Rides", value=total_casual_rides)

# Menampilkan total registered rides di kolom ketiga
with col3:
    total_registered_rides = main_df['registered'].sum()
    st.metric("Total Registered Rides", value=total_registered_rides)

# Menampilkan pemisah horizontal
import pandas as pd
import streamlit as st

st.markdown("---")

# ----- CHART 1: Weather Factor Plot Bar -----
import pandas as pd
import plotly.express as px
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/putramss/Proyek_Analisis_Data-Bike_Sharing/main/Dashboard/cleaned_dataset_bikesharing.csv')

fig = px.bar(data, x='weathersit', y='count', color='weathersit',  # Change 'weather_status' to 'weathersit'
             color_discrete_map={'Clear/Partly Cloudy': '#9AD0C2', 'Misty/Cloudy': '#2D9596', 'Light Snow/Rain': '#265073'},
             labels={'count': 'Jumlah Pengguna Sepeda', 'weathersit': 'Kondisi Cuaca'},
             title='Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca')

st.plotly_chart(fig, use_container_width=True)


# ----- CHART 2: Season Factor Plot Bar -----
import pandas as pd
import plotly.express as px
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/putramss/Proyek_Analisis_Data-Bike_Sharing/main/Dashboard/cleaned_dataset_bikesharing.csv')

fig = px.bar(
    data,
    x='season',
    y='count',
    color='season',
    color_discrete_map={'1': '#E0F4FF', '2': '#87C4FF', '3': '#39A7FF'},  # Warna sesuai dengan kode yang diberikan
    labels={'count': 'Jumlah Pengguna Sepeda', 'season': 'Kondisi Musim'},
    title='Jumlah Pengguna Sepeda berdasarkan Kondisi Musim'
)

st.plotly_chart(fig, use_container_width=True)


# ----- CHART 3: K-Means Clustering Results of Temperature and Humidity Plot Bar -----

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import streamlit as st

data_hour = pd.read_csv('https://raw.githubusercontent.com/putramss/Proyek_Analisis_Data-Bike_Sharing/main/Dashboard/cleaned_dataset_bikesharing.csv')

features = data_hour[['temp', 'hum']]

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

num_clusters = 3

kmeans = KMeans(n_clusters=num_clusters, random_state=42)
data_hour['cluster'] = kmeans.fit_predict(features_scaled)

fig = px.scatter(data_hour, x='temp', y='hum', color='cluster', color_continuous_scale='viridis',
                 labels={'temp': 'Temperature', 'hum': 'Humidity', 'cluster': 'Cluster'},
                 title='Hasil Clustering Menggunakan K-Means')
fig.update_layout(xaxis_title='Temperature', yaxis_title='Humidity')

st.plotly_chart(fig)

st.caption('Copyright (C) 2024, Putra Ramdhani')