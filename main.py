import os

def load_m3u(path: str):
    with open(path) as file:
        string = file.read()
    return string


if __name__ == "__main__":
    cwd = os.getcwd()
    load_m3u()
