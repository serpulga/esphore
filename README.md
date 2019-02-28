### ESPHORE

**Esphore** (ESP + Semaphore) is an example project using **Micropython** and `uasyncio` on **ESP8266** systems.


### FUNCTIONALITY

This is a simplified model of a *"smart"* pedestrian crossing semaphore which prevents unnecessary stops by allowing automoviles pass indefinitely until there is an actual cross request. 

*GREEN* LED is always turned on unless *CROSS DETECTOR* is pressed. When *CROSS DETECTOR* is triggered, the *RED* LED will be turned on during a period of `cross_time` seconds. Transitions will occur, at least, every `period` seconds.


### SCHEMATIC

![Schematic](https://i.imgur.com/8JiWGv7.png)


`L3`: *GREED* LED

`R3`: *GREED* LED Resistor [~200 Ω]

`L2`: *RED* LED

`R2`: *RED* LED Resistor [~200 Ω]

`S1`: *CROSS DETECTOR* push button

`R1`: *CROSS DETECTOR* push button Resitor [10 KΩ]

`NOTE`: *CROSS INDICATOR* LED is an onboard LED wired to `GPIO16` (*as far as Micropython mapping goes*)
