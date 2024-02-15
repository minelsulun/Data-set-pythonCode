import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını oku
df = pd.read_csv("veri_seti.csv")

# Tarih sütununu indeks olarak ayarla
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Her bir grafik için yeni ekran penceresi oluştur
fig, axes = plt.subplots(3, 1, figsize=(10, 18))

# Yakılan Kalori grafiğini çizdir
axes[0].plot(df.index, df['move(KCAL)'], marker='o', color='r')
axes[0].set_title('Yakılan Kalori (Kcal)')
axes[0].set_ylabel('Kcal')
axes[0].grid(True)

# Adım Sayısı grafiğini çizdir
axes[1].plot(df.index, df['steps'], marker='o', color='g')
axes[1].set_title('Adım Sayısı')
axes[1].set_ylabel('Adım')
axes[1].grid(True)

# Gidilen Mesafe grafiğini çizdir
axes[2].plot(df.index, df['distance(KM)'], marker='o', color='b')
axes[2].set_title('Gidilen Mesafe (km)')
axes[2].set_ylabel('Mesafe (km)')
axes[2].grid(True)

# Eksen etiketlerini döndür
for ax in axes:
    ax.set_xlabel('Tarih')
    ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
