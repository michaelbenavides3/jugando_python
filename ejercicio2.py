print('Ejercicio 2'.center(50))

#2. **Ahorcado:**  Debes presentar el siguiente menú al usuario


#1.   Agregar Palabra (solicita una palabra y la agregas a una lista de palabras)
#2.  Configurar (debes preguntar el número de equivocaciones permitidas)
#3.	Jugar
#4.	Salir


#La opción 3 de jugar debe obtener una palabra aleatoriamente de la lista de palabras y presentar en pantalla los espacios de cada letra de
#la palabra seleccionada.  Por ejemplo, si la palabra es paciencia, se debe mostrar en pantalla así _ _ _ _ _ _ _ _ _  Posteriormente
#debe preguntar una letra al usuario y si la letra se encuentra, debe mostrarla en la posición correcta.  Para el caso anterior, si la
#letra seleccionada es la a, se debería mostrar así
#_ A _ _ _ _ _ _ A En caso de error debe indicar cuantas oportunidades le quedan para adivinar.  El juego termina cuando el usuario llena
#la palabra antes de terminar sus oportunidades (en ese caso gana) o cuando se terminan sus oportunidades sin llenar la palabra (en ese
#caso pierde).  Al perder o ganar se debe presentar un mensaje indicando cual era la palabra escondida.      Usar funciones.
import random
import time


print('este juego se llama el del ahorcado.')
print('')

#creamos una lista vacia, que es donde el usuario almacenara la palabras ingresadas,
lista_palabras = [ ]
#creamos una variable para almacenar el numero maximo de intento
maximo_intentos = 0
while True:
	print('Bienvenido, elegir opcion.\n1. agregar palbra.\n2. numero de intentos.\n3. jugar.\n4. salir.')
	print('')
	opcion = int(input('Ingresar opcion: '))
	if opcion == 1:
		palabra = input('ingresar palabras: ')
		lista_palabras.append(palabra)
		while True:
			print('palabra ingresada correctamente.\nopcion 1. nueva palabra: \nopcion 2. dejar de ingresar palabras. ')
			opcion_palabra = int(input('ingresar: opcion_palabra: '))
			if opcion_palabra == 1:
	#agregamos la palabra, a la lista palabras, con el .append, que significa agregar o anadir
				palabra = input('ingresar palabra: ')
				lista_palabras.append(palabra)
			elif opcion_palabra == 2:
				print(f'no ingresaste mas palabras.\nPalabras ingresadas:')
				print(lista_palabras)
			#print('total palabras'len.listas_palabras)
				break
			else:
				print('no existe')
	if opcion == 2:
		maximo_intentos = int(input('ingresar numero maximo de intentos: '))

	if opcion == 3:
		if not lista_palabras:
			print('no existen las palabras. no se puede jugar.')
		else:
			palabra_secreta = random.choice(lista_palabras)
			print('palabra selecciona, preparados....')
			time.sleep(5)
			print('VAMOS A JUGAR')