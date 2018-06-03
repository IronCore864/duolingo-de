from duolingo import Duolingo

if __name__ == "__main__":
    d = Duolingo("your_duolingo_user_here", "your_duolingo_pwd_here")
    d.generate_list()
