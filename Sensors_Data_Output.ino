#include "Arduino_SensorKit.h"
int light_sen = A3; 
int sound_sen = A2;
float pressure;
void setup() {
  Serial.begin(9600);
  Pressure.begin();
  Environment.begin();
}

void loop() {
  // Light Sensor
  int raw_light = analogRead(light_sen); 
  int light = map(raw_light, 0, 1023, 0, 100);

  // Sound Sensor
  int soundValue = 0; 
  for (int i = 0; i < 32; i++) 
  { soundValue += analogRead(sound_sen);  } 
  soundValue >>= 5;
  
  //Printing Values
  
  
  Serial.print(Pressure.readPressure());
  Serial.print("x");
  
  Serial.print(Pressure.readAltitude());
  Serial.print("x");

  Serial.print(light);
  Serial.print("x");
  
  Serial.print(soundValue); 
  Serial.print("x");
  
  Serial.print(Environment.readTemperature()); 
  Serial.print("x");
  
  Serial.println(Environment.readHumidity()); 
 
  delay(500);
}
