import rsk
#Programme pour placer les robots à la position de départ
with rsk.Client(host='172.19.66.163', key='') as client:
    client.green2.kick(0.2)
    print(client.ball)

    while True:
        client.green2.goto((0.5, -0.3, 3.14), wait=False)

        client.green1.goto((0.5, 0.3, 3.14), wait=False)
