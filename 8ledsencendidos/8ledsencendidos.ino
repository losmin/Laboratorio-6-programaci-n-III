const int ledPins[] = {2, 3, 4, 5, 6, 7, 8, 9};  // Pines para los LEDs
const int pushbuttonPins[] = {10, 11, 12, 13};   // Pines para los pulsadores
const int numLeds = 8;
const int numPushbuttons = 4;

void setup() {
  Serial.begin(9600);  // Inicializar la comunicación serial

  // Configurar pines de salida para los LEDs
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
  }

  // Configurar pines de entrada para los pulsadores
  for (int i = 0; i < numPushbuttons; i++) {
    pinMode(pushbuttonPins[i], INPUT_PULLUP);
  }
}

void loop() {
  String ledStates = "";
  String pushbuttonStates = "";

  // Leer el estado de los LEDs
  for (int i = 0; i < numLeds; i++) {
    ledStates += digitalRead(ledPins[i]);
  }

  // Leer el estado de los pulsadores
  for (int i = 0; i < numPushbuttons; i++) {
    pushbuttonStates += !digitalRead(pushbuttonPins[i]);  // Invertir el estado debido a la resistencia pull-up
  }

  // Enviar los estados al Python
  Serial.println(ledStates + pushbuttonStates);

  delay(100);  // Pequeño retraso para evitar sobrecarga de datos
}