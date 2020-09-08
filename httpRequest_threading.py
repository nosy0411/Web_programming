from urllib.request import urlopen
from threading import Thread
from time import sleep


def printResult():
    while True:
        print("hello")
        html = urlopen("http://www.google.com/")
        print(html.read())

        # if you want to change cycle from 1 second to 3 second please change here to '3'.
        sleep(1)


def main():
    th = Thread(target=printResult)
    th.demon = True
    th.start()


if __name__ == '__main__':
    main()
