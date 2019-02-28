ESPHORE
=======

**Esphore** (ESP + Semaphore) is an example project using **Micropython** and `uasyncio` on **ESP8266** systems.


FUNCTIONALITY
=============

This is a simplified model of a *"smart"* pedestrian crossing semaphore which prevents unnecessary stops by allowing automoviles pass indefinitely until there is an actual cross request. 

*GREEN* LED is always turned on unless *CROSS DETECTOR* is pressed. When *CROSS DETECTOR* is triggered, the *RED* LED will be turned on during a period of `cross_time` seconds. Transitions will occur, at least, every `period` seconds.
