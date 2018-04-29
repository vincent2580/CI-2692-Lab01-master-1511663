# Lab-01. Busqueda lineal y binaria. Ordenamiento por insercion. Experimentos. Analisis de resultados.

# Integrantes:
# Vincent Guacaran 15-11663

# extender el limite de la profundidad del stack de recursion
from sys import setrecursionlimit
from sys import path
setrecursionlimit(int(1e6))
path.insert(0, '..')

# importar base
from common.base.basic import read_file
from common.base.test_lab_01 import test_search
from common.base.test_lab_01 import test_sort

from common.base.search import verifier_linear_search
from common.base.search import verifier_binary_search
from common.base.sort import native_sort
from common.base.sort import verifier_sort


########################################################################

def linear_search(A, x):
	i=0
	while i!=len(A):
		if A[i]==x:
			return i
		else:
			i=i+1

	return -1

def binary_search(A, x):
	p=0
	q=len(A)
	r=q//2
	while q-p>1:
		if A[r]>x:
			q=r
			r=(q+p)//2
		elif A[r]<x:
			p=r
			r=(q+p)//2
		elif A[r]==x:
			return r
	return -1

def insertion_sort(A):
	for i in range(len(A)):
		k=0
		while k+1<len(A):
			if A[k]>A[k+1]:
				key=A[k]
				A[k]=A[k+1]
				A[k+1]=key
				k=k+1
			else:
				k=k+1
	return(A)



########################################################################


# leer los datos y preparar variables para correr experimentos
data = read_file('C:/Users/Vincent/Desktop/Lab/algo II/Lab 1/CI-2692-Lab01-master/data/espanol.txt')
sizes = [ 2**i for i in range(16) ]
runs_per_each_size = 10
fractions = [ .5, .05, .005, .0005]
runs_per_each_size_and_fraction = 3

# imprimir encabezado de resultados
print 'type,name,size,i,time,verification'

# experimentos para algoritmos de busqueda en arreglos
test_search('linear', sizes, data, runs_per_each_size, linear_search, verifier_linear_search, False)
test_search('binary', sizes, data, runs_per_each_size, binary_search, verifier_binary_search, True)

# experimentos para algoritmos de ordenamiento
test_sort('native', sizes, fractions, data, runs_per_each_size_and_fraction, native_sort, verifier_sort)
test_sort('insertion', sizes[:-1], fractions, data, runs_per_each_size_and_fraction, insertion_sort, verifier_sort)

