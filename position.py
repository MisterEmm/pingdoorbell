from pymouse import PyMouse
from time import sleep

m = PyMouse()
while True:
    print(m.position())
    sleep(0.5)