import re


class Validace:
    """Třída pro validaci uživatelských vstupů."""

    @staticmethod
    def validuj_text(nazev_pole: str, max_delka: int = 50) -> str:
        """Validuje textový vstup (jméno, příjmení).

        Kontroluje:
        - Neprázdnost
        - Maximální délku
        - Pouze písmena (včetně české diakritiky)

        Args:
            nazev_pole: Název pole pro výpis ("jméno", "příjmení")
            max_delka: Maximální povolená délka (výchozí 50)

        Returns:
            Validní textový vstup
        """
        while True:
            # Načtení vstupu a odstranění mezer ze začátku/konce
            vstup = input(f"Zadejte {nazev_pole}: ").strip()

            # Kontrola prázdnosti
            if not vstup:
                print(f"{nazev_pole.capitalize()} nesmí být prázdné!")
                continue

            # Kontrola maximální délky
            if len(vstup) > max_delka:
                print(f"{nazev_pole.capitalize()} maximálně {max_delka} znaků!")
                continue

            # Kontrola že vstup obsahuje pouze písmena (včetně české diakritiky)
            if not re.match(r'^[a-zA-ZáčďéěíňóřšťúůüýžÁČĎÉĚÍŇÓŘŠŤÚŮÜÝŽ]+$', vstup):
                print(f"{nazev_pole.capitalize()} musí obsahovat pouze písmena!")
                continue

            # Všechny kontroly prošly - vrátíme validní vstup
            return vstup

    @staticmethod
    def validuj_vek() -> int:
        """Validuje věk pojištěného.

        Kontroluje:
        - Zda je vstup číslo
        - Rozsah 1-120 let

        Returns:
            Validní věk jako celé číslo
        """
        while True:
            try:
                # Načtení vstupu a odstranění mezer
                vstup = input("Zadejte věk: ").strip()

                # Pokus o převod na celé číslo - může vyhodit ValueError
                vek = int(vstup)

                # Kontrola rozsahu (1-120 let)
                if vek <= 0 or vek > 120:
                    print("Věk musí být mezi 1-120 lety!")
                    continue

                # Validní věk - vracíme
                return vek

            except ValueError:
                # Zachycení chyby při převodu na int (např. "abc", "25.5")
                print("Věk musí být platné číslo!")
                continue

    @staticmethod
    def validuj_telefon() -> str:
        """Validuje telefonní číslo v českém formátu.

        Povolené formáty:
        - 123456789
        - 123 456 789
        - +420123456789
        - +420 123 456 789

        Returns:
            Validní telefonní číslo
        """
        pattern = r'^(?:\+420)? ?[1-9][0-9]{2} ?[0-9]{3} ?[0-9]{3}$'

        while True:
            # Načtení vstupu
            vstup = input("Zadejte telefon: ").strip()

            # Kontrola prázdnosti
            if not vstup:
                print("Telefon nesmí být prázdný!")
                continue

            # Kontrola proti regex vzoru
            if not re.match(pattern, vstup):
                print("Telefon musí být ve formátu: 123456789 nebo +420 123 456 789")
                continue

            # Validní telefon - vracíme
            return vstup