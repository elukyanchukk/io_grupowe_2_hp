from main import wybierz_sowe_zwroc_koszt

assert wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'wyjec') == {'galeon': 0, 'sykl': 0, 'knut': 13}
assert wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'list gonczy') == {'galeon': 0, 'sykl': 1, 'knut': 9}
assert wybierz_sowe_zwroc_koszt(True, 'krajowa', 'list', 'wyjec') == {'galeon': 0, 'sykl': 0, 'knut': 23}
assert wybierz_sowe_zwroc_koszt(True, 'dalekobiezna', 'list', 'wyjec') == {'galeon': 0, 'sykl': 0, 'knut': 31}
assert wybierz_sowe_zwroc_koszt(True, 'lokalna', 'paczka', 'wyjec') == {'galeon': 0, 'sykl': 0, 'knut': 18}
assert wybierz_sowe_zwroc_koszt(True, 'lokalna', 'paczka', 'list gonczy') == {'galeon': 0, 'sykl': 1, 'knut': 14}
assert wybierz_sowe_zwroc_koszt(True, 'krajowa', 'paczka', 'wyjec') == {'galeon': 0, 'sykl': 1, 'knut': 13}
assert wybierz_sowe_zwroc_koszt(True, 'dalekobiezna', 'paczka', 'wyjec') == {'galeon': 0, 'sykl': 2, 'knut': 12}
assert wybierz_sowe_zwroc_koszt(False, 'lokalna', 'list', 'wyjec') == {'galeon': 0, 'sykl': 0, 'knut': 6}
assert wybierz_sowe_zwroc_koszt(False, 'lokalna', 'list', 'list gonczy') == {'galeon': 0, 'sykl': 1, 'knut': 2}
assert wybierz_sowe_zwroc_koszt(False, 'krajowa', 'list', 'wyjec') == {'galeon': 0, 'sykl': 0, 'knut': 16}
assert wybierz_sowe_zwroc_koszt(False, 'dalekobiezna', 'list', 'wyjec') == {'galeon': 0, 'sykl': 0, 'knut': 24}
assert wybierz_sowe_zwroc_koszt(False, 'lokalna', 'paczka', 'wyjec') == {'galeon': 0, 'sykl': 0, 'knut': 11}
assert wybierz_sowe_zwroc_koszt(False, 'lokalna', 'paczka', 'list gonczy') == {'galeon': 0, 'sykl': 1, 'knut': 7}
assert wybierz_sowe_zwroc_koszt(False, 'krajowa', 'paczka', 'wyjec') == {'galeon': 0, 'sykl': 1, 'knut': 6}
assert wybierz_sowe_zwroc_koszt(False, 'dalekobiezna', 'paczka', 'wyjec') == {'galeon': 0, 'sykl': 2, 'knut': 5}