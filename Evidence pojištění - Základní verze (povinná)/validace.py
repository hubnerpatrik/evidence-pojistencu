import re

class Validace:
    @staticmethod
    def validuj_text(nazev_pole: str, max_delka: int = 50) -> str:
        while True:
            vstup = input(f"Zadejte {nazev_pole}: ").strip()

            if not vstup:
                print(f"{nazev_pole.capitalize()} nesmí být prázdné!")
                continue

            if len(vstup) > max_delka:
                print(f"{nazev_pole.capitalize()} maximálně {max_delka} znaků!")
                continue

            if not re.match(r'^[a-zA-ZáčďéěíňóřšťúůüýžÁČĎÉĚÍŇÓŘŠŤÚŮÜÝŽ]+$', vstup):
                print(f"{nazev_pole.capitalize()} musí obsahovat pouze písmena!")
                continue

            return vstup

    @staticmethod
    def validuj_vek() -> int:
        while True:
            try:
                vstup = input("Zadejte věk: ").strip()
                vek = int(vstup)
                if vek <= 0 or vek > 120:
                    print("Věk musí být mezi 1-120 lety!")
                    continue
                return vek
            except ValueError:
                print("Věk musí být platné číslo!")
                continue

    @staticmethod
    def validuj_telefon() -> str:
        pattern = r'^(?:\+420)? ?[1-9][0-9]{2} ?[0-9]{3} ?[0-9]{3}$'
        while True:
            vstup = input("Zadejte telefon: ").strip()

            if not vstup:
                print("Telefon nesmí být prázdný!")
                continue

            if not re.match(pattern, vstup):
                print("Telefon musí být ve formátu: 123456789 nebo +420 123 456 789")
                continue

            return vstup
