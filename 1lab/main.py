

if __name__ == "__main__":
    slova_otv = {}
    byk_otv = {}
    
    S = input()
    
    def schet(n, mass):
        for i in n:
            if i not in mass:
                mass[i] = 1
            else:
                mass[i] += 1
        return mass
    
    slova = S
    byk = S.replace(" ", "")
    for i in '0123456789':
        slova = slova.replace(i, " ")
        byk = byk.replace(i, "")
    slova = slova.split()
    
    slova_otv = schet(slova, slova_otv)
    byk_otv = schet(byk, byk_otv)
    
    print(f"Количество слов: {slova_otv}")
    print(f"Количество букв: {byk_otv}")
    
    top_slov = sorted(slova_otv.items(), key=lambda item: item[1], reverse=True)[0:5]
    print(f"5 самых популярных слов: {top_slov}")
    top_byk = sorted(byk_otv.items(), key=lambda item: item[1], reverse=True)[0:5]
    print(f"5 самых популярных букв: {top_byk}")
    pass # Ваш код здесь
