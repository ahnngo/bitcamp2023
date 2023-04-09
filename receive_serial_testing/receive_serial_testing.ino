int LED = 2;
int data;
unsigned long startTime;

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, LOW);
}

void loop() {
    if (Serial.available() > 0) {
        data = Serial.read();
        startTime = millis();
        while (millis() - startTime <= 5000) {
            digitalWrite(LED, HIGH);
            delay(200);
            digitalWrite(LED, LOW);
            delay(200);
        }
    }
}