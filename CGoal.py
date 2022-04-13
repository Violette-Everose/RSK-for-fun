#ça fonctionne bordel
import rsk
from time import sleep
import math


with rsk.Client(host='172.19.66.163', key='') as client:
    while True :
        xb=client.ball[0]
        yb=client.ball[1]

        goal=0
        atta=0
        bluex2=client.blue2.position[0]
        bluex2=client.blue2.position[1]

        bluex1=client.blue1.position[0]
        bluex1=client.blue1.position[1]

        if bluex2>bluex1 :
                goal=client.blue2
                goalx=client.blue2.position[0]
                goaly=client.blue2.position[1]
                atta=client.blue1
                attax=atta.position[0]
                attay=atta.position[1]
                print('Le goal est b2')

        if bluex1>bluex2 :
            goal=client.blue1
            goalx=client.blue1.position[0]
            goaly=client.blue1.position[1]
            atta=client.blue2
            attax=atta.position[0]
            attay=atta.position[1]
            print('Le goal est b1')

        if xb<0 :
            goal.goto((-0.70, yb, 0.), wait = False)
            atta.goto((xb-0.1, yb, 0.), wait = False)

            if -0.1<(xb-attax)<0.13 :
                atta.kick()

            if -0.1<(xb-goalx)<0.13 and -0.1<(yb-goaly)<0.13 :
                goal.kick()
        
        else :
            atta.goto((xb-0.1, yb, 0.), wait = False)
            goal.goto((-0.5, 0.3, 0.), wait=False)

            if -0.1<(xb-attax)<0.11 :
                atta.kick()