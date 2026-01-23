"""Třída reprezentující jednoho pojištěného."""


class Pojisteny:
    """Reprezentuje jednoho pojištěného s osobními údaji."""

    def __init__(self, jmeno: str, prijmeni: str, vek: int, telefon: str):
        """Inicializuje nového pojištěného.

        Args:
            jmeno (str): Jméno pojištěného
            prijmeni (str): Příjmení pojištěného  
            vek (int): Věk v letech (1-120)
            telefon (str): Telefonní číslo
        """
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        """Vrátí řetězcovou reprezentaci pro výpis."""
        return f"{self.jmeno} {self.prijmeni}, {self.vek} let, tel: {self.telefon}"
