int LED = 2;
int data;

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    data = Serial.read();

    Serial.println("received " + data);

    if (data == '1') {
      digitalWrite(LED, HIGH);
      //Serial.println("Turn on LED");
    } else if (data == '0') {
        digitalWrite(LED, LOW);
        //Serial.println("Turn off LED");
    }
  }
}