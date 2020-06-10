#Valdez Mondragon Erik
#Algoritmo del Abusón (Bully)
#Sistemas Distribuidos
#Facultad de Ingeniería, UNAM

import random
n = 0
procesos = []
 
#Estado de los procesos
#STBY = En espera
#UP = Principal
#DOWN = Caído e irrecuperable
 
 
def bully():
    print("Algoritmo del abusador (Bully)")
    print("Ingrese la cantidad de nodos y su valor: ", end = "")
    #Cantidad de nodos de string a entero, para el ciclo for
    n = int(input())
 
    #Ingresa el ID del proceso junto con el estado "STBY"
    #No repetir IDs
    for i in range(n):
        print("ID del proceso #" + str(i) + ": ", end ='')
        ID = int(input())
        procesos.insert(i, [ID, "STBY"])
 
    #El proceso con el ID más grande será el principal
    max(procesos)[1] = "UP"
 
    #Mostrar lista inicial de procesos
    ver_procesos()
 
    genera_falla(n)
 
    print("Solo queda un proceso en ejecución :( no puedes generar más fallas")
 
def genera_falla(n):
  if n > 1:
    print("Presiona 0 para generar una falla en el sistema ", end="")
    if input() == "0":
      n = n-1
      #Mata al proceso principal
      mata_proceso()
 
      #Envía mensajes de elección
      convoca_eleccion();
 
      #Muestra los procesos después de la elección
      ver_procesos()
 
      #Regresa a esta función para seguir generando fallas
      genera_falla(n)
    else:
      genera_falla(n)
 
 
#Cambia el estado del proceso principal a DOWN
def mata_proceso():
  for i in range(len(procesos)):
      if procesos[i][1] == "UP":
        procesos[i][1] = "DOWN"
        print("El proceso [" + str(procesos[i][0]) + "] ha fallado.")
 
def convoca_eleccion():
  #Cualquier proceso con un ID menor al principal puede convocar una elección
  #En teoría, todos los procesos en STBY saben sobre la falla del principal
  eleccion = random.choice(procesos)
 
  #Asegurar que no se elegió el proceso caido
  if eleccion[1] == "DOWN":
    convoca_eleccion()
  else:
    print("El proceso [" + str(eleccion[0]) + "] ha convocado a una elección")
 
    envia_mensajes(procesos, eleccion)
 
 
def envia_mensajes(aux, eleccion):
  print("El proceso [" + str(eleccion[0]) + "] enviará mensajes")
  procesos_elegidos = []
 
  #Ordena la lista de procesos para mandar mensajes de elección a los procesos con ID mayor al elegido
  aux = sorted(procesos)
  for i in range(len(aux)):
    if aux[i][0] > eleccion[0]:
      print(str(eleccion[0]) + " -> ELECCION -> " + str(aux[i][0]))
      procesos_elegidos.append(aux[i])
      #El proceso responderá si está en STBY
      if aux[i][1] == "STBY":
        print(str(aux[i][0]) + " <- OK <- " + str(eleccion[0]))
      else:
        print("NO HAY RESPUESTA")
 
 
  #print("Procesos con los que me comuniqué")
  #for i in range(len(procesos_elegidos)):
  #  print(procesos_elegidos[i])  
 
  #El siguiente proceso mayor al elector original volvera a enviar mensajes
  #Primero hay que asegurar que el nuevo proceso no sea el "DOWN"
  if procesos_elegidos[0][1] == "DOWN":
    #Si el siguiente proceso fue el caido, el proceso anterior será el nuevo proceso principal y se finaliza la convocatoria
    for i in range(len(procesos)):
      if procesos[i] == eleccion:
        procesos[i][0] = eleccion[0]
        procesos[i][1] = "UP"
        print("El proceso [" + str(eleccion[0]) + "] se convierte en principal.")
 
  else:
    envia_mensajes(procesos_elegidos, procesos_elegidos[0])
 
 
def ver_procesos():
    print("PROCESOS:")
    for i in range(len(procesos)):
      print(procesos[i])  
 
 
#Ejecuta el programa
bully()
