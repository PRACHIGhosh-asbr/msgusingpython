
import random



import pyautogui as pg

import time

animal=('my', 'love')


time.sleep(6)

for i in range(10):
  a=random.choice(animal)
  pg.write('You are ' +a)
  pg.press('enter')

#you need to login your whatsapp via chrome to run this program. 