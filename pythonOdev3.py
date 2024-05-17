"""
Ödev-1:Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon oluşturulur.

Ödev-2:Faktöriyel adında fonksiyon oluşturulur.
Döngü kullanarak parametre olarak girilen sayının faktöriyeli hesaplanır.Format metodunu kullanılarak ekrana yazdırılır.

Ödev-3:Kişinin fonksiyona doğum yılını vererek kaç yaşında olduğunu hesaplayan bir fonksiyon oluşturun. 

Ödev-4:Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin.(Kişi 65 yaşında ise emekli olur)
Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak yapsın.
Kişi 65 yaşında ya da daha fazlaysa "Emekli oldunuz" yanıtını,
65 yaşından küçükse emekliliğine kaç yıl kaldığını da hesaplayarak
"(isim) emekliliğine (yıl) kaldı." yanıtını versin.
"""

# Ödev-1 #
import math

def daireAlanHesapla(pi,r):
    alan = pi * (r**2)
    return alan

pi = float(input("Pi değerini giriniz: "))
r = float(input("Yarıçap değerini giriniz: "))
alan = daireAlanHesapla(pi, r)

print("Dairenin alanı: ", alan)
print("**********")

# Ödev-2 #
def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n-1)

sayi = int(input("Bir sayi giriniz: "))
sonuc = faktoriyel(sayi)
print("Sonuç: ", sonuc)
print("**********")

# Ödev-3 #
def yas_hesapla(dogum_yili,mevcut_yil):
    yas = mevcut_yil - dogum_yili
    return yas

dogum_yili = int(input("Doğum yılınızı giriniz: "))
mevcut_yil = 2024
yas = yas_hesapla(dogum_yili,mevcut_yil)

print("Yaşınız: ", yas)
print("**********")

# Ödev-4 #
def emeklilik(dogum_yili,isim,mevcut_yil):
    yas = yas_hesapla(dogum_yili,mevcut_yil)
    emeklilik_yasi = 65

    if yas >= emeklilik_yasi:
        print("Emekli oldunuz. ")
    else:
        kalan_yil = emeklilik_yasi - yas
        print("{} emekliliğine {} yıl kaldı. ".format(isim,str(kalan_yil)))

dogum_yili = int(input("Doğum yılınızı giriniz: "))
isim = input("İsminizi giriniz: ")
mevcut_yil = 2024
emeklilik(dogum_yili,isim,mevcut_yil)