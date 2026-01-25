from pojisteny import Pojisteny
from evidence import EvidencePojistencu
from validace import Validace


class UI:
    """Uživatelské rozhraní aplikace - menu a komunikace s uživatelem."""

    def __init__(self):
        """Inicializace UI - vytvoření evidence a validace."""
        # Evidence pro ukládání pojištěných v paměti
        self.evidence = EvidencePojistencu()
        # Instance validace pro kontrolu vstupů
        self.validace = Validace()

    def zobraz_menu(self):
        """Zobrazí hlavní menu aplikace."""
        print("\n" + "=" * 40)
        print("EVIDENCE POJIŠTĚNÝCH")
        print("=" * 40)
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")
        print("=" * 40)

    def vytvor_pojistence(self):
        """Načte a zvaliduje data nového pojištěného.

        Postupně načte jméno, příjmení, věk a telefon.
        Každý vstup je validován před pokračováním.

        Returns:
            Nový objekt Pojisteny se zvalidovanými daty
        """
        print("\n--- Nový pojištěný ---")

        # Validace textových polí - pouze písmena, max 50 znaků
        jmeno = self.validace.validuj_text("jméno")
        prijmeni = self.validace.validuj_text("příjmení")

        # Validace věku - číslo v rozsahu 1-120
        vek = self.validace.validuj_vek()

        # Validace telefonu - český formát
        telefon = self.validace.validuj_telefon()

        # Vytvoření a vrácení nového objektu pojištěného
        return Pojisteny(jmeno, prijmeni, vek, telefon)

    def vypis_pojistence(self, seznam):
        """Vypíše seznam pojištěných.

        Args:
            seznam: List objektů Pojisteny k vypsání
        """
        # Kontrola prázdného seznamu
        if not seznam:
            print("\nŽádní pojištění nebyli zadáni.")
            return

        # Hlavička výpisu
        print("\n" + "=" * 40)
        print("SEZNAM POJIŠTĚNÝCH:")
        print("=" * 40)

        # Očíslovaný výpis všech pojištěných
        # enumerate(seznam, 1) - čísluje od 1
        for i, pojisteny in enumerate(seznam, 1):
            # Automaticky zavolá pojisteny.__str__()
            print(f"{i}. {pojisteny}")

        # Patička výpisu
        print("=" * 40)

    def spust(self):
        """Hlavní smyčka aplikace - zobrazuje menu a zpracovává volby."""
        # Nekonečný cyklus - běží dokud uživatel nezvolí konec (volba 4)
        while True:
            # Zobrazení menu
            self.zobraz_menu()

            # Načtení volby uživatele (strip odstraní mezery)
            volba = input("\nVyberte možnost (1-4): ").strip()

            # Match-case - zpracování jednotlivých voleb
            match volba:
                case "1":
                    # PŘIDÁNÍ NOVÉHO POJIŠTĚNÉHO
                    # 1. Načtení a validace dat
                    pojisteny = self.vytvor_pojistence()
                    # 2. Uložení do evidence
                    self.evidence.evidovat_pojistence(pojisteny)
                    # 3. Potvrzení
                    print("\nPojištěný byl úspěšně přidán.")

                case "2":
                    # VÝPIS VŠECH POJIŠTĚNÝCH
                    # Získání seznamu z evidence a jeho výpis
                    self.vypis_pojistence(self.evidence.vypis_vsechny())

                case "3":
                    # VYHLEDÁVÁNÍ POJIŠTĚNÉHO
                    print("\n--- Vyhledávání ---")

                    # Načtení jména a příjmení (bez validace - vyhledávání je tolerantnější)
                    jmeno = input("Zadejte jméno: ").strip()
                    prijmeni = input("Zadejte příjmení: ").strip()

                    # Vyhledání v evidenci (case-insensitive)
                    nalezeni = self.evidence.vyhledej(jmeno, prijmeni)

                    # Výpis výsledků (může být prázdný seznam)
                    self.vypis_pojistence(nalezeni)

                case "4":
                    # KONEC APLIKACE
                    print("\nKonec aplikace.")
                    # Break ukončí while True cyklus
                    break

                case _:
                    # NEPLATNÁ VOLBA - vše ostatní mimo 1-4
                    print("\nNeplatná volba! Zvolte číslo 1-4.")