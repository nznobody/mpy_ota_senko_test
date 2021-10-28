# Default template for Digi projects
import time
import network
conn = network.Cellular()
from xbee import XBee
x = XBee()


def wait_connected():
    global conn
    print("Waiting for the module to be connected to the cellular network... ")
    while not conn.isconnected():
        time.sleep(5)
    print("[CONNECTED]")


def main():
    wait_connected()


if __name__ == "__main__":
    main()
