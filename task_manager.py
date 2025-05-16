# Toto je program pro správu úkolů. program umožňuje přidávat, zobrazovat a odstraňovat úkoly.

# Seznam úkolů
ukoly = []

# Počet úkolů
n = 0

# Funkce

def hlavni_menu():                      # Funkce hlavní menu poskytuje možnosti pro přidání, zobrazení a odstranění úkolu.
    print("\nSprávce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")

def vyber_moznosti():                   # Funkce vyzve uživatele k výběru možností. Uživatelský vstup.
    return input("Vyberte možnost (1-4): ")

def zobrazit_ukoly():                   # Funkce zobrazí všechny úkoly v sezanmu.
    print("\nSeznam úkolů:")
    if ukoly:
        for i, ukol in enumerate(ukoly, start=1):
            print(f"{i}. {ukol[f"název"]} - {ukol[f"popis"]}")
    else:
        print("\nSeznam úkolů je prázdný.")

def pridat_ukol():                      # Funkce umožní uživateli zadat název a popis nového úkolu a uložit jej do seznamu úkolů.
    global n
    
    nazev = False
    while nazev == False:
        nazev_ukolu = input("\nZadejte název úkolu: ")      # Uživatelský vstup.
        if len(nazev_ukolu) == 0:                           # Pokud uživatel nezadá název úkolu, program ho upozorní a nechá volbu opakovat.
            print("\nZadal jste prázdný vstup! Zadejte název úkolu znovu.")
        else:
            nazev = True

    popis = False
    while popis == False:
        popis_ukolu = input("Zadejte popis úkolu: ")        # Uživatelský vstup.
        if len(popis_ukolu) == 0:                           # Pokud uživatel nezadá popis úkolu, program ho upozorní a nechá volbu opakovat.
            print("\nZadal jste prázdný vstup! Zadejte popis úkolu znovu.")
        else:
            popis = True
        
    ukoly.append({f"název": nazev_ukolu, f"popis": popis_ukolu})    # Přidání nového úkolu do seznamu úkolů.
    
    print(f"Úkol '{nazev_ukolu}' byl přidán.")                      # Potvrzovací hláška, že úkol byl přidán.
    #print(f"\n{ukoly}")
    #print(f"\nAktuální počet úkolů v seznamu: {len(ukoly)}")

    n = n + 1               # Aktualizuje se počet úkolů v seznamu úkolů.

def odstranit_ukol():                   # Funkce odstranit úkol. Umožní uživateli zadat číslo úkolu, který chce odstranit a tento úkol odstraní.
    global n
    
    if ukoly:
        podminka = False

        while podminka == False:
            zobrazit_ukoly()
            try:
                odstranit = int(input(f"\nZadejte číslo úkolu, který chcete odstranit: "))      # Uživatelský vstup.
            except ValueError:                                                                  # Podmínka při zadání neplatného vstupu.
                print("Neplatná volba! Opakujte volbu znovu.")
            else:    
                if odstranit >= 0 and odstranit <= n:
                    if odstranit == 0:
                        print("Návrat do hlavního menu.")
                    else:
                        odstraneny_ukol = ukoly.pop(odstranit-1)                                # Odstranění úkolu podle indexu.
                        print(f"Úkol '{odstraneny_ukol['název']}' byl odstraněn.")
                    podminka = True
                elif odstranit > n:
                    print(f"Úkol číslo '{odstranit}' neexistuje. Opakujte volbu znovu.")        # Podmínka při zadání neplatného vstupu.
    else:
        print("\nSeznam úkolů je prázdný.")

# Hlavní smyčka

while True:
    hlavni_menu()
    volba = vyber_moznosti()
    if volba == "1":
        pridat_ukol()
    elif volba == "2":
        zobrazit_ukoly()
    elif volba == "3":
        odstranit_ukol()
    elif volba == "4":
        print("\nKonec programu.\n")
        break
    else:
        print("\nNeplatná volba! Opakujte volbu znovu.")
