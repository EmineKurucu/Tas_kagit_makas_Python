# Python ile taş kağı makas oyunu programlıyoruz
import random
import time

#intordution
def introduction():

    # programı tanıtıyoruz
    print("Bu bir tas-kagit-makas oyunudur."
          "Iki kullaniciya taş - kagit ya da makas değeri atanir. "
          "Tas makasi yener "
          "Makas kagidi yener ")

    print("3 defa karsi tarafi yenen oyunu kazanir.")

def main():
    introduction()

    # liste oluşturuyoruz
    olasilikaklar = ["tas" , "kagit" , "makas"]

    # başlangıçtaki oyuncu skorları
    skor_oyuncu1 = 0
    skor_oyuncu2 = 0


    while skor_oyuncu1 < 3 and skor_oyuncu2 < 3:

        input("1. oyuncu icin secim yapmak istiyorsaniz ENTER'a basin ")
        oyuncu1 = random.choice(olasilikaklar)
        input("2. oyuncu icin secim yapmak istiyorsaniz ENTER'a basin ")
        oyuncu2 = random.choice(olasilikaklar)

        print(f"Oyuncu1 = {oyuncu1}")
        print(f"Oyuncu2 = {oyuncu2}")



        if oyuncu1 == oyuncu2:
            print("Secimler ayni puan yok .")
            print()
            continue

        elif (oyuncu1 == "tas" and oyuncu2 == "makas") or \
             (oyuncu1 == "kagit" and oyuncu2 == "tas") or \
             (oyuncu1 == "makas" and oyuncu2 == "kagit"):
            skor_oyuncu1 += 1
            print("Oyuncu1 1 puan kazandi")
            print()
        else:
            skor_oyuncu2 += 1
            print("Oyuncu2 1 puan kazandi")
            print()

        print(f"Puan durumu :"
              f"Oyuncu1 = {skor_oyuncu1} "
              f"Oyuncu2 = {skor_oyuncu2}")
        print()


    if skor_oyuncu1 == 3:
        print("Kazanan 1. oyuncu ")
        time.sleep(10)
    if skor_oyuncu2 == 3:
        print("Kazanan 2. oyuncu ")
        time.sleep(10)

if __name__ == '__main__':
    main()



