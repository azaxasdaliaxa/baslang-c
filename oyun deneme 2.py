import random

def zindan_macerasi():
    print("Zindan Macerasına Hoş Geldiniz!")
    print("Sen bir zindandasın ve senin buradan kaçman gerekiyor.")
    
    puan = 0
    
    while True:
        print("\nOdada ne yapmak istersin?")
        print("1. Kapıyı aç ve ilerle")
        print("2. Masaya bak duvardaki posterleri incele")
        print("3. Pencereye yaklaş")
        print("4. Oyundan çık")
        
        secim = input("Seçiminizi yapın (1/2/3/4): ")
        
        if secim == "1":
            puan += random.randint(1, 3)
            print("Kapıyı açıyorsun önünde bir ceset var cesetin üstündeki silahı alıp ilerliyorsun önüne çıkan ölüp dirilmiş canlıları öldürüyorsun en sonunda bir kapı buluyorsan ve kendini içeri atıyorsun ama dışarı değil farklı bir dünyaya atıyor seni üzgünüm oyuncu daha yeni başlıyoruz.")
        elif secim == "2":
            puan += random.randint(0, 1)
            print("Masanın altında bir fener buldun posterlerin arkasında bir yol buldun fenerle içeri baktın kaçış tüneline benzetip içeri girdin ve kaçmayı başardın tebrikler oyuncu.")

        elif secim == "3":
            puan += random.randint(0, 2)
            print("Pencere çok yüksekte ve kaçamazsın sinir krizi geçirdin ve pes ettin kendini ölüme terk ettin.")
        elif secim == "4":
            print("Oyundan çıkılıyor...")
            break
        else:
            print("Geçerli bir seçenek seçmelisiniz (1/2/3/4).")
        
        if puan >= 10:
            print("Tebrikler! Oyundan başarıyla kaçtınız!")
            break
        
        print(f"Puanınız: {puan}")

if __name__ == "__main__":
    zindan_macerasi()
