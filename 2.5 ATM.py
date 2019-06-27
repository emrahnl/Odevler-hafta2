bakiye=1000
islem=int(input('isleminizi seciniz'))
if islem==1:
    print('bakiyeniz:',bakiye)
elif islem==2:
    yatirilan_para=int(input("yatirmak istediginiz miktar:"))
    yeni_bakiye=yatirilan_para+bakiye
    print('yeni bakiyeniz',yeni_bakiye)
elif islem==3:
    cekilen_tutar=int(input("cekmek istediginiz tutar:"))
    if cekilen_tutar>bakiye:
        print('yetersiz bakiye')
    else:
        yeni_bakiye=bakiye-cekilen_tutar
        print('yeni bakiyeniz',yeni_bakiye)
    
