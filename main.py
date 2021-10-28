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

    tb_client = mon_thingsboard.init("KHVvf5tXJAZtZTkXlxhF")

    # Main loop because digi micropython does not have threads or asyncio :(
    next_ve_time = time.time()
    while True:
        curr_time = time.time()
        if curr_time >= next_ve_time:
            try:
                resp = mon_vedirect.read_single_clean()
                logging.info("Sending vedirect to Thingsboard")
                tb_client.send_telemetry(resp)
                logging.info("Done, will run again in ~30s")
                next_ve_time = curr_time + 30  # Ignore time passed during operation to attempt to make periodic
            except ValueError as _:
                pass
        tb_client.check_msg()
        time.sleep_ms(100)


if __name__ == "__main__":
    main()
