import math
def main():
    #escribe tu código abajo de esta línea
    A=float(input('Area a pintar en metros: '))
    R=float(input('Rendimiento (m2/l): '))
    L=int(math.ceil(A/R))
    print('Litros a comprar: '+str(L))

if __name__ == '__main__':
    main()
#Area a pintar en metros: 857.5
#Rendimiento (m2/l): 10
#Litros a comprar: 86