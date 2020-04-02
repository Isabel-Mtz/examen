# -*- coding: utf-8 -*-
"""
Editor de Spyder
autores: 
    Luna Gonzales Rosio.
    Martinez Garcia Isabel 
Este es un archivo temporal.
"""
# =============================================================================
# """
#Primos  <generadores>  30 pts
#Realice una generador que devuelva  de todos lo numeros primos
#existentes de 0 hasta n-1 que cumpla con el siguiente prototipo:
# [2, 3 ,5 ,7 ]
# =============================================================================
def gPrimo(N):
    def primo(i):
        if i <= 1:
            return False
        for j in range (2,i):
            if i % j == 0:
                return False
        return True
    i = 0
    while (i <= N):
        if primo(i):
            yield i
        i += 1
a= gPrimo(10)
z = [e for e in a]
print (z)
# =============================================================================
#Bada Boom!!! <generadores> 20 pts
#	
#	Defina un generador que reciba un numero entero positivo mayor a 0 N,
#	dicho generador proporciona numero de 1 hasta N
#	con las siguientes condiciones:
#		1) si es multiplo de 3 coloque la cadena "Bada"
#		2) si es multiplo de 5 coloque la cadena "Boom!!"
#		3) si es multiplo de 3 y 5 coloque "Bada Boom!!"
# =============================================================================
def genBadaBoom(N):
    i = 0
    while i < N:
        i = i + 1
        Bada = i % 3 == 0
        Boom = i % 5 == 0
        if Bada and Boom:
            yield "Bada Boom!!"
        elif Bada:
            yield "Bada"
        elif Boom:
            yield "Boom!!"
        else:
            yield i

a = genBadaBoom(10)
z = [e for e in a]
print(z)
# =============================================================================
# Combinaciones <Comprensión de listas> 30pts
#Una tienda de ropa quiere saber cuantos conjuntos se pueden crear 
#a partir de un grupo de 5 camisas (roja,negra,azul,morada y cafe),      
#4 pantalones (negro, azul, cafe obscuro y crema) y uno de 4 accesorios
#posibles (cinturon, tirantes, lentes, fedora)
#1) Obtenga una lista con todos los conjuntos posibles e imprimala en pantalla
#2) imprima un mensaje donde mencione la cantidad de conjuntos posibles	
# =============================================================================
Z = ['camisa roja','camisa negra','camisa azul','camisa morada','camisa cafe']
Y = ['pantalon negro','pantalon azul','pantalon cafe oscuro','pantalon crema']
W = ['cinturon','tirantes','lentes','fedora']

Combinacion = [[z,y,w] for z in Z for y in Y for w in W ]
print (Combinacion)
print(len(Combinacion))
# =============================================================================
# ¿Fedora?  <Comprensión de listas >  15 pts
	#Del problema anterior imprima una lista que tenga todos los conjuntos
	#que incluyen un sombrero fedora y tambien despliegue su longitud
# =============================================================================
N = [ con for con in Combinacion if con[2]=='fedora']
print(N)
print(len(N))
# =============================================================================