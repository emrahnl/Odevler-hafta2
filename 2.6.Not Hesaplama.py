vize1 =int(input("1.vize notunuz: "))
vize2 =int(input("2.vize notunuz: "))
final =int(input("final notunuz: "))
yilsonu_notu=vize1*0.3 + vize2*0.3 + final*0.4
print("yil sonu notunuz:",yilsonu_notu)

if yilsonu_notu >= 90:
    print("Notunuz: AA")
elif yilsonu_notu >=85:
    print("Notunuz:BA")
elif yilsonu_notu >= 80:
    print("Notunuz:BB")
elif yilsonu_notu >= 75:
    print("Notunuz:CB")
elif yilsonu_notu >= 70:
    print("Notunuz:CC")
elif yilsonu_notu >= 65:
    print("Notunuz:DC")
elif yilsonu_notu >= 60:
    print("Notunuz:DD")
elif yilsonu_notu >= 55:
    print("Notunuz:FD")
elif yilsonu_notu <55:
    print("Notunuz:FF")
    
    


