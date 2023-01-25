print(""" GİRİŞ EKRANI""")
sys_username="Mehmet"
sys_password="123456"
kullanici_adi=input("Kullanıcı adınızı girin:")
sifre=input("Şifrenizi girin:")
if(kullanici_adi==sys_username)and(sifre!=sys_password):
    print("Hatalı şifre girdiniz!")
elif(kullanici_adi!=sys_username)and(sifre==sys_password):
    print("Hatalı kullanıcı adı!")
elif(kullanici_adi!=sys_username)and(sifre!=sys_password):
    print("Hatalı kullanıcı adı ve şifre girdinz")
else:
    print("Giriş Başarılı")