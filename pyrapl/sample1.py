import pyRAPL
import time

def main():
    for i in range(1, 25):
        # print(i)
        time.sleep(0.1)

pyRAPL.setup()
measure = pyRAPL.Measurement('bar')
with measure:
    measure.begin()

    main()

    measure.end()
    