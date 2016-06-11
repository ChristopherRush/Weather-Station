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

//rain sensor
int rainpin = 3;
int inches;
int state;

void setup()
{
    Serial.begin(9600);         // start serial for output
    Wire.begin(SLAVE_ADDRESS);

    Wire.onReceive(receiveData);
    Wire.onRequest(sendData);

    pinMode(anenometerPin, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(anenometerPin), rpm_fan, FALLING);



}
int pin;
int j;
void loop()
{
//Anenometer Read
if (millis() - lastmillis == 1000){ //Uptade every one second, this will be equal to reading frecuency (Hz).
 detachInterrupt(0);//Disable interrupt when calculating
 rpm = half_revolutions; // Convert frecuency to RPM, note: this works for one interruption per full rotation. For two interrups per full rotation use half_revolutions * 30.

 half_revolutions = 0; // Restart the RPM counter
 lastmillis = millis(); // Uptade lasmillis
 attachInterrupt(0, rpm_fan, FALLING); //enable interrupt
  }

//Rain Gauge
state = digitalRead(rainpin);
if (state == HIGH){

  inches++;
  delay(500);
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
    else if(cmd[0]==7)
    {
      val = rpm;
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
  if(cmd[0] == 6)
  {
  Wire.write(inches);
  }
  if(cmd[0] == 7)
  {
    Wire.write(val);
  }


}
void rpm_fan(){
  half_revolutions++;
 }
