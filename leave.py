import rsk
#Programme pour éviter de sortir du terrain
#Coordonnées du terrain:     x : 0.9     y : 0.6

with rsk.Client(host='172.19.66.163', key='') as client:
    client.green2.kick(0.2)
    print(client.ball)

    bluex1=client.blue1.position[0]
    bluey1=client.blue1.position[1]

    bluex2=client.blue2.position[0]
    bluey2=client.blue2.position[1]

    while True: 
        bluex1=client.blue1.position[0]
        bluey1=client.blue1.position[1]

        if (-0.9<bluex1<0.9) and (-0.6<bluey1<0.6) :
            client.blue1.control(0., 0., 0.)
            print(client.blue1.pose)
            
        elif bluex1 > 0.9 :
            client.blue1.goto((0.85, bluey1, 0.))
            print(client.blue1.pose)
            
        elif bluex1 < -0.9 :
            client.blue1.goto((-0.85, bluey1, 0.))
            print(client.blue1.pose)
            
        elif bluey1 > 0.6 :
            client.blue1.goto((bluex1, 0.55, 0.))
            print(client.blue1.pose)
            
        elif bluey1 < -0.6 :
            client.blue1.goto((bluex1, -0.55, 0.))
            print(client.blue1.pose)