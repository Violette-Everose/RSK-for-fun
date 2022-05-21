#Code UwU team pour l'équipe blueue
import rsk
from time import sleep
import math
bluex1 = 0
bluey1 = 0
bluex2 = 0
bluey2 = 0
xb=0
yb=0
mi=1
ET=0.0
p = 0
if mi==1 :
    ET=0.0
    p = 1
else :
    ET=3.14
    p = -1

with rsk.Client(host='192.168.0.100', key='') as client:
    print(client.blue2.position, client.blue1.position)
    while True :
        try: 
            
            bluex2=client.blue2.position[0]
            bluey1=client.blue2.position[1]

            bluex1=client.blue1.position[0]
            bluey1=client.blue1.position[1]

            if client.ball is None:
                print('no',client.ball)
                print('Pas Balle')
            else:
                xb=client.ball[0]
                yb=client.ball[1]
                print('Balle')

            #La balle est dans la moitié de terrain Bleue
            if xb>0 :
                if bluex1<bluex2 :
                    goal=client.blue1
                    goalx=client.blue1.position[0]
                    goaly=client.blue1.position[1]
                    atta=client.blue2
                    print('Goal est B1')

                if bluex2<bluex1 :
                    goal=client.blue2
                    goalx=client.blue2.position[0]
                    goaly=client.blue2.position[1]
                    atta=client.blue1
                    
                    print('Goal est B2')

                attax=atta.position[0]
                attay=atta.position[1]

                if (xb)<(p*-0.55) and (p*-0.45)<(yb)<(p*0.45) :
                    goal.goto((xb, yb, ET), wait=False)
                    if (xb-goalx*p)<0.13 and -0.05<(yb-goaly)<0.1 :
                        goal.kick()
                else :
                    goal.goto((-0.75, yb, ET), wait=False)

                if (xb-attax*p)<0.13 and -0.05<(yb-attay)<0.1 :
                    atta.kick()
                    print('Pikachu attaque éclair')
                else :
                    atta.goto((xb-p*(-0.05), yb, ET), wait=False)

                if xb<0.50 :
                    atta.goto((-0.40*p, yb, ET))
                else :
                    atta.goto((xb-p*(-0.05), yb, ET), wait=False)

               
               

            #La balle est dans la moitié de terrain Verte
            if xb<0:
                if bluex1*p<bluex2*p :
                    spare=client.blue1
                    sparex=client.blue1.position[0]
                    sparey=client.blue1.position[1]
                    atta=client.blue2
                    print('Spare atta est B1')

                if bluex2*p<bluex1*p :
                    spare=client.blue2
                    sparex=client.blue2.position[0]
                    sparey=client.blue2.position[1]
                    atta=client.blue1
                    print('Spare atta est B2')

                attax=atta.position[0]
                attay=atta.position[1]

                spare.goto((0.0, yb, ET), wait=False)
                atta.goto((xb-0.05*p, yb, ET), wait=False)
                
                if (xb-sparex*p)<0.25 and -0.8<(yb-sparey)<0.1 :
                    spare.goto((xb+p*(-0.05), yb, ET), wait=False)
                    if (xb-sparex*p)<0.1 and -0.8<(yb-sparey)<0.1 :
                        spare.kick()
                if (xb-attax*p)<0.13 and -0.8<(yb-attay)<0.2:
                    atta.kick()
                    print('Pikachu attaque éclair')
                if (xb-attax)<0.04:
                    atta.kick()

                if xb==0:
                    if bluex2*p<bluex1*p :
                        spare=client.blue2
                        sparex=client.blue2.position[0]
                        sparey=client.blue2.position[1]
                        atta=client.blue1
                        print('Spare atta est B2')
                    atta.goto((xb, yb, ET))
                    if (xb-attax*p)<0.1 and -0.8<(yb-attay)<0.1:
                        atta.kick()
                        print('Pikachu attaque éclair en x=0')

        except rsk.client.ClientError as e:
            print(e)