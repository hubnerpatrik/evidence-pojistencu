"""Správa seznamu pojištěných v paměti."""


class EvidencePojistencu:
    """Kolekce pojištěných uložená v paměti."""

    def __init__(self):
        """Inicializuje prázdný seznam pojištěných."""
        self.seznam = []

    def evidovat_pojistence(self, pojisteny):
        """Přidá nového pojištěného do evidence.

        Args:
            pojisteny (Pojisteny): Objekt pojištěného
        """
        self.seznam.append(pojisteny)

    def vypis_vsechny(self):
        """Vrátí seznam všech pojištěných.

        Returns:
            list: Seznam objektů Pojisteny
        """
        return self.seznam

    def vyhledej(self, jmeno, prijmeni):
        """Vyhledá pojištěné podle jména a příjmení (case-insensitive).

        Args:
            jmeno (str): Hledané jméno
            prijmeni (str): Hledané příjmení

        Returns:
            list: Seznam nalezených pojištěných
        """
        nalezeni = []
        for pojisteny in self.seznam:
            if (pojisteny.jmeno.lower() == jmeno.lower() and
                    pojisteny.prijmeni.lower() == prijmeni.lower()):
                nalezeni.append(pojisteny)
        return nalezeni
