int d_pulgar = A0;
int d_indice = A1;
int d_medio = A2;
int d_anular = A3;
int d_menique = A4;
int senalpulgar = 0;
int senalindice = 0;
int senalmedio = 0;
int senalanular = 0;
int senalmenique = 0;
void setup() {
  Serial.begin(9600);
  pinMode (d_pulgar, INPUT);
  pinMode (d_indice, INPUT);
  pinMode (d_medio, INPUT);
  pinMode (d_anular, INPUT);
  pinMode (d_menique, INPUT);
  delay (1000);
}

void loop() {
  senalpulgar = analogRead(d_pulgar);
  senalindice = analogRead(d_indice);
  senalmedio = analogRead(d_medio);
  senalanular = analogRead(d_anular);
  senalmenique = analogRead(d_menique);
  // U //
  if ( senalpulgar >= 70 && senalpulgar <= 140 && senalindice >= 180 && senalindice <= 280 && senalmedio >= 250 && senalmedio <= 400 && senalanular >= 430 && senalanular <= 630 && senalmenique >= 200 && senalmenique <= 370)
  {
    Serial.println("U");
    delay (1000);
  }
  // O //
  if ( senalpulgar >= 130 && senalpulgar <= 220 && senalindice >= 250 && senalindice <= 350 && senalmedio >= 300 && senalmedio <= 460 && senalanular >= 550 && senalanular <= 650 && senalmenique >= 370 && senalmenique <= 500)
  {
    Serial.println("O");
    delay (1000);
  }
  // I //
  if ( senalpulgar >= 120 && senalpulgar <= 230 && senalindice >= 300 && senalindice <= 380 && senalmedio >= 250 && senalmedio <= 390 && senalanular >= 450 && senalanular <= 550 && senalmenique >= 120 && senalmenique <= 300)
  {
    Serial.println("I");
    delay (1000);
  }
  // E //
  if ( senalpulgar >= 150 && senalpulgar <= 250 && senalindice >= 300 && senalindice <= 400 && senalmedio >= 400 && senalmedio <= 550 && senalanular >= 520 && senalanular <= 650 && senalmenique >= 200 && senalmenique <= 400)
  {
    Serial.println("E");
    delay (1000);
  }
  // A //
  if ( senalpulgar >= 80 && senalpulgar <= 130 && senalindice >= 220 && senalindice <= 320 && senalmedio >= 250 && senalmedio <= 350 && senalanular >= 430 && senalanular <= 580 && senalmenique >= 380 && senalmenique <= 500)
  {
    Serial.println("A");
    delay (1000);
  }
  // Palabra //
  if ( senalpulgar >= 90 && senalpulgar <= 150 && senalindice >= 270 && senalindice <= 370 && senalmedio >= 250 && senalmedio <= 350 && senalanular >= 110 && senalanular <= 250 && senalmenique >= 130 && senalmenique <= 250)
  {
    Serial.println("B");
    delay (1000);
  }
}
