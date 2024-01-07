class Main:
    def __init__(self, name, password):
        self.name = self.check_str(name)
        self.password = password
        self.log = self.Log()

    @classmethod
    def check_str(cls, name):
        if type(name) != str:
            raise TypeError("Имя - строка из букв")
        return name

    @classmethod
    def check_int(cls, password):
        if type(password) != int:
            raise TypeError("Пароль - цифры")
        return password

    class Log:
        Log = 0

        def __init__(self):
            self.log = self.Log
            self.raise_log()

        def __str__(self):
            return str(self.log)

        @classmethod
        def raise_log(cls):
            cls.Log += 1


Nikita = Main("Nikita", 2215779638)
Vasya = Main("Vasya", 221577)
print(Nikita.log)
print(Vasya.log)
print(Nikita.__dict__)
print(Nikita.log.__dict__)
