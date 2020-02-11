var etiqueta;
function onloadFcn(){
	etiqueta=document.getElementById("led");
	etiqueta.innerHTML= "led 1";	
}

  // Create a client instance
  //client = new Paho.MQTT.Client("postman.cloudmqtt.com", 14970);
  
  client = new Paho.MQTT.Client("tailor.cloudmqtt.com", 30147, "web_" + parseInt(Math.random() * 100, 10));

  // set callback handlers
  client.onConnectionLost = onConnectionLost;
  client.onMessageArrived = onMessageArrived;
  var options = {
    useSSL: true,
    userName: "dcexfjor",
    password: "ICgqURN0dbCr",
    onSuccess:onConnect,
    onFailure:doFail
  }


  // connect the client
  client.connect(options);
  topic_rx="test";
  topic_tx='led';
  // called when the client connects
  function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("onConnect");
	
    client.subscribe(topic_rx);
    message = new Paho.MQTT.Message("holaaaa");
    message.destinationName = topic_tx;
    
	
  }

  function doFail(e){
    console.log(e);
	
  }

  // called when the client loses its connection
  function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("onConnectionLost:"+responseObject.errorMessage);
    }
  }

  // called when a message arrives
  function onMessageArrived(message) {
    console.log("el mensaje fue:"+message.payloadString);
	
	accion(message.payloadString);
  }
  
    // called when a message arrives
  function sendMessage(msg) {
    message = new Paho.MQTT.Message(msg);
    message.destinationName = topic_tx;
    client.send(message);
	
  }

    // called when a message arrives
  function led() {
	sendMessage('pao')	
  }
  
  function ledOnn(){
  sendMessage('led=1')
  }
  
  function ledOff(){
  sendMessage('led=0')
  }
  
  function accion(msg){
	mensaje=msg.split('=');
	if(mensaje[0]=='i')
		document.getElementById("sensor_i").innerHTML=mensaje[1];
	if(mensaje[0]=='p')
		document.getElementById("sensor_p").innerHTML=mensaje[1];
	if(mensaje[0]=='l')
		document.getElementById("sensor_l").innerHTML=mensaje[1];
	  
  
  }
  
 
