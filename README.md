# Evidence pojištěných
## Popis

Aplikace umožňuje evidovat pojištěné osoby, vyhledávat je podle jména a příjmení a vypsat celý seznam. Všechna data jsou validována a uložena v paměti během běhu programu.

<img width="314" height="208" alt="obrazek" src="https://github.com/user-attachments/assets/a5543351-820c-46b2-bfe3-772cf46d145a" />
<img width="358" height="311" alt="obrazek" src="https://github.com/user-attachments/assets/1155e9ea-1e61-4923-b39d-f14619288507" />




## Funkce

- **Přidání nového pojištěného** - s validací všech vstupních údajů
- **Výpis všech pojištěných** - přehledný číslovaný seznam
- **Vyhledávání** - podle jména a příjmení (nerozlišuje velikost písmen)
- **Validace vstupů** - kontrola formátu a platnosti všech údajů

## Technologie

- **Python 3.10+** (využívá match-case konstrukci)
- **Standardní knihovny**: `re` (regulární výrazy)

## Instalace

1. Naklonuj repozitář:
```bash
git clone https://github.com/hubnerpatrik/evidence-pojistencu.git
cd evidence-pojistencu
```

2. Ujisti se, že máš Python 3.10 nebo vyšší:
```bash
python --version
```

## Spuštění

```bash
python main.py
```

## Použití

Po spuštění aplikace se zobrazí hlavní menu:

```
========================================
EVIDENCE POJIŠTĚNÝCH
========================================
1 - Přidat nového pojištěného
2 - Vypsat všechny pojištěné
3 - Vyhledat pojištěného
4 - Konec
========================================
```

### 1. Přidání nového pojištěného

Zadej volbu `1` a postupně vyplň:
- **Jméno** - pouze písmena, max. 50 znaků
- **Příjmení** - pouze písmena, max. 50 znaků
- **Věk** - číslo v rozsahu 1-120
- **Telefon** - formát `123456789` nebo `+420 123 456 789`

### 2. Výpis všech pojištěných

Zadej volbu `2` pro zobrazení kompletního seznamu všech evidovaných pojištěných.

### 3. Vyhledávání pojištěného

Zadej volbu `3` a vyplň jméno a příjmení (nerozlišuje velikost písmen).

### 4. Ukončení aplikace

Zadej volbu `4` pro bezpečné ukončení programu.

### Popis souborů

- **main.py** - Spouští aplikaci a inicializuje uživatelské rozhraní
- **pojisteny.py** - Obsahuje třídu `Pojisteny` reprezentující jednu osobu
- **evidence.py** - Třída `EvidencePojistencu` spravuje kolekci pojištěných v paměti
- **validace.py** - Třída `Validace` zajišťuje kontrolu vstupních dat
- **ui.py** - Třída `UI` obsluhuje komunikaci s uživatelem

## Architektura

Aplikace dodržuje principy **čistého kódu** a **separation of concerns**:

- **Model** (`Pojisteny`) - datová vrstva
- **Repository** (`EvidencePojistencu`) - správa dat
- **View** (`UI`) - prezentační vrstva
- **Validation** (`Validace`) - validační vrstva

Každá třída má **jednu zodpovědnost** (Single Responsibility Principle).

## Validace

Aplikace kontroluje:

### Jméno a příjmení
- Nesmí být prázdné
- Maximálně 50 znaků
- Pouze písmena včetně české diakritiky
- Žádná čísla ani speciální znaky

### Věk
- Musí být celé číslo
- Rozsah 1-120 let

### Telefon
- Nesmí být prázdný
- Povolené formáty:
  - `123456789`
  - `123 456 789`
  - `+420123456789`
  - `+420 123 456 789`

## Autor

**Patrik Hübner**
- GitHub: [@hubnerpatrik ](https://github.com/hubnerpatrik)
- Email: hubnerpatrik00@gmail.com
