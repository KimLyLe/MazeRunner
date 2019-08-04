"""
This class is the template class for the MQTT client which receives MQTT messages 
and sends MQTT messages
"""
import paho.mqtt.client as mqtt
import time
import array as arr
import os
from MazeSolverAlgoTemplate import MazeSolverAlgoTemplate

if "MQTTSERVER" in os.environ and os.environ['MQTTSERVER']:
    mqtt_server = os.environ['MQTTSERVER']
else:
    mqtt_server = "127.0.0.1"

# HINT: it might be a good idea to copy this file into your team folder, e.g. TeamA
# HINT: it might be good idea to rename both the file and the class name
class MazeSolverClient:

    # initialize the MQTT client
    def __init__(self,master):
        # Master is a Member with no type, during runtime the type will be 
        # TODO: this is you job now :-)
        self.master=master
        self.master.on_connect=self.onConnect
        self.master.on_message=self.onMessage
        self.master.connect(mqtt_server,1883,60)

        print("Constructor Sample_MQTT_Publisher")
        self.master=master

        # HINT: here you should register the onConnect and onMessage callback functions
        #       it might be a good idea to look into file Framework\Test\test_mqtt_publisher.py

        self.master.connect(mqtt_server,1883,60)
        
        # This MQTT client forwards the requests, so you need a link to the solver
        # HINT: don't forget to create your algorithm class here, e.g.
        self.solver = MazeSolverAlgoTemplate()
        #pass

    # Implement MQTT publishing function
    def publish(self, topic, message=None, qos=0, retain=False):
        # TODO: this is you job now :-)
        # HINT: it might be a good idea to look into file Framework\Test\test_mqtt_publisher.py
        print("Published message: " , topic , " --> " , message)
        self.master.publish(topic,message,qos,retain)

    def solveMazeClient(self):
            # TODO: this is you job now :-)
            #HINT:  don't forget to publish the results, e.g.
            print('Was geht')
            for step in self.solver.solveMaze():
                print('Step: ', step)
                step_str = '{},{}'.format(step[0],step[1])
            
                self.publish("/maze/go" , step_str)

    # Implement MQTT receive message function -> Callback function that is called when we receive message
    def onMessage(self, master, obj, msg):
        # TODO: this is you job now :-)
        # HINT: it might be a good idea to look into file Framework\Test\test_mqtt_subscriber.py
        topic = str(msg.topic)
        payload = str(msg.payload.decode("utf-8"))
        print(" Received message: " , topic , " --> " , payload)
        if topic=="/maze":
            if payload == "clear":
                self.solver.clearMaze()
            elif payload == "start":
                self.solver.startMaze(0,0)
            elif payload == "solve":
                self.solveMazeClient()
            elif payload == "end":
                self.solver.startMaze(self.solver.dimRows,self.solver.dimCols)
                self.solver.endMaze()
                self.solver.printMaze()
            else:
                pass
        elif topic=="/maze/dimRow":
            self.solver.setDimRowsCmd(int(payload))
            self.solver.startMaze(self.solver.dimRows, self.solver.dimCols)
        elif topic=="/maze/dimCol":
            self.solver.setDimColsCmd(int(payload))
            self.solver.startMaze(self.solver.dimRows, self.solver.dimCols)
        elif topic=="/maze/startCol":
            self.solver.setStartColCmd(int(payload))
        elif topic=="/maze/startRow":
            self.solver.setStartRowCmd(int(payload))
        elif topic=="/maze/endCol":
            self.solver.setEndColCmd(int(payload))
        elif topic=="/maze/endRow":
            self.solver.setEndRowCmd(int(payload))
        elif topic=="/maze/blocked":
            cell = payload.split(",")
            self.solver.setBlocked(int(cell[0]),int(cell[1]))
        else:
            pass


    # Implement MQTT onConnecr function -> Callback function 
    def onConnect(self, master, obj, flags, rc):
        # TODO: this is you job now :-)
        # HINT: it might be a good idea to look into file Framework\Test\test_mqtt_subscriber.py
        self.master.subscribe("/maze" )
        self.master.subscribe("/maze/clear" )
        self.master.subscribe("/maze/start" )
        self.master.subscribe("/maze/dimRow" )
        self.master.subscribe("/maze/dimCol" )
        self.master.subscribe("/maze/startCol" )
        self.master.subscribe("/maze/startRow" )
        self.master.subscribe("/maze/endCol" )
        self.master.subscribe("/maze/endRow" )
        self.master.subscribe("/maze/blocked" )
        self.master.subscribe("/maze/end" )
        print("Connnect to mqtt-broker")

    # Initiate the solving process of the maze solver
   

    
if __name__ == '__main__':
    mqttclient=mqtt.Client()
    #HINT: maybe you rename the MazeSolverAlgoTemplate class ?
    solverClient = MazeSolverClient(mqttclient)
    solverClient.master.loop_forever()
