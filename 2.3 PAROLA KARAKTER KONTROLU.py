username=input("3-18 karaker arasinda bir username giriniz: ")
if len(username)>18:
    print("username en az fazla 18 karakter olmalı")
elif len(username)<3:
    print("username en az 3 karakter olmalı")
else:
    rakamlar=("0", "1" , "2", "3", "4", "5", "6", "7", "8", "9")
    for harf in username:
       if harf in rakamlar:
         print("username'de rakam kullanamazsınız")
         break
    
    password=input("6-12 karakter aralığında bir şifre giriniz:")
    p=len(password)
    if p>=6 and p<12:
        print("başarılı kayıt")

    elif p>12:
        print("şifreniz en az fazla 12 karakter olmalı")
    elif p<6:
        print("şifreniz en az 6 karakter olmalı")

    

print(username,password)
