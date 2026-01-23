from pojisteny import Pojisteny
from evidence import EvidencePojistencu
from validace import Validace

class UI:
    def __init__(self):
        self.evidence = EvidencePojistencu()
        self.validace = Validace()

    def zobraz_menu(self):
        print("\n" + "=" * 40)
        print("EVIDENCE POJIŠTĚNÝCH")
        print("=" * 40)
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")
        print("=" * 40)

    def vytvor_pojistence(self):
        print("\n--- Nový pojištěný ---")
        jmeno = self.validace.validuj_text("jméno")
        prijmeni = self.validace.validuj_text("příjmení")
        vek = self.validace.validuj_vek()
        telefon = self.validace.validuj_telefon()

        return Pojisteny(jmeno, prijmeni, vek, telefon)

    def vypis_pojistence(self, seznam):
        if not seznam:
            print("\nŽádní pojištění nebyli zadáni.")
            return

        print("\n" + "=" * 40)
        print("SEZNAM POJIŠTĚNÝCH:")
        print("=" * 40)
        for i, pojisteny in enumerate(seznam, 1):
            print(f"{i}. {pojisteny}")
        print("=" * 40)

    def spust(self):
        while True:
            self.zobraz_menu()
            volba = input("\nVyberte možnost (1-4): ").strip()

            match volba:
                case "1":
                    pojisteny = self.vytvor_pojistence()
                    self.evidence.evidovat_pojistence(pojisteny)
                    print("\nPojištěný byl úspěšně přidán.")

                case "2":
                    self.vypis_pojistence(self.evidence.vypis_vsechny())

                case "3":
                    print("\n--- Vyhledávání ---")
                    jmeno = input("Zadejte jméno: ").strip()
                    prijmeni = input("Zadejte příjmení: ").strip()
                    nalezeni = self.evidence.vyhledej(jmeno, prijmeni)
                    self.vypis_pojistence(nalezeni)

                case "4":
                    print("\nKonec aplikace.")
                    break

                case _:
                    print("\nNeplatná volba! Zvolte číslo 1-4.")
