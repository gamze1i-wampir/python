print("SAYI SAYMA OYUNUNA HOŞGELDİNİZ")
print("------------------------------")
print("harf yazmayın hata verir!!!!!!!")
import random
tahminisayi=random.randint(1, 99)
yanlış_tahmin = 0
while True: 
    yanlış_tahmin+=1
    sayi=int(input("1 ile 99 arasında değer girin (404 yazarak Çıkış yap):"))
    if(sayi==404):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < tahminisayi:
        print("Daha Yüksek Bir Sayı Girin....")
        continue
    elif sayi > tahminisayi:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Tahmin edilen sayı:  {0}".format(tahminisayi))
        print("yanlış tahmin sayınız: {0}".format(yanlış_tahmin))
        print("TEBRİKLER OYUNU KAZANDINIZ")
        print("YENİDEN BAŞLAYIN")
        


  
