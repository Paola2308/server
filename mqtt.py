import passw                                     #almacena datos de credenciales
import paho.mqtt.client as mqtt                  
import os, urlparse

#led=1/0
#sensor=p/i/l
#['led','0']

def accion (msg):
    mensaje=msg.split('=')
    if mensaje[0]=='led':
        if int(mensaje[1]):
            print('led on')
        else:
            print('led off')   



# Define event callbacks
def publish(msg):
	print (msg)
	mqttc.publish(topic_tx, msg)
    
#def publish(topic,msg):
#	print (msg)
#	mqttc.publish(topic, msg)
    
    
#publicarT('10;15;100,0')
#mensaje=msg.split(',');
#sensor_p.innerHTML=mensaje[0];
#sensor_i.innerHTML=mensaje[1];
#sensor_l.innerHTML=mensaje[2];


def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def new_message(client, obj, msg):
    #print('new message'=+str(msg.payload));
    accion(str(msg.payload))
    

def on_publish(client, obj, mid):
    pass
    #print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = new_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log


# Connect
mqttc.username_pw_set(passw.user, passw.psw)
mqttc.connect(passw.server, passw.port)
topic='test'
# Start subscribe, with QoS level 0
mqttc.subscribe('led', 0)

# Publish a message
mqttc.publish(topic, 'test')
#mqttc.publish(topic,topic)
# Continue the network loop, exit when an error occurs
rc = 0
import time
i=0
while rc == 0:
	time.sleep(2)
	i=i+1
	mqttc.publish(topic, 'i='+str(i)) 
	rc=mqttc.loop() #comando para recibir mensajes
print("rc: " + str(rc))






