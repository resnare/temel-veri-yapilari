import random
import time

class Kumanda():
    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi = ["Trt"],kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def tv_ac(self):
        if (self.tv_durum == "Açık"):
            print("Televizyon açık....")
        else:
            print("Televizyon açılıyor....")
            self.tv_durum = "Açık"
    def tv_kapat(self):
        if (self.tv_durum == "Kapalı"):
            print("Televizyon kapalı...")
        else:
            print("Televizyon kapanıyor....")
            self.tv_durum = "Kapalı"
    def ses_ayarları(self):
        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Artır: '>'\nÇıkış : çıkış")
            if (cevap == "<"):
                if (self.tv_ses != 0):
                    self.tv_ses -=1
                    print("Ses",self.tv_ses)
            elif (cevap == ">"):
                if (self.tv_ses != 31):
                    self.tv_ses += 1
                    print("Ses",self.tv_ses)
            else:
                print("Ses güncellendi :",self.tv_ses)
                break
    def kanal_ekle(self,kanal_isim):
        print("Kanal ekleniyor.....")
        time.sleep(1)
        self.kanal_listesi.append(kanal_isim)
        print("Kanal eklendi....")
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi(rastgele)
        print("Şu anki kanal:",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv durumu: {}\nTV ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda = Kumanda()
print("""
Televizyon uygulaması

1. Tv aç
2 tv kapat
3 ses yarları
4 kanal ekle
5 kanal sayısı öğrenme
6 rastgele kanala geçme
7 televiyon bilgileri


çıkmak için 'q' ya basın
""")

while True:
    işlem = input("işlem seçin :")

    if (işlem == 'q'):
        print("program kanapıyor.....")
        break
    elif (işlem == "1"):
        kumanda.tv_ac()
    elif (işlem == "2"):
        kumanda.tv_kapat()
    elif (işlem == "3"):
        kumanda.ses_ayarları()
    elif (işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin :")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (işlem == "5"):
        print("Kanal sayısı:",len(kumanda))
    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif (işlem == "7"):
        print(kumanda)
    else:
        print("Geçersiz işlem.....")
