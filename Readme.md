# **Powerpoint Controller**

##

The entire idea based on: </br>
If you do not want to stand in front of the laptop during the presentation so you decdied to use a Powerpoint controller to switch between the slides.

<span style="color: red;">**The problem:**</span>

    There is no such a device in your school or in your university :(

<span style="color: green;">**The solution:**</span>

    Let make one

##

## Project structure

</br>

![alt text](/Images/Project.PNG)

### Components & supplies :

1. Arduino Uno
2. HC-05 Board
3. Jumper cables

### Softwares & web application :

1. MIT app inventor
2. Arduino IDE
3. PyCharm

---

## Let develop the App

I used MIT app inventor, it is a web application integrated development environment originally provided by Google, and now maintained by the Massachusetts Institute of Technology.

You only need a Google accoount to develop the App

### App Design

</br>

![alt text](/Images/AppDesignerView.PNG)

### App Code

</br>

Setup the Bluetooth conection:
</br>

![alt text](/Images/SetupBluetoothConnection.png)
</br>

To show and to check if the connection is successful or not:
</br>

![alt text](/Images/BluetoothConnectionChecker.png)
</br>

Sending Data if the connection is successful:
</br>

![alt text](/Images/App-logic.png)
</br>

---

## Let receive data from the App to the Arduino:

### the circuit:

</br>

![alt text](/Images/Circuit.PNG)
</br>

### the code:

</br>

```C
char datafromUser=0;
void setup(){
Serial.begin(9600);
}
void loop(){
if(Serial.available() > 0){
    datafromUser=Serial.read();
    Serial.println(datafromUser);
    }
}
```

---

## Let process the received data in python

First of all, we need to install to python libraries

    pip install pyserial

and then

    pip install PyAutoGUI

### the code:

```Python
import serial
import pyautogui
ser = serial.Serial('COM5',9600)
ser.flushInput()
while True:
        ser_data = ser.readline()
        data = chr(ser_data[0])
        print(data)
        if data == "R":
                pyautogui.press('right')
        if data == "L":
                pyautogui.press('left')

```

---

<span style="color: green;">**Happy Hack :)**</span>


