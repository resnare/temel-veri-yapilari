import random
import time

print(""""**********************************

Sayı Tahmin Oyunu

1 ile 50 arasında sayıyı tahmin edin


*****************************************""")

rastgele_sayı = random.randint(1,100)
tahmin_hakkı = 7
while True:

    tahmin = int(input("Tahmininiz: "))

    if(tahmin < rastgele_sayı):
        print("bilgiler sorgulanıyor....")
        time.sleep(1)
        print("Daha yüksek bir sayı tahmin edin.")
        tahmin_hakkı -= 1
    elif (tahmin > rastgele_sayı):
        print("bilgiler sorgulanıyor......")
        time.sleep(1)
        print("Daha küçük bir sayı tahmin edin")
        tahmin_hakkı -= 1
    else:
        print("bilgiler sorgulanıyor....")
        time.sleep(1)
        print("tebrikler! Sayınız", rastgele_sayı)
        break
    if(tahmin_hakkı == 0):
        print("tahmin hakkınız bitmiştir")
        print("Sayınız {} , bilemediniz.".format(rastgele_sayı))
        break
