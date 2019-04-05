import os
import threading
import time
import sys

URL_PATHS = "./defaced.txt"

arguments = sys.argv

if (len(arguments) != 3):
    print("Error: Format = script.py  directoryPath pathUrls")
else:
    path = arguments[1]
    urls = arguments[2]
    print(path)
    def readLine(url, i):
        input = "phantomjs screens.js " + url + " " + urls + str(i)
        os.system(input)
        i += 1


    i = 0
    text_file = open(path, "r")
    lines = text_file.read().splitlines()
    print(lines.__len__())
    for url in lines:
        while threading.active_count() == 25:
            time.sleep(2)
            print(i)
        thread = threading.Thread(target=readLine, args=(url, i,))
        thread.start()


        i += 1
    text_file.close()


