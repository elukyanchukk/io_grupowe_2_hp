from main import wyslij_sowe

def testuj_wysylanie_sowy():

    true_count = 0
    false_count = 0
    for _ in range(200):
        if wyslij_sowe("Adresat", "Treść"):
            true_count += 1
        else:
            false_count += 1

    return true_count, false_count

    true_count, false_count = testuj_wysylanie_sowy()

    print("Liczba poprawnie wysłanych sów:", true_count)
    print("Liczba błędnie wysłanych sów:", false_count)