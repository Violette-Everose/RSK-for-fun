import rsk
from time import sleep
import math


with rsk.Client(host='172.19.66.163', key='') as client:
    while True :
        xb=client.ball[0]
        yb=client.ball[1]

        bluex1=client.blue1.position[0]
        bluey1=client.blue1.position[1]

        bluex2=client.blue2.position[0]
        bluey2=client.blue2.position[1]

        greenx2=client.green2.position[0]
        greeny2=client.green2.position[1]

        greenx1=client.green1.position[0]
        greeny1=client.green1.position[1]

        client.blue1.goto((-0.70, yb, 0.), wait = False)
        if -0.1<(xb-bluex1)<0.13 :
            client.blue1.kick()
            sleep(0.5)
        print('La balle est en', yb)
        print('Distance de la balle', xb-bluex1)