#!/usr/bin/python

try:
	from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
except:
	from http.server import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
try:
	from urlparse import urlparse
	from urlparse import urlparse, parse_qs
except:
	from urllib.parse import urlparse, parse_qs

import os #asigna un puerto manualmente 
port = int(os.environ.get("PORT", 5000))	
PORT_NUMBER = port

def lenOn():
print('led on')
def lenOff:
print('led off')


#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler): #existe metodos get y post  y el get se dispara cuando se abre la pagina web
	
	#Handler for the GET requests
	def do_GET(self):
    
		path=self.path                       #path es parte de la direccion es el / despues de url
		print(self.path.split('/')[-1])
		nombre=self.path.split('/')[-1]
		datos=''
        
		if (self.path=='/led on');
		ledOn();
		if (self.path=='/led off');
		ledOff();
        
		if self.path=="/":  #127.0.0.1:5000/
			nombre="index.html" #127.0.0.1:5000/index.html
		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False                        #especifica el tipo de respuesta da un mensaje al servidor 
			if nombre.endswith(".html"):                 #cuando termina con html es que es tipo texto
				mimetype='text/html'                      #tipo texto en formato html
				f=open(nombre)
				datos=f.read()
				f.close()
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):                       
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				#f = open(curdir + sep + self.path,'r') 
				self.send_response(200)                  # el codigo 200 es una respuesta exitosa
				self.send_header('Content-type',mimetype)
				self.end_headers()
				
				try:
					self.wfile.write(datos)                  #envia respuesta dependiendo si voy a trabajoar en python 2 o 3
				except:
					self.wfile.write(bytes(datos, 'UTF-8'))   #paython 3
				
			return


		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('0.0.0.0', PORT_NUMBER), myHandler)           #cuando especifique la direccion recibe peticiones de cualaquuier ip y 0.0.0. es acceder al computador
	print ('Started httpserver on port ' , PORT_NUMBER)
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print ('^C received, shutting down the web server')
	server.socket.close()
	