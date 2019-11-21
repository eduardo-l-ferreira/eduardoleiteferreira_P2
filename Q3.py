def isCollisionDetected(rec1, rec2):
    rec1_xi = rec1['bottomLeft'][0]
    rec1_xf = rec1['topRight'][0]
    rec1_yi = rec1['bottomLeft'][1]
    rec1_yf = rec1['topRight'][1]

    rec2_xi = rec2['bottomLeft'][0]
    rec2_xf = rec2['topRight'][0]
    rec2_yi = rec2['bottomLeft'][1]
    rec2_yf = rec2['topRight'][1]

    if (rec1_xi < rec2_xf and rec1_xf > rec2_xi and rec1_yi < rec2_yf and rec1_yf > rec2_yi):
        return True
    return False

def main():

    BLx1 = float(input())
    BLy1 = float(input())
    TRx1 = float(input())
    TRy1 = float(input())

    BL1 = (BLx1, BLy1)
    TR1 = (TRx1, TRy1)
    
    rectangle1 = {'bottomLeft':BL1,'topRight':TR1}
    
    BLx2 = float(input())
    BLy2 = float(input())
    TRx2 = float(input())
    TRy2 = float(input())

    BL2 = (BLx2, BLy2)
    TR2 = (TRx2, TRy2)

    rectangle2 = {'bottomLeft':BL2,'topRight':TR2}

    colisao = isCollisionDetected(rectangle1, rectangle2)

    if colisao == True:
        print('Colisão detectada')

    else:
        print('Colisão não detectada')

main()
