const int ledPin = 3;
int incomingByte = 1;
const long sleepTimeDefault = 10000;

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH);
  // initialize serial communications:
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    int sleepTime = sleepTimeDefault;
    incomingByte = Serial.read();
    // recebeu do computador um '0' para desligar a tomada
    if (incomingByte == 48) { // 48 = ASCII 0
      digitalWrite(ledPin, LOW);
      Serial.print("{\"status\":\"off\",\"duration\":");
      Serial.print(sleepTime, DEC);
      Serial.println("}");
      delay(sleepTime);
      digitalWrite(ledPin, HIGH);
      incomingByte = 1;
      Serial.println("{\"status\":\"on\"}");
    } else {
      Serial.println("{\"status\":\"on\",\"msg\":\"not allowed\"}");
    }
  }
  delay(1);        // delay in between reads for stability
}
