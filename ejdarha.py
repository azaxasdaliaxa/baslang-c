import random
import time

def hikaye_goster():
    print("Bir toprakta, uzun zaman önce, ejderhaların yaşadığı bir kara bulunmaktadır.")
    time.sleep(1)
    print("\nEjderhalar insanları sever, ancak onları yemeyi tercih ederler.")
    time.sleep(1)
    print("\nÖnünde iki mağara bulunan büyük bir tepenin önündesin.")
    time.sleep(1)
    print("Bir mağarada dost canlısı bir ejderha yaşamaktadır ve seni içeri alıp hazineyle tanıştırır.")
    time.sleep(2)
    print("Diğer mağarada ise aç ve tehlikeli bir ejderha bulunmakta, seni görür görmez yemek isteyecektir.")
    time.sleep(2)

def mağara_sec():
    mağara = ''
    while mağara != '1' and mağara != '2':
        print("\nHangi mağarayı seçeceksin? (1 veya 2)")
        mağara = input()
    return mağara

def oyunu_oyna(mağara):
    print("\nMağaraya doğru ilerliyorsun...")
    time.sleep(1)
    print("\nKarartı daha da derinleşiyor...")
    time.sleep(1)
    print("\nBüyük bir ejderha beliriyor, ağzını açıyor ve...")
    time.sleep(2)
    
    iyi_mağara = random.randint(1, 2)
    
    if mağara == str(iyi_mağara):
        print("\nSana hazine sunuyor!")
    else:
        print("\nSeni bir nefeste yakıp küle çeviriyor!")

oyun_oynamaya_devam = "evet"
while oyun_oynamaya_devam == "evet":
    hikaye_goster()
    secilen_mağara = mağara_sec()
    oyunu_oyna(secilen_mağara)
    
    print("\nBir kez daha oynamak istiyor musun? (evet ya da hayır)")
    oyun_oynamaya_devam = input().lower()
