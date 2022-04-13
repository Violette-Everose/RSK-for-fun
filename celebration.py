import rsk
#ET C'EST LE BUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUT
with rsk.Client(host='172.19.66.163', key='') as client:
    client.green2.kick(0.2)
    print(client.ball)

    while True:
        client.green2.goto((0., -0.05, 1.57), wait=False)

        client.green1.goto((0., 0.05, -1.57), wait=False)

        client.green2.control(0.1, -0.05, 1.57)

        client.green1.control(0.1, 0.05, -1.57)


        '''client.green1.kick()
        client.green1.kick()'''