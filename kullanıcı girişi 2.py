print("""
*******************************
      Kullanıcı Girişi
*******************************
""")
      
sys_kullanıcı_adı = "Talha"
sys_parola = "123456A"

giriş_hakkı = 3 

while True:
    kullanıcı_adı = input("Kullanıcı Adı :")
    parola = input("Parola:")
    if(kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Kullanıcı adı hatalı")
        giriş_hakkı -= 1 
    elif ( kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("Parola hatalı")
        giriş_hakkı -= 1
    elif (kullanıcı_adı!= sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı adı ve parola yanlış")
        giriş_hakkı -= 1 

    else:
        print("Sisteme başarıyla giriş yapıldı")
        break
    if(giriş_hakkı == 0):
        print("Giriş hakkınız bitti")
        break
