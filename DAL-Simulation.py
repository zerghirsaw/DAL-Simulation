# DAL - Drawback Asymmetrical Loop
# Copyright (C) 2025 Zerg Hirsaw
# This program is licensed under the GNU General Public License v3.0
# See LICENSE.txt for details.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

class DrawbackAsymmetricalLoop:
    def __init__(self, data):
        self.data = np.array(data)
        self.scaler = MinMaxScaler()

    def normalize_data(self):
        """ Normalisasi data agar nilainya antara 0 dan 1 """
        self.data = self.scaler.fit_transform(self.data.reshape(-1, 1)).flatten()

    def detect_pattern(self):
        """ Mendeteksi pola utama menggunakan regresi sederhana """
        trend = np.polyfit(range(len(self.data)), self.data, 1)
        return trend  # [slope, intercept]

    def find_negation(self):
        """ Mencari pola negasi dari data dengan inversi berbasis rata-rata """
        mean = np.mean(self.data)
        negation = [x if x < mean else mean - (x - mean) for x in self.data]
        return np.array(negation)

    def drawback_loop(self):
        """ Menggabungkan pola utama dan pola negasi untuk kesimpulan lebih akurat """
        self.normalize_data()
        pattern = self.detect_pattern()
        negation = self.find_negation()
        
        # Menghitung faktor keseimbangan (cross factor)
        cross_factor = abs(pattern[0]) / (np.std(self.data) + 1e-5)
        
        # Menghasilkan output final dengan integrasi DAL
        final_output = (self.data + negation * cross_factor) / 2  
        
        return final_output

# **📌 Buat Data Sederhana untuk Simulasi**
x = np.arange(1, 21)  # Data dari 1 hingga 20
y = np.array([5, 7, 10, 15, 20, 18, 17, 16, 14, 12, 8, 5, 3, 6, 9, 12, 16, 19, 22, 25])  # Tren naik-turun

# **📌 Terapkan DAL**
dal = DrawbackAsymmetricalLoop(y)
result = dal.drawback_loop()

# **📌 Plot Grafik Sebelum & Sesudah DAL**
plt.figure(figsize=(10, 5))
plt.plot(x, y, label="Data Awal", linestyle="--", marker="o", color="blue")
plt.plot(x, result, label="Hasil DAL", linestyle="-", marker="s", color="red")

# **📌 Tambahkan Label**
plt.xlabel("Waktu")
plt.ylabel("Nilai Data")
plt.title("Simulasi Drawback Asymmetrical Loop (DAL)")
plt.legend()
plt.grid()
plt.savefig("dal_result.png")
plt.show()
