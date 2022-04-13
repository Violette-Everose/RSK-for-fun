import rsk
from time import sleep
import math


with rsk.Client(host='172.19.66.163', key='') as client:
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

        while True :
            while (bluex1-greenx1)>0.1 :
                client.blue1.control(0.1, 0., 0.)
            while (bluey1-greeny1)>0.1 :
                client.blue1.control(0., 0.1, 0.)