#boolean - none - dictionary


users = {
    "admin": {"password": "1234", "yetki": True},   # Yönetici
    "user": {"password": "abcd", "yetki": False},   # Normal Kullanıcı
    "guest": {"password": "guest", "yetki": None}   # Yetkisiz Kullanıcı
}


def login_screen(name,passw):
    if name in users and users[name]["password"] == passw:
        yetki = users[name]["yetki"]
    
    if yetki is True:
        print("Yönetici olarak giriş yaptınız. Tüm işlemleri yapabilirsiniz.")
    elif yetki is False:
        print("Kullanıcı olarak giriş yaptınız. Yalnızca sınırlı işlemleri yapabilirsiniz.")
    elif yetki is None:
        print("Yetkiniz bulunmamaktadır.")
    else:
        # Geçersiz kullanıcı adı veya şifre
        print("Geçersiz kullanıcı adı veya şifre.")     
    

    
username = input("Username:")
password = input("Password:")
login_screen(username,password)

        