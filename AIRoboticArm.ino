#include<Servo.h>

#define numsofValsRec 5
#define digitsPerVal 1

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

int valsRec[numsofValsRec];
//$00000
int stringLength = numsofValsRec*digitsPerVal + 1;
int counter = 0;
bool countStart = false;
String receivedString;




void setup() {
 Serial.begin(9600);
 servo1.attach(8);
 servo2.attach(9);
 servo3.attach(10);
 servo4.attach(11);
 servo5.attach(12);
}

void receivedata(){
  while(Serial.available()){
    char c = Serial.read();
    if (c=='$'){
      countStart = true;
    }
    if(countStart){
      if(counter < stringLength){
        receivedString = String(receivedString + c); 
        counter++;  
      }
      if(counter >= stringLength){
        for(int i = 0;i<numsofValsRec;i++){
          int num = (i*digitsPerVal) + 1;
          valsRec[i] = receivedString.substring(num,num + digitsPerVal).toInt(); 
        }
        receivedString = "";
        counter = 0;
        countStart = false;
      }
    }
  }
}


void loop() {
  receivedata();
  if(valsRec[0] == 1){
    servo1.write(180);
  }
  else{
    servo1.write(0);
  }
  if(valsRec[1] == 1){
    servo2.write(180);
  }
  else{
    servo2.write(0);
  }
  if(valsRec[2] == 1){
    servo3.write(0);
  }
  else{
    servo3.write(180);
  }
  if(valsRec[3] == 1){
    servo4.write(180);
  }
  else{
    servo4.write(0);
  }
  if(valsRec[4] == 1){
    servo5.write(180);
  }
  else{
    servo5.write(0);
  }
}
