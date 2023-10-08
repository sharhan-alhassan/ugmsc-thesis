
## Run output
```sh
# 1. python3 code.py
Label : bar
Begin : Tue Oct  3 16:49:51 2023
Duration : 4909462.1490 us
-------------------------------
PKG :
        socket 0 :  18372450.0000 uJ
-------------------------------
DRAM :
        socket 0 :  1750423.0000 uJ
-------------------------------

# PKG is the CPU energy consumption
# DRAM is the RAM energy consumption
```

## Errors Fix
```sh
# 1. PermissionError: [Errno 13] Permission denied: '/sys/class/powercap/intel-rapl/intel-rapl:0/energy_uj'

sudo chmod -R a+r /sys/class/powercap/intel-rapl  

# 2. 

```