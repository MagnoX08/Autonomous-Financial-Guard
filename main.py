import yfinance as yf
import joblib
import time

try:
    model = joblib.load("yatirim_asistani.pkl")
    print("✅ Yapay Zeka Modeli Başarıyla Yüklendi.")
except:
    print("❌ HATA: 'yatirim_asistani.pkl' dosyası bulunamadı! Lütfen dosyayı klasöre ekle.")

def otonom_analiz():
    hisseler = ["AAPL", "MSFT", "GOOGL", "TSLA"] 
    
    print(f"\n--- {time.strftime('%Y-%m-%d %H:%M:%S')} Analizi Başlatılıyor ---")
    
    for sembol in hisseler:
        try:
            hisse = yf.Ticker(sembol)
            info = hisse.info
            borc_orani = info.get('totalDebt', 0) / info.get('marketCap', 1)
            tahmin = model.predict([[borc_orani]]) 
            
            if tahmin[0] == 1:
                print(f"🚀 {sembol}: Yatırıma UYGUN (Borç Oranı: {borc_orani:.4f})")
            else:
                print(f"⚠️ {sembol}: RİSKLİ / UYGUN DEĞİL")
                
        except Exception as e:
            print(f"❌ {sembol} verisi çekilemedi: {e}")

if __name__ == "__main__":
    while True:
        otonom_analiz()
        print("\n😴 1 saat bekleniyor...")
        time.sleep(3600)