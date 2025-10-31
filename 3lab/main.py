

if __name__ == "__main__":
    import os

    res = {}


    def qwe(n):
        global res
        dirs = []
        files = []

        try:
            a = os.listdir(n)
        except:
            res[n] = ([], [])
            return res

        for i in a:
            path = os.path.join(n, i)
            if os.path.isdir(path):
                dirs.append(i)
            elif os.path.isfile(path):
                files.append(i)

        res[n] = (dirs, files)

        for i in dirs:
            qwe(os.path.join(n, i))

        return res


    a = qwe('.')

    for path, (dirs, files) in res.items():
        if len(dirs) > 0:
            if len(files) > 0:
                print(f'Папка: "{path}";  Папок в ней: {dirs};  Файлов в ней: {files}')
            else:
                print(f'Папка: "{path}";  Папок в ней: {dirs}')
        else:
            if len(files) > 0:
                print(f'Папка: "{path}";  Файлов в ней: {files}')
            else:
                print(f'Пустая папка: {path}')
    pass # Ваш код здесь
