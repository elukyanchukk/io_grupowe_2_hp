import time
import random
import csv
from datetime import datetime
import os

def wyslij_sowe (adresat, tresc):

    print(f"Wysyłanie sowy do: {adresat}, o treści: {tresc}")
    time.sleep(1)

    if random.random()<0.85:
        print("Sowa została wysłana pomyślnie!")
        return True
    else:
        print("Niestety wystąpił błąd podczas wysyłania sowy")
        return False
    

def licz_sume(fundusz):
    # Przeliczenie knutów na sykle
    knuty = sum(fundusz.get("knut"))
    knut_sykl = knuty // 21
    knuty = knuty % 21

    # Dodanie knutów do sykli i przeliczenie sykli na galeony 
    sykle = sum(fundusz.get("sykl")) + knut_sykl
    sykl_galeon = sykle // 17
    sykle = sykle % 17

    # Dodanie sykli do galeonów
    galeony = sum(fundusz.get("galeon")) + sykl_galeon

    return {
        "galeon": galeony,
        "sykl": sykle,
        "knut": knuty
    }


def wybierz_sowe_zwroc_koszt(potw_odbioru, odleglosc, typ, specjalna):

    koszt_dict = {'galeon': 0, 'sykl': 0, 'knut': 0}

    if typ == 'list':
        if odleglosc == 'lokalna':
            koszt_dict['knut'] = 2
        elif odleglosc == 'krajowa':
            koszt_dict['knut'] = 12
        elif odleglosc == 'dalekobiezna':
            koszt_dict['knut'] = 20

    elif typ == 'paczka':
        if odleglosc == 'lokalna':
            koszt_dict['knut'] = 7
        elif odleglosc == 'krajowa':
            koszt_dict['knut'] = 2
            koszt_dict['sykl'] = 1
        elif odleglosc == 'dalekobiezna':
            koszt_dict['knut'] = 1
            koszt_dict['sykl'] = 2

    if potw_odbioru:
        koszt_dict['knut'] = koszt_dict.get('knut') + 7

    if specjalna == 'wyjec':
        koszt_dict['knut'] = koszt_dict.get('knut') + 4
    elif specjalna == 'list gonczy':
        koszt_dict['sykl'] = koszt_dict.get('sykl') + 1

    return koszt_dict


def waluta_dict_na_str(fundusz):
    for k, v in fundusz.items():
        if k in fundusz and v != 0:
            fundusz[k] = v
    cena = ""

    if fundusz['galeon'] != 0:
        cena += str(fundusz['galeon']) + ' galeon '
    if fundusz['sykl'] != 0:
        cena += str(fundusz['sykl']) + ' sykl '
    if fundusz['knut'] != 0:
        cena += str(fundusz['knut']) + ' knut'

    return cena


def waluta_str_na_dict(waluta_str):
    
    elements = waluta_str.split()
    
   
    currency_dict = {'galeony': 0, 'sykle': 0, 'knuty': 0}
    
    
    for i in range(0, len(elements), 2):
        value = int(elements[i])  
        unit = elements[i + 1]    
        
        if unit.startswith('g'):
            currency_dict['galeony'] = value
        elif unit.startswith('s'):
            currency_dict['sykle'] = value
        elif unit.startswith('k'):
            currency_dict['knuty'] = value
    
    return currency_dict


def nadaj_sowe(adresat, tresc, potw_odbioru, odleglosc, typ, specjalna):
    koszt_dict = wybierz_sowe_zwroc_koszt(potw_odbioru, odleglosc, typ, specjalna)
    koszt_str = waluta_dict_na_str(koszt_dict)
    potwierdzenie_str = "TAK" if potw_odbioru else "NIE"
    dane = {
        'adresat': adresat,
        'treść wiadomości': tresc,
        'koszt przesyłki': koszt_str,
        'potwierdzenie odbioru': potwierdzenie_str
    }
    sciezka_do_pliku = 'poczta_nadania_lista.csv'
    plik_istnieje = os.path.isfile(sciezka_do_pliku)
    with open(sciezka_do_pliku, mode='a', newline='', encoding='utf-8') as plik:
        fieldnames = ['adresat', 'treść wiadomości', 'koszt przesyłki', 'potwierdzenie odbioru']
        writer = csv.DictWriter(plik, fieldnames=fieldnames)

        if not plik_istnieje:
            writer.writeheader()

        writer.writerow(dane)


def poczta_wyslij_sowy(sciezka_do_pliku):
    data = datetime.now().strftime("%d_%m_%Y")
    nazwa_pliku_wyjsciowego = f"output_sowy_z_poczty_{data}.csv"
    
    with open(sciezka_do_pliku, mode='r', newline='', encoding='utf-8') as plik_csv:
        with open(nazwa_pliku_wyjsciowego, mode='w', newline='', encoding='utf-8') as plik_wyjsciowy:
            writer = csv.writer(plik_wyjsciowy)
            writer.writerow(['adresat', 'treść wiadomosci', 'koszt przesyłki', 'potwierdzenie odbioru', 'rzeczywisty koszt'])
            
            reader = csv.DictReader(plik_csv)
            for row in reader:
                adresat = row['adresat']
                tresc = row['treść wiadomości']
                koszt_przesylki = (row['koszt przesyłki'])
                
                potwierdzenie_odbioru = row['potwierdzenie odbioru']
                
                sowa_doleciala = wyslij_sowe(adresat, tresc)
                if sowa_doleciala:
                    rzeczywisty_koszt = koszt_przesylki
                else:
                    if potwierdzenie_odbioru == 'TAK':
                        rzeczywisty_koszt = 0 
                    else:
                        rzeczywisty_koszt = koszt_przesylki 
                
                writer.writerow([adresat, tresc, koszt_przesylki, potwierdzenie_odbioru, rzeczywisty_koszt])
