if __name__ == "__main__":
    work_otv = {}
    byk_otv = {}

    S = input()


    def schet(n, mass):
        for ind in n:
            if ind not in mass:
                mass[ind] = 1
            else:
                mass[ind] += 1
        return mass


    word = S
    byk = S.replace(' ', '')
    for i in '0123456789,.;:!&?':
        word = word.replace(i, ' ')
        byk = byk.replace(i, '')
    word = word.split()

    work_otv = schet(word, work_otv)
    byk_otv = schet(byk, byk_otv)

    print(f"Количество слов: {work_otv}")
    print(f"Количество букв: {byk_otv}")

    top_slov = sorted(work_otv.items(), key=lambda item: item[1], reverse=True)[0:5]
    print(f"5 самых популярных слов: {top_slov}")
    top_byk = sorted(byk_otv.items(), key=lambda item: item[1], reverse=True)[0:5]
    print(f"5 самых популярных букв: {top_byk}")

    pass  # Ваш код здесь
