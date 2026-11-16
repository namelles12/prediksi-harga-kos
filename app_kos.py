import streamlit as st
import pandas as pd
import joblib

st.title("🏠 Prediksi Harga Kos Madiun")

@st.cache_resource
def muat_model():
    return joblib.load("model_kos.joblib")

model = muat_model()

jarak = st.slider("Jarak ke kampus (km)", 0.3, 5.0, 1.0, 0.1)
rating = st.slider("Rating kos", 3.0, 5.0, 4.0, 0.1)
ac = st.selectbox("Fasilitas AC", ["ya", "tidak"])

if st.button("🔮 Prediksi Harga"):
    data_baru = pd.DataFrame({
        "jarak_km": [jarak],
        "rating": [rating],
        "ac_num": [1 if ac == "ya" else 0]
    })

    harga = model.predict(data_baru)[0]

    st.success(f"Perkiraan harga: Rp {harga:.0f} ribu / bulan")
