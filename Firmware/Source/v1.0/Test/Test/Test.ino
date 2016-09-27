

#include <Wire.h>
#include <DHT.h>

#define DHTPIN 6
#define SLAVE_ADDRESS 0x04
#define DHTTYPE DHT22

int cmd[5];
int index=0;
int flag=0;
int i;
byte val=0,b[21],float_array[4],mph_b[3],rate=0, mm=0, hum=0, tmp=0;
unsigned char dta[21];
int length;
int aRead=0;
byte accFlag=0,clkFlag=0;
int8_t accv[3];

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

int h;
int t;
DHT dht(DHTPIN, DHTTYPE);

int pin;
int j;

void setup()
{
    dht.begin();
    pinMode(13, OUTPUT);
    //Serial.begin(9600);
    Wire.begin(SLAVE_ADDRESS);

    Wire.onReceive(receiveData);
    Wire.onRequest(sendData);

    pinMode(anenometerPin, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(anenometerPin), rpm_fan, FALLING);


}

void loop(){

if (millis() - lastmillis == 1000){
  detachInterrupt(0);
  rpm = half_revolutions;
  half_revolutions = 0;
  lastmillis = millis();
  attachInterrupt(0, rpm_fan, FALLING);
  }

state = digitalRead(rainpin);
if (state == HIGH){
  digitalWrite(13, HIGH);
  inches++;
  delay(100);
}
else{
  digitalWrite(13, LOW);
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
    rate = rpm;
  }
else if(cmd[0]==6)
  {
    mm = inches;
  }
else if(cmd[0]==8)
  {
  h = dht.readHumidity();
  hum = h;
  }
else if(cmd[0]==9)
  {
  t = dht.readTemperature();
  tmp = t;
  }

//Set up Analog Write
else if(cmd[0]==4)
  analogWrite(cmd[1],cmd[2]);

//Set up pinMode
else if(cmd[0]==5)
  pinMode(cmd[1],cmd[2]);
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


void sendData()
{
  if(cmd[0] == 1){
    Wire.write(val);
  }
  else if(cmd[0] == 3){
    Wire.write(b, 3);
  }
  else if(cmd[0] == 6)
  {
    Wire.write(mm);
  }
  else if(cmd[0] == 7)
  {
    Wire.write(rate);
  }
  else if(cmd[0] == 8)
  {
   Wire.write(hum);
  }
  else if(cmd[0] == 9)
  {
  Wire.write(tmp);
  }
}



void rpm_fan(){
  half_revolutions++;
 }
