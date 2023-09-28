## Lidar_LDS-01_HLDS
Lidar LDS-01 Hitachi-LG Data Storage Python interface

## Python script:
```
$python lidar_LDS-01_HLDS.py

>port: /dev/cu.usbserial-A50285BI  baud_rate: 230400
>lidar connect: True
>r[ 359.0 ]= 0.784
>r[ 358.0 ]= 0.789
>r[ 357.0 ]= 0.801
>r[ 356.0 ]= 0.797
>r[ 355.0 ]= 0.799
>r[ 354.0 ]= 0.805
>r[ 353.0 ]= 0.815
```
_____

## C source:

LDS-01 supports Windows, Linux, and MacOS development environments for general purposes.

The software requirement is:
<li>GCC (for Linux and macOS), MinGW (for Windows)</li>
<li>Boost library (Lib for boost system, tested on v1.66.0)</li>



Download:
```
$ git clone https://github.com/ROBOTIS-GIT/hls_lfcd_lds_driver.git
```
Or get soucre from <a href="https://github.com/silenzio777/Lidar_LDS-01_HLDS/tree/main/C_lds_driver">C_lds_driver</a> directory


Build:
```
$ cd hls_lfcd_lds_driver/applications/lds_driver/
$ make
```

Run:
```
$ ./lds_driver
r[359]=0.438000,r[358]=0.385000,r[357]=0.379000,...
```
_____


## Wiring diagram with USB to UART TTL FTDI FT232RL chip:

![lidar_wires](https://github.com/silenzio777/Lidar_LDS-01_HLDS/assets/7931919/2f83f679-5960-458f-9e91-7a6ae71e2fd7)


<br>
<br>



## Device:

<img width="414" alt="Screen Shot 2023-08-11 at 17 34 28" src="https://github.com/silenzio777/Lidar_LDS-01_HLDS/assets/7931919/76decc4e-beb7-4d17-b073-b4ec62fe7da8">

