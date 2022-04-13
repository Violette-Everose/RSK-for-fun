import rsk
from time import sleep

#import math

with rsk.Client(host='172.19.66.163', key='') as client:
    client.green2.kick()
    print(client.ball)
    while True:
        xb=client.ball[0]
        yb=client.ball[1]
        bluex1=client.blue1.position[0]
        bluey1=client.blue1.position[1]
        bluex2=client.blue2.position[0]
        bluey2=client.blue2.position[1]
        greenx=client.green2.position[0]
        greeny=client.green2.position[1]
        gbx1=greenx-bluex1
        gbx2=greenx-bluex2
        gby1=greenx-bluey1
        gby2=greenx-bluey2
        print(xb,yb)
        print(greenx,greeny)
        if xb < 0:
            client.green2.goto((xb,yb, 0.))
            if ((xb - greenx)< 0.2) and ((yb-greeny) < 0.1) :
                client.green2.kick()
                #sleep(100)
    
        elif xb > 0:
            client.green2.goto((xb+0.1, yb, 0.))
            if (xb - greeny)< 0.1:
                client.green2.kick()
                #sleep(100)
        if (gbx1)<0.1 or (gbx2) :
            client.green2.control(0.1, 0., 0.)
        if (gby1)<0.1 or (gby2) :
            client.green2.control(0., 0.1, 0.)