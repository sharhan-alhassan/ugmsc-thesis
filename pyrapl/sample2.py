
import pyRAPL
import time

pyRAPL.setup()

def main():
    for i in range(1, 25):
        # print(i)
        time.sleep(0.1)


with pyRAPL.Measurement('bar'):
    main()