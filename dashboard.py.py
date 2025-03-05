import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
DATA_PATH = "data_baru.csv"
df = pd.read_csv(DATA_PATH)

# Streamlit UI
st.title("Dashboard Analisis Data")

# Menampilkan info dasar
st.subheader("Info Dataset")
st.write(df.head())
st.write("Jumlah baris dan kolom:", df.shape)

# Pertanyaan 1: Ada berapakah jumlah kategori produk yang ada?
if "product_category_name" in df.columns:
    num_categories = df["product_category_name"].nunique()
    st.write(f"Jumlah kategori produk yang ada: {num_categories}")

# Pertanyaan 2: Kategori produk mana yang memiliki jumlah foto produk terbanyak?
if "product_category_name" in df.columns and "product_photos_qty" in df.columns:
    top_category = df.groupby("product_category_name")["product_photos_qty"].sum().idxmax()
    st.write(f"Kategori produk dengan jumlah foto produk terbanyak: {top_category}")

# Sidebar filter
st.sidebar.header("Filter Data")
selected_column = st.sidebar.selectbox("Pilih Kolom untuk Visualisasi", df.columns)

# Visualisasi
st.subheader("Histogram dari " + selected_column)
fig, ax = plt.subplots()
df[selected_column].hist(bins=20, edgecolor='black', ax=ax)
st.pyplot(fig)

# Scatter plot jika ada kolom numerik
numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
if len(numeric_columns) > 1:
    st.subheader("Scatter Plot")
    x_axis = st.selectbox("Pilih Kolom X", numeric_columns)
    y_axis = st.selectbox("Pilih Kolom Y", numeric_columns)
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
    st.pyplot(fig)

st.write("Selesai!")