if __name__ == "__main__":
    import datetime
    import fileinput
    import os
    import socket
    import sys
    import time
    import threading

    ports = sys.argv[1:]
    interface = ""
    def bind(p):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((interface, int(p)))
        print("Listening on Port: " + str(p))
        while True:
            s.listen(5)
            conn, addr = s.accept()
            info = time.ctime() + " : connection from: " + \
                addr[0] + " on port: " + str(p)
            print(info)
            f = open('honeypot.log', 'a')
            conn.close()
            f.write(info + "\n")
            f.close()
    jobs = []
    for p in ports:
        t = threading.Thread(target=bind, args=(p,))
        jobs.append(p)
        t.start()
    for j in jobs:
        j.join