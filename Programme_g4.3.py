import rsk
from time import sleep
import math

robot= "green"
nombre= 2
if robot == "blue":
    ET=0
else :
    ET=3.14
    
xb=0
yb=0



with rsk.Client(host='172.19.66.163', key='') as client:
    client.robots[robot][nombre].kick
    print(client.ball)

    ballsort=0
    while True:
        print(client.ball)
        if client.ball is None:
            print('no',client.ball)
        else:
            xb=client.ball[0]
            yb=client.ball[1]

        #bluex1=client.blue1.position[0]
        #bluey1=client.blue1.position[1]

        #bluex2=client.blue2.position[0]
        #bluey2=client.blue2.position[1]

        robotx=client.robots[robot][nombre].position[0]
        roboty=client.robots[robot][nombre].position[1]
        print(robotx, roboty,ballsort)
        
        '''
        gbx1=greenx1-bluex1
        gbx2=greenx1-bluex2
        gby1=greenx1-bluey1
        gby2=greenx1-bluey2
        print(xb,yb)
        print(greenx1,greeny1)
        '''
        def siball():
            '''
            if (greenx1-xb<0.5)and(greenx1-xb>0.5):#and (greeny1-yb>0.5):
                client.green1.goto((greenx1-0.1,greeny1,3.14))
                client.green1.goto((xb+0.1,yb,3.14))'''
            print('jefaisdestruc')
        def versball():
            if (xb-robotx) < 0:
                if roboty<0:
                    client.robots[robot][nombre].goto((xb,yb-0.05, ET), wait=False)
                    print('ici')
                    if ((xb - robotx)< 0.2) and (((yb-roboty) < 0.1) and (yb-roboty) > -0.1) : 
                        client.robots[robot][nombre].kick()
                    print('ball devant')
                if roboty>0:
                    client.robots[robot][nombre].goto((xb,yb+0.05, ET), wait=False)
                    print('la')
                    if ((xb - robotx)< 0.2) and (((yb-roboty) < 0.1) and (yb-roboty) > -0.1) : 
                        client.robots[robot][nombre].kick()
                    print('ball devant')
                if ((xb - robotx)< 0.2) and (((yb-roboty) < 0.1) and (yb-roboty) > -0.1) : 
                    client.robots[robot][nombre].kick()
                    print('ball devant')
                    #sleep(100)
            elif (xb-robotx) > 0:
                client.robots[robot][nombre].goto((xb+0.15, yb, ET), wait=False)
                if (xb - robotx)< 0.1:
                    client.robots[robot][nombre].kick()
                    print('ball p')
                    #sleep(100)
            else:
                 print('azdh')
        def ballesort():
            print('testballsort')
            if xb > 0.9 :
                client.robots[robot][nombre].goto((0,0, ET), wait=False)
                ballsort=1
            if xb < -0.9 :
                client.robots[robot][nombre].goto((0,0, ET), wait=False)
                ballsort=1
            if xb < -0.5 :
                client.robots[robot][nombre].goto((0,0, ET), wait=False)
                ballsort=1
            if xb > 0.5 :
                client.robots[robot][nombre].goto((0,0, ET), wait=False)
                ballsort=1
            else:
                ballsort=0
              
        if client.ball is None:
            print('no',client.ball)
        else:
            xb=client.ball[0]
            yb=client.ball[1]   

        if robotx > 0.6 :
            client.robots[robot][nombre].goto((robotx-0.1, roboty, ET), wait=False)
        if robotx < -0.6 :
            client.robots[robot][nombre].goto((robotx+0.1, roboty, ET), wait=False)
        if roboty < -0.5 :
            client.robots[robot][nombre].goto((robotx, roboty+0.1, ET), wait=False)
        if roboty > 0.5 :
            client.robots[robot][nombre].goto((robotx, roboty-0.1, ET), wait=False)
        else:
            ballesort()
            if ballsort == 0:
                versball()
                

       #y 0.6 -0.6 x0.90 
