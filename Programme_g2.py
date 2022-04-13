import rsk
from time import sleep
import math


with rsk.Client(host='172.19.66.163', key='') as client:
    print(client.ball)

    #client.green2.goto((0.5, -0.3, 3.14), wait=False)
    client.green1.goto((0.5, 0.3, 3.14), wait=False)

    while True:
        atta=0
        goal=0

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

        gbx1=greenx1-bluex1
        gbx2=greenx1-bluex2

        gby1=greenx1-bluey1
        gby2=greenx1-bluey2

        if greenx2>greenx1 :
                goal=client.green2
                goalx=client.green2.position[0]
                goaly=client.green2.position[1]
                atta=client.green1
                attax=atta.position[0]
                attay=atta.position[1]
                print('Le goal est g2')

        if greenx1>greenx2 :
            goal=client.green1
            goalx=client.green1.position[0]
            goaly=client.green1.position[1]
            atta=client.green2
            attax=atta.position[0]
            attay=atta.position[1]
            print('Le goal est b1')

        print(xb,yb)
        print("Robot g1 en", client.green1.pose)

        if xb>0 :

            goal.goto((0.70, yb, 3.14))

            client.atta.goto((xb+0.03, yb, 3.14), wait = False)
            if (xb-attax)<0.1 and (yb-attay)<0.05:
                client.goal.control(0., 0., 0.)
                #client.atta.kick()
            
            if attax>0.9:
                client.atta.goto((0.85, attay, 3.14), wait = False)
                #print(client.atta.pose)
                    
            if (attax<-0.9):
                client.atta.goto((-0.85, attay, 3.14), wait = False)
                #print(client.atta.pose)
                    
            if (attay>0.6):
                client.atta.goto((attax, 0.55, 0.), wait = False)
                #print(client.atta.pose)
                    
            if (attay<0.6):
                client.atta.goto((attax, 0.55, 0.), wait = False)

        if (xb<0) :
            client.green1.goto((xb+0.03, yb, 3.14), wait = False)
            if (xb-greenx1)<0.1 and (yb-greeny1)<0.05:
                if greeny1<0 :
                    client.green1.goto((xb+0.03, yb-0.03, 2.9), wait = False)
                    client.green1.kick()
                    sleep(1)
                if greeny1>0 :
                    client.green1.goto((xb+0.03, yb+0.05, 3.7), wait = False)

            elif (greenx1 > 0.9) :
                client.green1.goto((0.85, greeny1, 3.14), wait = False)
                #print(client.green1.pose)
                    
            elif (greenx1 < -0.9) :
                client.blue1.goto((-0.85, greeny1, 3.14), wait = False)
                #print(client.green1.pose)
                    
            elif (greeny1 > 0.6) :
                client.green1.goto((greenx1, 0.55, 0.), wait = False)
                #print(client.green1.pose)
                    
            elif (greeny1 < 0.6) :
                client.green1.goto((greenx1, 0.55, 0.), wait = False)
                #print(client.green1.pose)
                    
            elif (greenx1 > 0.9) :
                client.green1.goto((0.85, greeny1, 3.14), wait = False)
                #print(client.green2.pose)
                
       #y 0.6 -0.6 x0.90
       #Chosir l'attaquant : tester qui est le plus près de la balle puis le stocker dans une variable(atta) et mettre (atta) dans le code du joueur attaquant : à tester (en cours)