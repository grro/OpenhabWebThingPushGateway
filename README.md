# OpenhabWebThingPushGateway
A push gateway sending webthing properties updates to a openhab server

This project provides a background service connecting devices supporting the [webthing API](https://iot.mozilla.org/wot/) to the [Openhab](https://www.openhab.org/) automation system. 

Internally the service uses the web socket notification capability of the webthing api to listen for changes. If a webthing property is updated, the service will use the REST api of the OPenhab installation 
to update the assoiciated Openhab item.

For each link (webthing property <-> openhab item association) an entry in a gateway config file has to be placed. E.g. a concrete config file may look lie
```
# webthing_root_uri, webthing_property_name, openhab_root_uri, openhab_item_name
http://192.168.1.21:9131/, temperature, http://192.168.1.12:8080, TempCurrent
http://192.168.1.21:9132/, windspeed, http://192.168.1.12:8080, WindspeedCurrent
http://192.168.1.187:9045/, motion, http://192.168.1.12:8080, MotionGroundfloor
```
The first entry is the webthing endpoint uri, the second the property name to link. 
The third parameter is the endpoint uri of the openhab installation, the fourth is the item name which may differ from the webthing propertyname      

To service can be started manually via command line using
```
sudo pushgateway --command listen --filename /etc/conf/gateway.conf
```
 
Alternatively to the *listen* command, you can use the *register* command to register and start the service as systemd unit. 
By doing this the service will be started automatically on boot. Starting the server manually using the *listen* command is no longer necessary. 
```
sudo pushgateway --command register --filename /etc/conf/gateway.conf
```  

To install this software you may use [PIP](https://realpython.com/what-is-pip/) package manager such as shown below
```
sudo pip install pushgateway
```
