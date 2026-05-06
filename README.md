Autonomous Financial Guard: ML-Driven Sharia-Compliant Stock Analyst

Hakkında (About / Description)

Bu proje, borsa verilerini otonom olarak tarayan ve makine öğrenmesi (Random Forest) algoritmalarını kullanarak finansal uygunluk analizi yapan bir Karar Destek Sistemi (Decision Support System) ürünüdür. Sistem, karmaşık finansal tabloları analiz ederek yatırım kriterlerine (Borç/Piyasa Değeri oranları vb.) göre proaktif risk değerlendirmesi yapar.

Öne Çıkan Özellikler (Key Features)
Otonom Veri Madenciliği: yfinance API entegrasyonu ile canlı borsa verilerinin (Market Cap, Total Debt, Cash) gerçek zamanlı olarak çekilmesi.

Makine Öğrenmesi Tabanlı Sınıflandırma: Scikit-Learn kütüphanesi ve Random Forest Classifier algoritması ile eğitilmiş, yüksek doğruluk oranına sahip tahminleme modeli.

Gelecek Projeksiyonu: Doğrusal Regresyon (Linear Regression) ile şirketlerin borçlanma eğilimlerini önceden tahmin eden trend analizi.

Dinamik Risk Analizi: Sadece sabit eşiklere (hard-coded rules) değil, veriler arasındaki olasılıksal ilişkilere dayalı "Güven Skoru" üretimi.

Sürekli İzleme (Looping): Zamanlanmış görevler (Time-based triggers) ile sistemin kendi kendine güncellenen otonom yapısı.

Kategori,Araçlar

Dil,Python 3.x
Veri Analizi,"Pandas, Numpy"
Makine Öğrenmesi,"Scikit-Learn (Random Forest, Linear Regression)"
Veri Kaynağı,Yahoo Finance API (yfinance)
Model Yönetimi,Joblib (Model Persistence)
Geliştirme Ortamı,"VS Code, Google Colab"

Nasıl Çalışır? (Technical Workflow)

Data Ingestion: Hedeflenen hisse senetlerinin finansal verileri API üzerinden çekilir.

Preprocessing: Ham veriler Pandas aracılığıyla normalize edilir ve modelin anlayacağı özniteliklere (features) dönüştürülür.

Inference: Önceden eğitilmiş ve joblib ile kaydedilmiş yapay zeka modeli (.pkl), yeni verileri sınıflandırır.

Actionable Insights: Sistem, her şirket için "Yatırıma Uygun" veya "Riskli" etiketini, %0-100 arası bir olasılık değeriyle (Confidence Score) raporlar.

Not:
"Bu proje, finansal özgürlük yolunda veriye dayalı kararlar alabilmek amacıyla, klasik finansal analiz yöntemlerini modern yapay zeka teknikleriyle otomatize etmek için geliştirilmiştir."