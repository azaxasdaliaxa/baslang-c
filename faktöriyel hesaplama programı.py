print("""
Faktöriyel Hesaplama Programı
Çıkmak için 'Z' basın
      
      
""")
      
while True:
    sayı = input("Sayı:")
    if(sayı == "Z"):
        print("Program Kapatılıyor")
        break
    else:
        sayı = int(sayı)
        faktöriyel = 1
        for i in range (2 , sayı+1):
            faktöriyel *= i 
            print("Faktöriyel", faktöriyel)
            