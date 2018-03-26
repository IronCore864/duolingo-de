from duolingo import Duolingo

if __name__ == "__main__":
    d = Duolingo()
    d.login("guotiexin@gmail.com", "xxx")
    d.generate_list()
