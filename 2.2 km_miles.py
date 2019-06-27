birim=input("km mi miles mi kullanmak istersiniz?")
mesafe=float(input("ne kadar mesafe aldınız?"))
if birim=="km":
    sonuc=mesafe*0.62
    print(sonuc, "miles")
elif birim=="miles":
    sonuc=mesafe/0.62
    print(sonuc,"km")

else:
    print("yanlış birim girdiniz")
    
