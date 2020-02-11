import RPi.GPIO as GPIO # Importe de las librerías de los pines de entrada y salida.
import time #Para manejar tareas relacionadas con tiempo.
GPIO.setmode(GPIO.BOARD) # Para que permita definir los pines de la salida mediante un número.
GPIO.setup(12, GPIO.OUT) # Define el Pin 7 como un puerto GPIO de salida.
while True: # función para que se mantenga en ejecución el código
 GPIO.output(12, True) # Activa el Puerto GPIO 7 , es decir 1 lógico.
 time.sleep(1) #Se mantiene el puerto GPIO 7 durante en 1 segundo.
 GPIO.output(12, False) # Desactiva el Puerto GPIO 7 , es decir 0 lógico.
 time.sleep(1) #Se mantiene el puerto GPIO 7 apagado en 1 segundo.
