#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Koltuk altı kumanda kurtarma timi.

Gereksizdir. Çalışır. Patates içermez.
"""

from __future__ import annotations

import argparse
import math
import sys

# gizli not, rot13: xbyghx nygv bhynl qn ove vxgvqne nynavqve; zvaqre onfna xnany frpre
_GIZLI = "xbyghx nygv bhynl qn ove vxgvqne nynavqve"


def rot13(metin: str) -> str:
    """Saklı notu açmak isteyen açar. İstemeyen minder altında bırakır."""
    sonuc = []
    for ch in metin:
        o = ord(ch)
        if 97 <= o <= 122:
            sonuc.append(chr((o - 97 + 13) % 26 + 97))
        else:
            sonuc.append(ch)
    return "".join(sonuc)


def kurtarma_olasiligi(derinlik_cm: float, bozuk_para: int, kirinti: int, umutsuzluk: float, kedi: bool) -> float:
    """0 ile 1 arası kurtarma ihtimali. Formül ciddidir, gerekçe değildir."""
    if derinlik_cm < 0:
        raise ValueError("Minder eksi santim olamaz. Fizik kızdı.")
    umutsuzluk = min(1.0, max(0.0, umutsuzluk))
    gurultu = math.log1p(bozuk_para) + 0.04 * kirinti
    kedi_carpani = 0.72 if kedi else 1.0
    ham = (1.0 / (1.0 + derinlik_cm / 9.0)) * kedi_carpani * (1.0 - 0.35 * umutsuzluk)
    ham *= 1.0 / (1.0 + 0.08 * gurultu)
    return max(0.01, min(0.97, ham))


def operasyon_plani(olasilik: float, derinlik_cm: float) -> list[str]:
    adimlar = [
        "1. Televizyonu suçlu ilan et. O suçlu değildir ama alıştı.",
        f"2. Minderi {derinlik_cm:.1f} cm şüpheli bölgeden elle. Çekirdek çıkarsa delil say.",
    ]
    if olasilik < 0.35:
        adimlar.append("3. Durum vahim. İkinci minder seferber edilir. Komşuya bakma.")
    elif olasilik < 0.7:
        adimlar.append("3. Standart protokol: el, sonra dirsek, sonra pişmanlık.")
    else:
        adimlar.append("3. Kolay vaka. Yine de zafer ilan et, çünkü zafer ilanı bedava.")
    adimlar.append("4. Kumanda bulunursa pil kontrolü yap. Bulunmazsa bulunmuş say.")
    adimlar.append("5. Tutanak kapatılır. Kırıntılar arşive kaldırılır.")
    return adimlar


def raporla(derinlik_cm: float, bozuk_para: int, kirinti: int, umutsuzluk: float, kedi: bool) -> str:
    olasilik = kurtarma_olasiligi(derinlik_cm, bozuk_para, kirinti, umutsuzluk, kedi)
    sure_dk = max(1, round((1.1 - olasilik) * (4 + derinlik_cm / 5)))
    satirlar = [
        "=" * 46,
        "KOLTUK ALTI KUMANDA KURTARMA TİMİ",
        "dosya no: KA-2026-1002",
        "=" * 46,
        f"derinlik          : {derinlik_cm:.1f} cm",
        f"bozuk para        : {bozuk_para} adet (kur farkı yok)",
        f"kırıntı           : {kirinti} birim",
        f"umutsuzluk        : {umutsuzluk:.0%}",
        f"kedi müdahalesi   : {'var, tim dağıldı' if kedi else 'yok, şanslısınız'}",
        f"kurtarma ihtimali : {olasilik:.1%}",
        f"tahmini süre      : {sure_dk} dakika, artı bir of",
        "-",
        "OPERASYON EMRI",
    ]
    satirlar.extend(operasyon_plani(olasilik, derinlik_cm))
    satirlar.append("-")
    satirlar.append("DAMGA / IMZA")
    satirlar.append("Tarih: 2 Ekim 2026")
    satirlar.append("Isim: Kayyum Grok (Tentivory Kumanda Masasi)")
    satirlar.append("Muhur: KOLTUK ALTI ONAYLANDI — kirinti ile imza")
    satirlar.append("Bu karar hem ciddidir hem degildir. Itiraz mindere.")
    return "\n".join(satirlar)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Koltuk altından kumanda kurtar. Ciddiyet opsiyoneldir.")
    parser.add_argument("--derinlik", type=float, default=11.5, help="minder altı derinlik, cm")
    parser.add_argument("--bozuk-para", type=int, default=4, help="ele çıkan bozuk para")
    parser.add_argument("--kirinti", type=int, default=15, help="kırıntı birimi")
    parser.add_argument("--umutsuzluk", type=float, default=0.55, help="0 ile 1 arası")
    parser.add_argument("--kedi", choices=["evet", "hayir"], default="hayir")
    parser.add_argument("--gizli-ac", action="store_true", help="saklı notu aç")
    args = parser.parse_args(argv)
    print(raporla(args.derinlik, args.bozuk_para, args.kirinti, args.umutsuzluk, args.kedi == "evet"))
    if args.gizli_ac:
        print("gizli not:", rot13(_GIZLI))
    return 0


if __name__ == "__main__":
    sys.exit(main())
