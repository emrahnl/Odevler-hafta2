geometrik_sekil=input("Kullanmak istediginiz sekil ucgen midir dortgen mi")


if geometrik_sekil=="ucgen":
        kenar1 = (int(input("1.kenar: ")))
        kenar2 = (int(input("2.kenar: ")))
        kenar3 = (int(input("3.kenar: ")))
        if kenar1 == kenar2 == kenar3:
            print (" seklimiz eskenar ucgendir ")
        elif kenar1 == kenar2 and kenar1 != kenar3:
            print("seklimiz ikizkenar ucgendir")
        elif kenar1 != kenar2 != kenar3:
            print("seklimiz ucgendir'.")
        else:
            print("seklimiz ucgen degilidir")

elif geometrik_sekil== "dortgen":
        kenar1 = (int(input("1.kenar: ")))
        kenar2 = (int(input("2.kenar: ")))
        kenar3 = (int(input("3.kenar: ")))
        kenar4 = (int(input("4.kenar: ")))
        if kenar1 == kenar2 and kenar3==kenar4:
            print("seklimiz karedir")
        elif kenar1 == kenar3 and kenar2==kenar4:
            print("seklimiz dikdortgendir")
        else:
            print("seklimiz siradan dortgendir")

else:
            print("bu bir sekil degildir")

    
