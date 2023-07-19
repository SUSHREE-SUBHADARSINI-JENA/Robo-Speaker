import os

if __name__ == '__main__':
    pass
    print("welcome")
    while True:
        x = input("enter what you want to pronounce: ")
        if x == "q":
            os.system("bye bye friends")
            break
        command = f"say{x}"
        os.system(command)
