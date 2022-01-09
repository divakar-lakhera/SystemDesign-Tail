from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
import watchdog
import tail
from threading import Thread
from time import sleep
import args

appFlask = Flask("Backend-Server")
webSocket = SocketIO(appFlask, cors_allowed_origins="*")
CORS(appFlask)

HAS_CONNECTION = False


def printSocket(msg):
    webSocket.emit("on_connect", msg)


def checker_thread():
    doggy = watchdog.watchdog(args.SOURCE_FILE)
    taily = tail.tailn(n_lines=args.NLINES, filename=args.SOURCE_FILE)
    while True:
        sleep(0.5)
        #   Check if file has some changes
        ret = doggy.get_changes()
        if ret == "NA":
            continue
        print(ret)
        # Get last N lines
        printSocket(taily.get_tail())


# File Checker Thread
thread = Thread(target=checker_thread)


@appFlask.route("/")
def index():
    return "Hello"


@webSocket.on("connect")
def test_connect():
    global HAS_CONNECTION
    HAS_CONNECTION = True
    print("Incomming Connection")
    printSocket("Ready")


if __name__ == "__main__":
    thread.start()
    webSocket.run(appFlask)
    thread.join()
