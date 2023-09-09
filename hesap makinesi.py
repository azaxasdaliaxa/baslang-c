print("""*************************
    Hesap makinesi programı
    
    İşlemler,
    
    
    
    1.Toplama
    2.Çıkarma
    3.Çarpma
    4.Bölme
    
    
    **************************""")

a= int(input("Birinci sayı:"))
b= int(input("İkinci sayı."))

işlem = input("İşlemleri girin:")

if işlem == "1":
    print ("{}ile{} in toplamı {}dır".format(a,b,a+b))
elif işlem == "2":
    print("{} {} nın farkı {} dır".format(a,b,a-b))
elif işlem == "3":
    print("{} ile {}nın çarpımı {}dır.".format(a,b,a*b))
elif işlem == "4":
    print ("{}ile {} nın bölümü {}dır".format(a,b,a/b))
else :
    print("Hatalı İşlem")
    