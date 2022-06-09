import wiringpi
import sys

wiringpi.wiringPiSetup()
serial = wiringpi.serialOpen('/dev/ttyS4', 115200)

for count in range(0, 256):
    try:
        print("\nOut: %3d:" % count, end="")
        wiringpi.serialFlush(serial)
        wiringpi.serialPutchar(serial, count)
        wiringpi.delayMicroseconds(300000)

        while wiringpi.serialDataAvail(serial):
            print(" -> %3d" % wiringpi.serialGetchar(serial))
            wiringpi.serialFlush(serial)
        print("\n")
    except KeyboardInterrupt:
        print("\nexit")
        sys.exit(0)

wiringpi.serialClose(serial)  # Pass in ID
