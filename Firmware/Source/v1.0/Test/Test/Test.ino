// Weather Station Firmware V1.0

#include <Wire.h>

#define SLAVE_ADDRESS 0x04

int cmd[5];
int index=0;
int flag=0;
int i;
byte val=0,b[21],float_array[4],dht_b[21],ultrasonic_b[3],mph_b[3];
unsigned char dta[21];
int length;
int aRead=0;
byte accFlag=0,clkFlag=0;
int8_t accv[3];
byte rgb[] = { 0, 0, 0 };
int run_once;

//Anenometer Variables
const int anenometerPin = 2;
int half_revolutions = 0;
int rpm = 0;
unsigned long lastmillis = 0;
float diameter = 2.75; //inches from center pin to middle of cup
long mph;


void setup()
{
    Serial.begin(9600);         // start serial for output
    Wire.begin(SLAVE_ADDRESS);

    Wire.onReceive(receiveData);
    Wire.onRequest(sendData);

    pinMode(anenometerPin, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(anenometerPin), wind, FALLING);
	//attachInterrupt(0,readPulseDust,CHANGE);
}
int pin;
int j;
void loop()
{
//Anenometer Read
if (millis() - lastmillis == 1000){
  detachInterrupt(0);
  rpm = half_revolutions * 30;
  half_revolutions = 0;
  lastmillis = millis();
  attachInterrupt(digitalPinToInterrupt(anenometerPin), wind, FALLING);
  //mph = diameter / 12 * 3.14 * rpm * 60 / 5280;
  //mph = mph * 3.5;

}


    //Digital Read
    if (cmd[0]==1)
      val=digitalRead(cmd[1]);

    //Digital Write
    else if(cmd[0]==2)
      digitalWrite(cmd[1],cmd[2]);

    //Analog Read
    else if(cmd[0]==3)
    {
      aRead=analogRead(cmd[1]);
      b[1]=aRead/256;
      b[2]=aRead%256;
    }

    //Set up Analog Write
    else if(cmd[0]==4)
      analogWrite(cmd[1],cmd[2]);

    //Set up pinMode
    else if(cmd[0]==5)
      pinMode(cmd[1],cmd[2]);


    //Firmware version
    else if(cmd[0]==8)
    {
      b[1] = 1;
      b[2] = 2;
      b[3] = 6;
    }

}

void receiveData(int byteCount)
{
    while(Wire.available())
    {
      if(Wire.available()==4)
      {
        flag=0;
        index=0;
		run_once=1;
      }
        cmd[index++] = Wire.read();
    }
}

// callback for sending data
void sendData()
{
  if(cmd[0] == 1)
    Wire.write(val);
  if(cmd[0] == 3 || cmd[0] == 56)
    Wire.write(b, 3);

  if(cmd[0] == 7)
  {
    Wire.write(rpm);
  }
  if(cmd[0] == 8 || cmd[0] == 20)
    Wire.write(b, 4);
  if(cmd[0] == 30)
    Wire.write(b, 9);
  if(cmd[0] == 40)
  {
    Wire.write(dht_b, 9);
    cmd[0] = 0;
  }

  if(cmd[0]==21)
  {
    Wire.write(b,21);
    b[0]=0;
  }

}
void wind(){
  half_revolutions++;
 }
