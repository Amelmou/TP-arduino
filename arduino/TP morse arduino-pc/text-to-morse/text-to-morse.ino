
int buttonPin= 12;


void text_to_morse() {
    //read the input pin
  int buttonState = digitalRead(buttonPin);

  //if the button is pressed
  if (buttonState == 1){
    Serial.write("1");
  }else{
    Serial.write("0");    
  }
}
void loop(){
  //pc_to_arduino();
  text_to_morse();
}
