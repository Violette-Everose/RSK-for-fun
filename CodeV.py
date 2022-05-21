#Code UwU team pour l'équipe verte
import rsk
from time import sleep
import math
greenx1 = 0
greeny1 = 0
greenx2 = 0
greeny2 = 0
xb=0
yb=0
mi=2
ET=0.0
p = 0
if mi==1 :
    ET=3.14
    p = 1
else :
    ET=0.0
    p = -1

with rsk.Client(host='192.168.0.100', key='32315') as client:
    print(client.green2.position, client.green1.position)
    while True :
        try: 
            
            greenx2=client.green2.position[0]
            greeny1=client.green2.position[1]

            greenx1=client.green1.position[0]
            greeny1=client.green1.position[1]

            if client.ball is None:
                print('no',client.ball)
                print('Pas Balle')
            else:
                xb=client.ball[0]
                yb=client.ball[1]
                print('Balle')

            #La balle est dans la moitié de terrain Bleue
            if xb>0 :
                if greenx2<greenx1 :
                    goal=client.green1
                    goalx=client.green1.position[0]
                    goaly=client.green1.position[1]
                    atta=client.green2
                    print('Goal est G1')

                if greenx1<greenx2 :
                    goal=client.green2
                    goalx=client.green2.position[0]
                    goaly=client.green2.position[1]
                    atta=client.green1
                    
                    print('Goal est G2')

                attax=atta.position[0]
                attay=atta.position[1]

                if (xb)>(p*0.45) and (-0.45)<(yb)<(0.45) :
                    goal.goto((xb, yb, ET), wait=False)
                    if (goalx*p-xb)<0.13 and -0.05<(yb-goaly)<0.1 :
                        goal.kick()
                else :
                    goal.goto((0.75*p, yb, ET), wait=False)

                if (attax*p-xb)<0.13 and -0.05>(yb-attay)>0.1 :
                    atta.kick()
                    print('Pikachu attaque éclair')
                else :
                    atta.goto((xb-p*(0.05), yb, ET), wait=False)

                if xb>0.50 :
                    atta.goto((0.40*p, yb, ET))
                else :
                    atta.goto((xb-p*(0.05), yb, ET), wait=False)

               
               

            #La balle est dans la moitié de terrain Verte
            if xb<0:
                if greenx2*p<greenx1*p :
                    spare=client.green1
                    sparex=client.green1.position[0]
                    sparey=client.green1.position[1]
                    atta=client.green2
                    print('Spare atta est G1')

                if greenx1*p<greenx2*p :
                    spare=client.green2
                    sparex=client.green2.position[0]
                    sparey=client.green2.position[1]
                    atta=client.green1
                    print('Spare atta est G2')

                attax=atta.position[0]
                attay=atta.position[1]

                spare.goto((0.01, yb, ET), wait=False)
                atta.goto((xb-0.05*p, yb, ET), wait=False)
                
                if (sparex*p-xb)<0.25 and -0.8<(yb-sparey)<0.1 :
                    spare.goto((xb+p*(-0.05), yb, ET), wait=False)
                    if (sparex*p-xb)<0.1 and -0.8<(yb-sparey)<0.1 :
                        spare.kick()
                if (attax*p-xb)<0.1 and -0.8<(yb-attay)<0.1:
                    atta.kick()
                    print('Pikachu attaque éclair')

                if xb==0:
                    if greenx2*p<greenx1*p :
                        spare=client.green2
                        sparex=client.green2.position[0]
                        sparey=client.green2.position[1]
                        atta=client.green1
                        print('Spare atta est G2')
                    atta.goto((xb, yb, ET))
                    if (attax*p-xb)<0.1 and -0.8<(yb-attay)<0.1:
                        atta.kick()
                        print('Pikachu attaque éclair en x=0')

        except rsk.client.ClientError as e:
            print(e)