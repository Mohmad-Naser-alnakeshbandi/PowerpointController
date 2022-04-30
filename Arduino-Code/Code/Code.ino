char datafromUser=0;



void setup() 
{
  Serial.begin(9600);
}
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)
  {
    datafromUser=Serial.read();
    Serial.println(datafromUser);
  }
}