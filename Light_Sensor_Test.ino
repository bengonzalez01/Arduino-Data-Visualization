int light_sen = A3;

void setup() {
  Serial.begin(9600);

}

void loop() {
  int raw_light = analogRead(light_sen);
  int light = map(raw_light, 0, 1023, 0, 100);


  Serial.println(light);

  delay(200);
}
