if __name__ == "__main__":
    small = 'abcdefghijklmnopqrstuvwxyz'
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


    def proverka():
        line = input()
        vse = small + big
        for i in line:
            if i not in vse:
                print('Введите только латинские буквы')
                return proverka()
        return line


    def rem(n):
        delet = set()

        for i in range(26):
            small_cnt = n.count(small[i])
            big_cnt = n.count(big[i])

            if small_cnt > big_cnt:
                delet.add(small[i])
                delet.add(big[i])

        res = ''
        for q in n:
            if q not in delet:
                res += q

        return res


    k = proverka()
    print(rem(k))

    pass  # Ваш код здесь
