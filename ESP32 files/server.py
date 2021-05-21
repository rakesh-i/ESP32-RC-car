#command_server.py


def soc():
    import socket               # Import socket module
    import time
    import json
    p1 = Pin(13)
    servo = PWM(p1, freq=50)
    
    
    s = socket.socket()         # Create a socket object
    host = '111.111.111.111'    # Ip of esp32 on network
    port = 12345                # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    s.listen(5)                 # Now wait for client connection.
    
    while True:
        c, addr = s.accept()     # Establish connection with client.
        print ('Got connection from', addr)
        while True:
            d = 'thank you for connection'
            data = str(d)
            msg =str.encode(data, 'utf-8')
            c.send(msg)
            a = c.recv(2048)
            com = a.decode()
            de = json.loads(com)
            if de["w"] == 1 and de["s"] == 0:
                motor.motorSpeed(-1000)
            if de["s"] == 1 and de["w"] == 0:
                motor.motorSpeed(1000)
            if de["a"] == 1 and de["d"] == 0:
                servo.duty(55)
            if de["d"] == 1 and de["a"] == 0:
                servo.duty(89)
            if de["d"] == 0 and de["a"] == 0:
                servo.duty(75)
            if de["w"] == 0 and de["s"] == 0:
                motor.motorSpeed(0)
                
            print(de)