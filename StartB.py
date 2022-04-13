import rsk
#Programme pour placer les robots à la position de départ
with rsk.Client(host='172.19.66.163', key='') as client:

    while True:
        client.blue1.goto((-0.5, -0.3, 0.), wait=False)

        client.blue2.goto((-0.5, 0.3, 0.), wait=False)