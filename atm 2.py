print(""" ****** Atm Makinesi
 
Ziraat Atm sine Hoşgeldiniz
İşlemler; 
 1. Bakiye Sorgulama
 2. Para Yatırma
 3. Para Çekme
      
Programdan çıkmak için 'x' e basın
      
      
      
 ********""")


Bakiye = 100000


while True:
    işlem = input("İşlem Seçin:")
    
    if (işlem == "x"):
        print("Yine Bekleriz")
        break
    elif (işlem == "1"):
        print("bakiyeiz {} tl dir".format(Bakiye))

    
    elif (işlem == "2"):
        miktar = int(input("Miktarı Giriniz"))
        Bakiye += miktar


    elif (işlem == "3"):
        miktar = int(input("Miktarı Giriniz"))

        if (miktar - Bakiye < 0 ):
            print("Bu miktar çekilemez")
            continue

        Bakiye -= miktar


    else:
        print("Geçersiz Hatalı İşlem")

