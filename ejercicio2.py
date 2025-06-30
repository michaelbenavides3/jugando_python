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
# Bucle principal del programa que muestra el menú y permite elegir opciones
while True:
	#mostrar menu principal
	print('Bienvenido, elegir opcion.\n1. agregar palbra.\n2. numero de intentos.\n3. jugar.\n4. salir.')
	print('')
	#variable para alamcenar la respuesta del usuario
	opcion = int(input('Ingresar opcion: '))
	#opcion 1 agregar palabra a la lista
	if opcion == 1:
		#pedimos la primera palabra que se agrega a  la lista vacia
		palabra = input('ingresar palabras: ')
		#lista_palabra es la lista vacia, con .append agregarmos la palabra ingresada
		lista_palabras.append(palabra)
		#creamos un submenu con el ciclo while
		while True:
			#mostramos el menu
			print('palabra ingresada correctamente.\nopcion 1. nueva palabra: \nopcion 2. dejar de ingresar palabras. ')
			#con esta variable almacena la respuesta del submenu
			opcion_palabra = int(input('ingresar: opcion_palabra: '))
			#cuando se cumpla la condicion 1 del submenu ingresar aca
			if opcion_palabra == 1:
	#agregamos la palabra, a la lista palabras, con el .append, que significa agregar o anadir
				palabra = input('ingresar palabra: ')
				lista_palabras.append(palabra)
				#cuando cumpla la condicion 2 ingresar
			elif opcion_palabra == 2:
				#mostramos el mensaje
				print(f'no ingresaste mas palabras.\nPalabras ingresadas:')
				print(lista_palabras)
			#print('total palabras'len.listas_palabras)
			#breack se cierre el ciclo y salga al menu principal
				break
			else:
				print('no existe')
				#condicion numero del menu princioal
	if opcion == 2:
		#le preguntamos al usuario la cantidad de intentos que desea, y se guarda en la variable maximo_intentos
		maximo_intentos = int(input('ingresar numero maximo de intentos: '))
		print(f'numero de intentos, {maximo_intentos}')
		#condicional numero 3
	if opcion == 3:
		#con el condicional if, estamos diciendo, si lista de palabra esta vacia, no se puede jugar
		if not lista_palabras:
			#mostramos mensaje
			print('no existen las palabras. no se puede jugar.')
		else:
			#importamos ramdon para seleccionar una palabra, donde escoja una palabra secreta de la lista de palabras
			palabra_secreta = random.choice(lista_palabras)
			#mostramos el mensaje
			print('palabra selecciona, preparados....')
			#importamos time para darle suspenso
			time.sleep(5)
			print('VAMOS A JUGAR')
			 # Creamos una lista con guiones bajos para ocultar la palabra
			palabra_oculta = ["_"] * len(palabra_secreta)
			#inciamos el contador de intentos en 0
			intentos = 0
			#creamos un ciclo while, para que el juego se repita hasta que se acierte
			while "_" in palabra_oculta and intentos < maximo_intentos:
				print("\n " + " ".join(palabra_oculta))
				#preguntamos al usuario que letra quiere adivinar
				letra = input("ingresar una letra: ")
				# Verificamos si la letra ingresada por el jugador está en la palabra secreta
				if letra in palabra_secreta:
    # Recorremos cada posición (índice) de la palabra secreta
					for i in range(len(palabra_secreta)):
        # Si la letra en la posición actual coincide con la letra ingresada
						if palabra_secreta[i] == letra:
            # Reemplazamos el guion bajo en esa posición por la letra correcta
							palabra_oculta[i] = letra
    # Informamos al jugador que adivinó correctamente
					print("¡Letra correcta!")
				else:
					# Si la letra no está en la palabra secreta, informamos al jugador y sumara los intentos
					intentos += 1
					print(f"letra incorrecta, intentos usados, {intentos}")
					#si el jugador adivina la palabra
			if "_" not in palabra_oculta:
				print("\nfelicidades adivinaste la palabra secreta", palabra_secreta)
				#si el jugador se queda sin intentos
			else:
				print("\nperdiste la palabra era", palabra_secreta)
	# cuando no escoge la opcion 1,2,3, por descarte queda la 4
	else:
		print("salir del juego")
