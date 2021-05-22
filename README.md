# ESP32-RC-car
RC car, which you can control from your PC.

![image][car]
 
## Things required

`Before we start you can use any other similar parts to build your car. You just need to adjust your car according to it.`




| Item | Image |
| --- | --- |
| RC car | <img src="media/rc-car.jpg" alt="Logo" width="80" height="80"> |
| L298N motor dc motor driver | <img src="media/l298n.jpg" alt="Logo" width="80" height="80"> |
| Antenna | <img src="media/antenna.jpg" alt="Logo" width="80" height="80"> |
| Buck Convertor | <img src="media/buck-convertor.jpg" alt="Logo" width="80" height="80"> |
| LIPO battery | <img src="media/lipo.jpg" alt="Logo" width="80" height="80"> |
| ESP32 | <img src="media/download.jpg" alt="Logo" width="80" height="80"> |
| ESP32 CAM | <img src="media/ESP32-Cam.jpg" alt="Logo" width="80" height="80"> |
| Servo motor | <img src="media/servo.jpg" alt="Logo" width="80" height="80"> |
| Header pins | <img src="media/header-pins.jpg" alt="Logo" width="80" height="80"> |
| Wires | <img src="media/wires.jpg" alt="Logo" width="80" height="80"> |
| PCB board | <img src="media/pcb.jpg" alt="Logo" width="80" height="80"> |

## Modifing the rc car

1. Open the outer shell.
   
   <img src="media/open.jpg" alt="Logo" width="400" height="200">
2. Remove all wiring and circuits.

    <img src="media/wiring.jpg" alt="Logo" width="400" height="200">

3. Cut slot in battery holder, for fitting lipo battery.
    
    <img src="media/cutslot.jpg" alt="Logo" width="400" height="200">
    <img src="media/slotver.jpg" alt="Logo" width="400" height="200">

4. Remove steering motor.(we will replace it with servo)
    
    <img src="media/wiring.jpg" alt="Logo" width="400" height="200">

5. Cut slots to accommodate servo motor.
   
    <img src="media/steer.jpg" alt="Logo" width="200" height="200">
    <img src="media/flip.jpg" alt="Logo" width="200" height="200">

6. Cut slots in servo arm like this for connecting to stering shaft.

    <img src="media/hand.jpg" alt="Logo" width="400" height="400">

7. Fix the servo to chassis with the help of few spacers.
    
    <img src="media/10.jpg" alt="Logo" width="400" height="200">
8. Put back the cover.

    <img src="media/8.jpg" alt="Logo" width="400" height="180">
9. Follow the schematic and solder the parts.

    <img src="media/Schematic-diagram.png" alt="Logo" width="400" height="300">

10. If you have done everything right it should look something like this.
     
     <img src="media/Schematic-diagram.png" alt="Logo" width="400" height="300">
     <img src="media/Schematic-diagram.png" alt="Logo" width="400" height="300">
     <img src="media/Schematic-diagram.png" alt="Logo" width="400" height="300">
     <img src="media/Schematic-diagram.png" alt="Logo" width="400" height="300">
     
     
12. If you are struck follow the following video.

## Code

1. Follow this [link](), where you can find how to setup client-server socket using micropython.
2. Now that you know how to setup socket for wireless connection. Modify files in esp32-files to setup your connection. 
3. Copy all the files in folder esp32 files to your esp32.
4. Confirm every thing is working before putting esp32 on car.
5. Now, turn on your car, wait for it to connect to your wifi. Once connected run client.py
6. Once connection is made you can drive the car using AWSD keys on keyboard.
7. You can change speed by changing the motorSpeed() function in server.py
8. If direction is reversed, flip the sign of motorSpeed() values.


## Contribution

Feel free to point out issues. You can contribute to this repo to improve it.

























[rc-car]: media/rc-car(1).jpg
[l298n]: media/img.jpg
[antenna]: media/img.jpg
[buck_convertor]: media/img.jpg
[lipo]: media/img.jpg
[esp32cam]: media/img.jpg
[servo]: media/img.jpg
[header]: media/img.jpg
[wires]: media/img.jpg
[pcb]: media/img.jpg
[esp32]: media/img.jpg
[car]: media/img.jpg
