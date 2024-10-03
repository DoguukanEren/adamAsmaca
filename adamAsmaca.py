import random

resim = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
--------"""]

kelimeler = ["kiraz","meyve","masa","asansör","kurbağa","prenses","adaptör,sandalye,bilgisayar,ders,insan,hayvan"]

control = True

while control:
    secilenKelime = random.choice(kelimeler)
    kelimeUzunluk = len(secilenKelime)
    bosluk = "_" * kelimeUzunluk
    kalanHak = 6
    tahminler = []

    while kalanHak > 0 and "_" in bosluk:
        print(resim[6 - kalanHak])
        print("Gizli Kelime: ", end="")
        for harf in bosluk:
            print(harf, end=" ")
        print()
        print(f"Kalan Hak: {kalanHak}")
        print("Tahminler: ", end="")
        for harf in tahminler:
            print(harf, end=" ")
        print()

        alinanKelime = input("Lütfen tek harf giriniz: ").lower()

        if len(alinanKelime) != 1 or not alinanKelime.isalpha():
            print("Lütfen sadece bir harf girin.")
            continue

        if alinanKelime in tahminler:
            print("Bu harfi zaten tahmin ettiniz.")
            continue

        tahminler.append(alinanKelime)

        if alinanKelime in secilenKelime:
            yeniBosluk = ""
            for i in range(kelimeUzunluk):
                if secilenKelime[i] == alinanKelime:
                    yeniBosluk += alinanKelime
                else:
                    yeniBosluk += bosluk[i]
            bosluk = yeniBosluk
            print("Doğru tahmin!")
        else:
            kalanHak -= 1
            print("Yanlış tahmin!")

    if "_" not in bosluk:
        print("Kazandınız! Kelime: " + secilenKelime)
    else:
        print(resim[6 - kalanHak])
        print("Kaybettiniz! Kelime: " + secilenKelime)

    tekrar = input("Tekrar oynamak ister misiniz? (e/h): ").lower()
    if tekrar != 'e':
        control = False
    
    
    
    

