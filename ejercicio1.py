
#ejercicio1
#mensaje del ejercio, .center para centrar (50) es el campo de espacio
print('EJERCICIO 1'.center(50))

# 1.  **Adivina el número:**
#El ordenador elige un número y el jugador intenta adivinarlo. Puedes usar la función random para generar el número aleatorio.
#**Bibliotecas útiles: **
#•	random: Para generar números aleatorios y
#•	time: Para añadir pausas o controlar el flujo del juego.

#Se debe mostrar la opción ingresada por el usuario y la obtenida de manera aleatoria por el computador.  El programa debe indicar el #ganador En caso de empate se debe continuar hasta que haya un ganador. Utiliza funciones. puede determinar el número de intentos #máximo que puede emplear el usuario.

#**time ** En Python proporciona funciones relacionadas con el tiempo. Permite realizar tareas como medir el tiempo de ejecución de un #programa, pausar la ejecución, obtener la hora actual en diferentes formatos y trabajar con representaciones de tiempo.

#Un ejemplo de la función con time.sleep(segundos):

#mensaje de bienvenida al juego
print("Bienvenidos al Jugo de adivinanza.\nLa reglas son faciles, se tienen 5 juegos, el usuario,\ntiene que adivinar el numero al ordenador.\nLos numero van del 1 al 10. ")

print(" ")
#importamos las bibliotecas que vamos a necesitar, ramdon, es un numero aleatorio, y time, dara el tiempo entre juego y juego
import random
import time


#declaramos la primera funcion donde el usuario intenta adivinar el numero del ordenador
def jugar_partida ():
	#declaramos la variables, donde se alamacenara automaticamente el numero por el ordenador
	numero_ordenador = random.randint (1, 10)
	#delcaramos la variable para almacenar el numero por el usuario
	numero_usuario = int(input("Ingresar un numero del 1 al 10: "))
	#imprimimos el mensaje, donde nos muestra el numero que eleijio el usuario y el ordenador
	print(f"tu numero es: {numero_usuario}\nnumero del ordenador es: {numero_ordenador}")
	# con el condicional if, compramos si el numero de ordenador, es igual al numero de usuario, es punto para el usuario por adivinar,
	if numero_ordenador == numero_usuario:
		print(f"punto para el usuario, el numero era {numero_ordenador}")
		#se alamacenra 1 punto a favor del usaurio, y nada para ordenador
		return 1, 0
	#de lo contrario, si usuario no avidina el numero, punto a favor del ordenador
	else:
		print(f"punto para el ordenador, el numero era: {numero_ordenador}")
		return 0, 1

#creamos una seguna funcion que se encargara de llevar el puntaje del usuario  y ordenador, y tambien la roda de desempate
def jugar_juego():
	#declaramos las variables para almacenar los puntos del usuario y ordenador, empiezan en 0 porque no tiene puntos
	puntaje_usuario = 0
	puntaje_ordenador = 0
	rondas = 1 # contador de ronda empieza en 1
	# con el bucle while recorremos las rondas, la condicion tiene que ser igual a 5 para cumplir el ciclo
	while rondas <= 5:
		#imprimer el mensaje del numero de la ronda, empiza en 1 va hasta 5
		print(f"\n--- Ronda {rondas} ---")
		#llamamos a la funcion jugar_partida, para que el usuario adivin,
		#en el primer valor se guarda 1 que se guarda en el return, o al contrario si el punto sera para el ordenador
		punto_usuario, punto_ordenador = jugar_partida()
		#se almacenan los puntos al usuario y al ordenador
		puntaje_usuario += punto_usuario
		puntaje_ordenador += punto_ordenador
		#el contador de la rondas empiezan aumentar de 1 en 1
		rondas += 1
		time.sleep(2)
		print("Cargando...")

    # Si hay empate, jugar rondas extra, se repite todo
	while puntaje_usuario == puntaje_ordenador:
		print("\nEmpate, se jugará una ronda extra...")
		punto_usuario, punto_ordenador = jugar_partida()
		puntaje_usuario += punto_usuario
		puntaje_ordenador += punto_ordenador
		time.sleep(2)
		print("cargando...")

    # Mostrar resultado final
	print("\n--- Resultado final ---")
	#muestra el resultado del puntaje usuario
	print(f"Puntaje usuario: {puntaje_usuario}")
	#muestra el resultado de puntaje del ordenador
	print(f"Puntaje ordenador: {puntaje_ordenador}")
	#con el ciclo if, miramos la condicin, si puntaje usuario es mayor que ordenador, gana el usuari
	if puntaje_usuario > puntaje_ordenador:
		print(" ¡El usuario gana el juego!")
		#si no se cumple, else, imprime lo contarario
	else:
		print(" ¡El ordenador gana el juego!")
#este cilco while va por fuera, porqe no tiene nada que ver con el bloque central de las funciones
#con este ciclo while, le preguntamos al usuario, si desea jugar o salir
while True:
	juego = input("Desea jugar (si/no): ")
	#si el usuario dice si, cumple la primera condicion
	if juego == "si":
		#muestra el mensaje de ejecucion
		print("juego en ejecucion, esperar....")
		#dara un tiempo de 3 segungos para ejecutar el juego
		#y empezara a funcionar por que es muy pesado
		time.sleep(3)
		#llammos a la funcion jugar_juego, pra que se ejecute el bloque,
		#o lo que esta dentro de la funcion que es elprograma
		jugar_juego()
		# si el usuario elije no, se cierra el juego con el break
	else:
		print("¡ hasta luego !.")
		break