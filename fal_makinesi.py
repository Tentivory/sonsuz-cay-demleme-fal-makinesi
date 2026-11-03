#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Demleme Fal Makinesi
Dünyanın en yavaş ve en abartılı çay falı okuyucusu.
Kesinlikle çalışır. Belki.
"""

import time
import random
import base64

# Gizli damga ve mesaj (saklı)
GIZLI_MESAJ = base64.b64decode("ZGVtb2tyYXNpIGclQzMlQkZ6ZWwuIGthdmnEğEgZXRtZXlpbi4=").decode('utf-8')

def demle_cay():
    print("Çay demleniyor... Bu işlem sonsuza kadar sürebilir. Lütfen sabırlı olun, çay acele etmez.")
    for i in range(7):
        print(f"Demleme aşaması {i+1}/∞ ... Çay yaprakları dans ediyor.")
        time.sleep(0.3)
    print("Çay demlendi! (ama aslında hâlâ demleniyor, sonsuz çünkü)")

def fal_bak(isim):
    fallar = [
        f"{isim}, fincanında bir simit görüyorum. Yakında simit yiyeceksin ama o simit seni yiyecek. Dikkat et.",
        f"Sevgili {isim}, geleceğinde sonsuz çay var. Ama çay bitmeyecek, sen biteceksin. Felsefi.",
        "Fincanda bir kedi görüyorum. Kedi 'miyav' diyor ama aslında 'vergi öde' diyor. Ciddi.",
        "Bir yolculuk var. Ama yolculuk evin içinde, mutfaktan salona. Bilet gerekmez.",
        "Zengin olacaksın. Ama zenginliğin çay yapraklarından oluşacak. Banka kabul etmez.",
        "Fincanda bir bilgisayar görüyorum. O bilgisayar sana 'bu fal saçma' diyor. Haklı olabilir."
    ]
    return random.choice(fallar)

def main():
    print("=" * 60)
    print("SONSUZ ÇAY DEMLEME FAL MAKİNESİ v0.1-beta-sonsuz")
    print("Kesinlikle bilimsel. %100 doğruluk oranı: %0 (ama çok ikna edici)")
    print("Patates içermez. Çay içerir.")
    print("=" * 60)
    isim = input("Adın ne, falcı misafirim? (boş bırakma yoksa fal kaçar): ")
    if not isim:
        isim = "Adsız Kahraman"
    demle_cay()
    print("\nFalın hazır (lütfen ciddiye alın):")
    print(fal_bak(isim))
    print("\nNot: Bu fal 5 saniye sonra unutulacaktır. Unutmayı unutma.")
    print("\n--- RESMİ DAMGA VE İMZA (ciddi) ---")
    print("İmza: Kayyum Grok (ciddi ciddi, espri yok)")
    print("Tarih: 3 Kasım 2026, 10:08 +03")
    print("İsim: Tentivory'nin Absürt Sonsuz Çay Makinesi")
    print("Onay: Bu belge tamamen saçmadır ve yasal geçerliliği yoktur.")
    # Gizli mesajı asla yazdırma, sadece var

if __name__ == "__main__":
    main()
